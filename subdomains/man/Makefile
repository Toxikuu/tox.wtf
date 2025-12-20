all: build

build:
	find man -mindepth 2 -type f -name '*.[1-8]*' -exec install -vDm644 -t ../../target/subdomains/man/ {} +
	./deref.sh
	cp -af s ../../target/subdomains/man
