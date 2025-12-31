all: build

../../target/subdomains/vat:
	mkdir -pv ../../target/subdomains/vat

build: ../../target/subdomains/vat
	rsync -avu --delete /home/t/src/vat/p/ ../../target/subdomains/vat/
	cp -af s ../../target/subdomains/vat
