TMP ?= $(abspath tmp)

RSYNC_FLAGS ?= \
		--compress \
		--delete \
		--exclude '__pycache__' \
		--exclude '*_test.py' \
		--quiet \
		--recursive \
		--rsh ssh \
		--times

container_name := trmnl_srv
image_name := trmnl_srv


.SECONDEXPANSION :


.PHONY : all
all : check


.PHONY : build
build : $(TMP)/docker-build.stamp.txt


.PHONY : check
check : $(TMP)/pytest.stamp.txt


.PHONY : deploy
deploy : $(TMP)/deploy.stamp.txt


.PHONY : clean
clean :
	rm -rf $(TMP)


.PHONY : clobber
clobber : clean
	rm -rf .venv


.PHONY : run
run : $(TMP)/docker-run.stamp.txt


.PHONY : shell
shell : $(TMP)/docker-run.stamp.txt
	docker exec \
		--interactive \
		--tty \
		$(container_name) sh -l


.PHONY : stop
stop :
	-docker stop $(container_name)
	rm -rf $(TMP)/docker-run.stamp.txt


alpine_files := \
		alpine/etc/cron.d/trmnl \
		alpine/etc/init.d/trmnl_srv

container_files := \
		.dockerignore \
		container/etc/nginx/nginx.conf \
		container/etc/profile.d/dir.sh \
		container/srv/www/index.html \
		container/usr/local/sbin/trmnl_srv \
		container/Dockerfile

src_files := \
		src/gather/__init__.py \
		src/gather/__main__.py \
		src/gather/weather.py \
		src/gather/weather_test.py \
		\
		src/render/__init__.py \
		src/render/__main__.py \
		src/render/AtkinsonHyperlegibleMono-Regular.otf \
		src/render/screen.py \
		\
		src/serve/__init__.py \
		src/serve/__main__.py \
		\
		src/serve_trmnl \
		src/update_trmnl

python_files := $(filter %.py, $(src_files))

python_sources := $(filter-out %_test.py, $(python_files))

python_tests := $(filter %_test.py, $(python_files))

resource_files := $(filter-out %.py, $(src_files))


uv.lock : pyproject.toml .python-version
	uv sync
	touch $@


$(TMP)/deploy.stamp.txt : \
		$(TMP)/pytest.stamp.txt \
		$(alpine_files) \
		$(src_files)
	rsync \
		$(RSYNC_FLAGS) \
		src/ \
		donmcc@10.1.1.1:~/trmnl_srv/
	rsync \
		$(RSYNC_FLAGS) \
		alpine/ \
		donmcc@10.1.1.1:~/trmnl_setup/
	date > $@


$(TMP)/docker-build.stamp.txt : \
		$(container_files) \
		$(src_files) \
		| $$(dir $$@)
	docker build \
		--file container/Dockerfile \
		--platform linux/amd64 \
		--tag $(image_name) \
		--quiet \
		.
	date > $@


$(TMP)/docker-run.stamp.txt : \
		$(TMP)/docker-build.stamp.txt \
		stop \
		| $$(dir $$@)
	-docker rm $(container_name)
	docker run \
		--detach \
		--name $(container_name) \
		--platform linux/amd64 \
		--publish 4002:80 \
		$(image_name)
	date > $@


$(TMP)/pytest.stamp.txt : \
		$(python_files) \
		$(TMP)/uv-sync.stamp.txt \
		| $$(dir $$@)
	uv run -m pytest --quiet --quiet
	date > $@


$(TMP)/uv-sync.stamp.txt : uv.lock | $$(dir $$@)
	uv sync --frozen
	date > $@


$(TMP)/ :
	mkdir -p $@
