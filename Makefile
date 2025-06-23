-include config.mk

.PHONY: all clean build serve dev local-serve

all: build

clean:
	rm -rf target

build:
	python3 py/render.py

serve: build
	caddy run --config Caddyfile

local-serve: build
	python3 -m http.server -d target

dev: clean build serve
