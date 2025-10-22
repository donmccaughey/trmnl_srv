DEPLOY_BASE_URL := http://10.0.0.100:4000
DEV_BASE_URL ?= http://127.0.0.1:4000
FIVE11_ORG_KEY ?= $(shell cat secrets/five11-org-key.txt)
PORT ?= 4000
TMP ?= $(abspath tmp)

container := trmnl_srv
container_files := \
	.dockerignore \
	$(shell find container/ -type f -not -name '.DS_Store')
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


src_files := \
		src/common/http_message/__init__.py \
		src/common/http_message/entity.py \
		src/common/http_message/header.py \
		src/common/http_message/header_test.py \
		src/common/http_message/message.py \
		src/common/http_message/message_test.py \
		src/common/http_message/octet_entity.py \
		src/common/http_message/octet_entity_test.py \
		src/common/http_message/request.py \
		src/common/http_message/request_test.py \
		src/common/http_message/response.py \
		src/common/http_message/text_entity.py \
		src/common/http_message/text_entity_test.py \
		\
		src/common/logs/__init__.py \
		src/common/logs/log_storage.py \
		src/common/logs/trmnl_log_entry.py \
		\
		src/common/serialize/__init__.py \
		src/common/serialize/decodable.py \
		src/common/serialize/deserializable.py \
		src/common/serialize/encodable.py \
		src/common/serialize/jsontype.py \
		src/common/serialize/serializable.py \
		\
		src/common/__init__.py \
		src/common/atomic_write.py \
		src/common/common_options.py \
		src/common/common_options_test.py \
		\
		src/gather/__init__.py \
		src/gather/__main__.py \
		src/gather/five11.py \
		src/gather/five11_test.py \
		src/gather/giants-schedule.json \
		src/gather/giants_games.py \
		src/gather/giants_games_test.py \
		src/gather/logs.py \
		src/gather/options.py \
		src/gather/options_test.py \
		src/gather/refresh_rate.py \
		src/gather/weather.py \
		src/gather/weather_test.py \
		\
		src/render/__init__.py \
		src/render/__main__.py \
		src/render/api_display.py \
		src/render/api_display_test.py \
		src/render/api_setup.py \
		src/render/api_setup_test.py \
		src/render/AtkinsonHyperlegibleMono-Regular.otf \
		src/render/bitmap.py \
		src/render/constants.py \
		src/render/date_and_time.py \
		src/render/forecast.py \
		src/render/giants_games_today.py \
		src/render/intro_screen.py \
		src/render/logs.py \
		src/render/next_muni.py \
		src/render/options.py \
		src/render/options_test.py \
		src/render/screen.py \
		\
		src/serve/__init__.py \
		src/serve/__main__.py \
		src/serve/handler.py \
		src/serve/options.py \
		src/serve/options_test.py \
		src/serve/server.py

python_files := $(filter %.py, $(src_files))

python_sources := $(filter-out %_test.py, $(python_files))

python_tests := $(filter %_test.py, $(python_files))

resource_files := $(filter-out %.py, $(src_files))


uv.lock : pyproject.toml .python-version
	uv sync
	touch $@


$(TMP)/deploy.stamp : \
		$(TMP)/trmnl_srv_deploy.env \
		$(TMP)/trmnl_srv.tar.gz \
		| $$(dir $$@)
	rsync --archive \
		$(TMP)/trmnl_srv_deploy.env \
		$(TMP)/trmnl_srv.tar.gz \
		don@10.0.0.100:~
	ssh don@10.0.0.100 '/bin/bash -l -s' < scripts/deploy.sh
	touch $@


$(TMP)/docker-build-deploy.stamp : \
		$(container_files) \
		$(src_files) \
		| $$(dir $$@)
	docker build \
		--build-arg BASE_URL="$(DEPLOY_BASE_URL)" \
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
		--build-arg BASE_URL="$(DEV_BASE_URL)" \
		--file container/Dockerfile \
		--platform linux/amd64 \
		--tag $(dev_image) \
		--quiet \
		.
	touch $@


$(TMP)/docker-run.stamp : \
		$(TMP)/docker-build-dev.stamp \
		$(TMP)/trmnl_srv_dev.env \
		| $$(dir $$@)
	-docker stop $(container)
	-docker rm $(container)
	docker run \
		--detach \
		--env-file $(TMP)/trmnl_srv_dev.env \
		--init \
		--name $(container) \
		--platform linux/amd64 \
		--publish $(PORT):80 \
		$(dev_image)
	touch $@


$(TMP)/pytest.stamp : \
		$(python_files) \
		$(TMP)/trmnl_srv_dev.env \
		$(TMP)/uv-sync.stamp \
		| $$(dir $$@)
	uv run -m pytest --quiet --quiet
	touch $@


$(TMP)/trmnl_srv_deploy.env : secrets/five11-org-key.txt | $$(dir $$@)
	touch $@
	chmod 600 $@
	printf "BASE_URL=%s\n" "$(DEPLOY_BASE_URL)" >> $@
	printf "FIVE11_ORG_KEY=%s\n" "$(FIVE11_ORG_KEY)" >> $@


$(TMP)/trmnl_srv_dev.env : secrets/five11-org-key.txt | $$(dir $$@)
	touch $@
	chmod 600 $@
	printf "BASE_URL=%s\n" "$(DEV_BASE_URL)" >> $@
	printf "FIVE11_ORG_KEY=%s\n" "$(FIVE11_ORG_KEY)" >> $@


$(TMP)/trmnl_srv.tar.gz : \
		$(TMP)/docker-build-deploy.stamp \
		| $$(dir $$@)
	docker image save $(deploy_image) | gzip > $@


$(TMP)/uv-sync.stamp : uv.lock | $$(dir $$@)
	uv sync --frozen
	touch $@


$(TMP)/ :
	mkdir -p $@
