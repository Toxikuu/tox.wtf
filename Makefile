-include config.mk

.PHONY: all clean build serve dev local-serve subdomains

SUBDOMAINS = lfs
.PHONY: subdomains/$(SUBDOMAINS)

all: build subdomains

clean:
	rm -rf target/site target/subdomains

purge:
	rm -rf target

build: Cargo.toml
	cargo run
	find target/site -type f -iname '*.html' -print0 | xargs -0 tidy -m -config tidyconf
	cp -af static -T target/site/s

subdomains: subdomains/$(SUBDOMAINS)

subdomains/$(SUBDOMAINS):
	@for subdomain in $(SUBDOMAINS); do \
		cd subdomains/$$subdomain && $(MAKE); \
	done

serve: build
	caddy run --config Caddyfile

local-serve: build
	caddy run --config Caddyfile.local

dev: clean build local-serve
