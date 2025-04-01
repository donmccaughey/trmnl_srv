TMP ?= $(abspath tmp)


.SECONDEXPANSION :


.PHONY : all
all : check


.PHONY : check
check : $(TMP)/pytest.stamp.txt


.PHONY : clean
clean :
	rm -rf $(TMP)


.PHONY : clobber
clobber : clean
	rm -rf .venv


python_files := \
		src/gather/__init__.py \
		src/gather/__main__.py \
		src/gather/weather.py \
		src/gather/weather_test.py \
		src/render/__init__.py \
		src/render/__main__.py \
		src/serve/__init__.py \
		src/serve/__main__.py \


source_files := $(filter-out %_test.py, $(python_files))

test_files := $(filter %_test.py, $(python_files))


uv.lock : pyproject.toml .python-version
	uv sync
	touch $@


$(TMP)/pytest.stamp.txt : \
		$(source_files) \
		$(test_files) \
		$(TMP)/uv-sync.stamp.txt \
		| $$(dir $$@)
	uv run -m pytest --quiet --quiet
	date > $@


$(TMP)/uv-sync.stamp.txt : uv.lock | $$(dir $$@)
	uv sync --frozen
	date > $@


$(TMP)/ :
	mkdir -p $@
