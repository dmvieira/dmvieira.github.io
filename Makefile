.PHONY: install run build

ROOT=$(shell pwd)
SRCFOLDER=$(ROOT)/src

install:
	@pip install -r requirements.txt
	@git submodule update --init

build:
	@cd $(SRCFOLDER) && pelican

run: build
	@python -m SimpleHTTPServer