-include config.mk

.PHONY: all clean build serve dev

all: build

dev: clean build serve

clean:
	rm -rf target

build:
	python3 py/render.py

serve: build
	python3 -m http.server -d target
