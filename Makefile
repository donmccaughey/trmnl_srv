TMP ?= $(abspath tmp)

container := trmnl_srv
image := trmnl_srv


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
		$(container) sh -l


.PHONY : stop
stop :
	-docker stop $(container)
	rm -rf $(TMP)/docker-run.stamp.txt


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


$(TMP)/deploy.stamp.txt : $(TMP)/trmnl_srv.tar.gz
	rsync --archive $< don@10.0.0.100:~


$(TMP)/docker-build.stamp.txt : \
		$(container_files) \
		$(src_files) \
		| $$(dir $$@)
	docker build \
		--file container/Dockerfile \
		--platform linux/amd64 \
		--tag $(image) \
		--quiet \
		.
	date > $@


$(TMP)/docker-run.stamp.txt : \
		$(TMP)/docker-build.stamp.txt \
		stop \
		| $$(dir $$@)
	-docker rm $(container)
	docker run \
		--detach \
		--name $(container) \
		--platform linux/amd64 \
		--publish 4002:80 \
		$(image)
	date > $@


$(TMP)/pytest.stamp.txt : \
		$(python_files) \
		$(TMP)/uv-sync.stamp.txt \
		| $$(dir $$@)
	uv run -m pytest --quiet --quiet
	date > $@


$(TMP)/trmnl_srv.tar.gz : \
		$(TMP)/docker-build.stamp.txt \
		| $$(dir $$@)
	docker image save $(image) | gzip > tmp/$(image).tar.gz


$(TMP)/uv-sync.stamp.txt : uv.lock | $$(dir $$@)
	uv sync --frozen
	date > $@


$(TMP)/ :
	mkdir -p $@
