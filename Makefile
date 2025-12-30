-include config.mk

.PHONY: all clean build serve dev local-serve subdomains

all: build subdomains tidy

clean:
	rm -rf target/site target/subdomains target/tmp

purge:
	rm -rf target

build: Cargo.toml
	cargo run
	cp -af s target/site

tidy: build subdomains
	find target/{site,subdomains} -type f -iname '*.html' -print0 | xargs -0 tidy -m -config tidyconf

subdomains: subdomain-man subdomain-vat

subdomain-lfs:
	$(MAKE) -C subdomains/lfs

subdomain-man:
	$(MAKE) -C subdomains/man

subdomain-vat:
	$(MAKE) -C subdomains/vat

serve: build
	caddy run --config Caddyfile

local-serve: build
	caddy run --config Caddyfile.local

dev: clean build local-serve
