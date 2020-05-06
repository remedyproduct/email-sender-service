default: build

build:
	docker build --tag email-sender-service:latest .
