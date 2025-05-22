DEPLOY_BASE_URL := http://10.0.0.100:4000
DEV_BASE_URL ?= http://127.0.0.1:4000
PORT ?= 4000
TMP ?= $(abspath tmp)

container := trmnl_srv
deploy_image := trmnl_srv
dev_image := trmnl_srv_dev


.SECONDEXPANSION :


.PHONY : all
all : check


.PHONY : build
build : $(TMP)/docker-build-dev.stamp


.PHONY : check
check : $(TMP)/pytest.stamp


.PHONY : deploy
deploy : $(TMP)/deploy.stamp


.PHONY : clean
clean :
	rm -rf $(TMP)


.PHONY : clobber
clobber : clean
	rm -rf .venv


.PHONY : run
run : $(TMP)/docker-run.stamp


.PHONY : shell
shell : $(TMP)/docker-run.stamp
	docker exec \
		--interactive \
		--tty \
		$(container) sh -l


.PHONY : stop
stop :
	-docker stop $(container)
	rm -rf $(TMP)/docker-run.stamp


container_files := \
		.dockerignore \
		container/etc/crontabs/root \
		container/etc/nginx/nginx.conf \
		container/etc/profile.d/dir.sh \
		\
		container/srv/www/api/display/index.json \
		container/srv/www/api/setup/index.json \
		\
		container/srv/www/content/bitmap/index.png \
		container/srv/www/content/index.json \
		\
		container/srv/www/fonts/Atkinson-Hyperlegible-Bold-102a.woff2 \
		container/srv/www/fonts/Atkinson-Hyperlegible-BoldItalic-102a.woff2 \
		container/srv/www/fonts/Atkinson-Hyperlegible-Italic-102a.woff2 \
		container/srv/www/fonts/Atkinson-Hyperlegible-Regular-102a.woff2 \
		\
		container/srv/www/index.html \
		\
		container/usr/local/sbin/gather-render \
		container/usr/local/sbin/serve \
		container/usr/local/sbin/trmnl_srv \
		\
		container/Dockerfile

src_files := \
		src/gather/__init__.py \
		src/gather/__main__.py \
		src/gather/giants-schedule.json \
		src/gather/giants_games.py \
		src/gather/giants_games_test.py \
		src/gather/options.py \
		src/gather/weather.py \
		src/gather/weather_test.py \
		\
		src/render/__init__.py \
		src/render/__main__.py \
		src/render/api_display.py \
		src/render/api_setup.py \
		src/render/AtkinsonHyperlegibleMono-Regular.otf \
		src/render/bitmap.py \
		src/render/constants.py \
		src/render/date_and_time.py \
		src/render/forecast.py \
		src/render/giants_games_today.py \
		src/render/intro_screen.py \
		src/render/logs.py \
		src/render/options.py \
		src/render/refresh_rate.py \
		src/render/screen.py \
		\
		src/serve/__init__.py \
		src/serve/__main__.py \
		src/serve/handler.py \
		src/serve/log_entry.py \
		src/serve/options.py \
		src/serve/server.py \
		\
		src/utils/__init__.py

python_files := $(filter %.py, $(src_files))

python_sources := $(filter-out %_test.py, $(python_files))

python_tests := $(filter %_test.py, $(python_files))

resource_files := $(filter-out %.py, $(src_files))


uv.lock : pyproject.toml .python-version
	uv sync
	touch $@


$(TMP)/deploy.stamp : $(TMP)/trmnl_srv.tar.gz
	rsync --archive $< don@10.0.0.100:~
	ssh don@10.0.0.100 '/bin/bash -l -s' < scripts/deploy.sh
	touch $@


$(TMP)/docker-build-deploy.stamp : \
		$(container_files) \
		$(src_files) \
		| $$(dir $$@)
	docker build \
		--build-arg DEPLOY_BASE_URL="$(DEPLOY_BASE_URL)" \
		--file container/Dockerfile \
		--platform linux/amd64 \
		--tag $(deploy_image) \
		--quiet \
		.
	touch $@


$(TMP)/docker-build-dev.stamp : \
		$(container_files) \
		$(src_files) \
		| $$(dir $$@)
	docker build \
		--build-arg DEV_BASE_URL="$(DEV_BASE_URL)" \
		--file container/Dockerfile \
		--platform linux/amd64 \
		--tag $(dev_image) \
		--quiet \
		.
	touch $@


$(TMP)/docker-run.stamp : \
		$(TMP)/docker-build-dev.stamp \
		| $$(dir $$@)
	-docker stop $(container)
	-docker rm $(container)
	docker run \
		--detach \
		--env DEV_BASE_URL="$(DEV_BASE_URL)" \
		--init \
		--name $(container) \
		--platform linux/amd64 \
		--publish $(PORT):80 \
		$(dev_image)
	touch $@


$(TMP)/pytest.stamp : \
		$(python_files) \
		$(TMP)/uv-sync.stamp \
		| $$(dir $$@)
	uv run -m pytest --quiet --quiet
	touch $@


$(TMP)/trmnl_srv.tar.gz : \
		$(TMP)/docker-build-deploy.stamp \
		| $$(dir $$@)
	docker image save $(deploy_image) | gzip > $@


$(TMP)/uv-sync.stamp : uv.lock | $$(dir $$@)
	uv sync --frozen
	touch $@


$(TMP)/ :
	mkdir -p $@
