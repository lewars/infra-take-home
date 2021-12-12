TAG_NAME := "0.0.1"
.PHONY: build-local build
.PHONY: test

dep-install:
	pip install -r reverse/requirements-test.txt
build-local:
	cloud-build-local --dryrun=false --config=cloudbuild.yaml --substitutions=TAG_NAME=${TAG_NAME} .
build:
	gcloud builds submit --config cloudbuild.yaml --substitutions=TAG_NAME=${TAG_NAME}
test:
	pytest --verbose --color=yes reverse
