DEPLOY_BASE_URL := http://10.0.0.100:4000
DEV_BASE_URL ?= http://127.0.0.1:4000
FIVE11_ORG_KEY ?= $(shell cat secrets/five11-org-key.txt)
PORT ?= 4000
TMP ?= $(abspath tmp)

container := trmnl_srv
container_files := \
	.dockerignore \
	$(shell find container -type f -not -name '.DS_Store')
deploy_image := trmnl_srv
dev_image := trmnl_srv_dev
src_files := $(shell find src \
	-type f \
	-not -path '*/__pycache__/*' \
	-not -name '.DS_Store' \
)


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


## file targets


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
		$(src_files) \
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
