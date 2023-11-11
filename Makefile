install:
	bash setup.sh install

generate-project:
	bash setup.sh generate-project

lint:
	bash setup.sh lint

lint-ci:
	bash setup.sh lint:ci

test:
	bash setup.sh test

clean:
	bash setup.sh clean
