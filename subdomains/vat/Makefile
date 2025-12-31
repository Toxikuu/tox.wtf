all: build

../../target/tmp/vat:
	mkdir -pv ../../target/subdomains/vat

build: ../../target/tmp/vat
	rsync -avu --delete /home/t/src/vat/p/ ../../target/subdomains/vat/
	cp -af s ../../target/subdomains/vat
