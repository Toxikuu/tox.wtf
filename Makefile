-include config.mk

.PHONY: all clean build serve dev local-serve

all: build

clean:
	rm -rf target/site

purge:
	rm -rf target

build:
	cargo run
	find target -type f -iname '*.html' -print0 | xargs -0 tidy -m -config tidyconf
	cp -af static -T target/site/s

serve: build
	caddy run --config Caddyfile

local-serve: build
	caddy run --config Caddyfile.local

dev: clean build local-serve
