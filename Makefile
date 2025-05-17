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

.SECONDEXPANSION :


.PHONY : all
all : check


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


alpine_files := \
		alpine/etc/cron.d/trmnl \
		alpine/etc/init.d/trmnl_srv

python_files := \
		src/gather/__init__.py \
		src/gather/__main__.py \
		src/gather/weather.py \
		src/gather/weather_test.py \
		src/render/__init__.py \
		src/render/__main__.py \
		src/serve/__init__.py \
		src/serve/__main__.py

python_source := \
		$(filter-out %_test.py, $(python_files)) \
		$(shell_files)

python_tests := $(filter %_test.py, $(python_files))

shell_files := \
		src/serve_trmnl \
		src/update_trmnl


uv.lock : pyproject.toml .python-version
	uv sync
	touch $@


$(TMP)/deploy.stamp.txt : \
		$(TMP)/pytest.stamp.txt \
		$(alpine_files) \
		$(shell_files)
	rsync \
		$(RSYNC_FLAGS) \
		src/ \
		donmcc@10.1.1.1:~/trmnl_srv/
	rsync \
		$(RSYNC_FLAGS) \
		alpine/ \
		donmcc@10.1.1.1:~/trmnl_setup/
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
