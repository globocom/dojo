GO_LANG="go"
PYTHON="python"
JAVA="java"
JAVASCRIPT="javascript"
RUST="rust"
PHP="php"
RUBY="ruby"
R="r"

.PHONY: dojo-go
dojo-go:
	@bash ./boilerplates/generate.sh ${GO_LANG}

.PHONY: dojo-python
dojo-python:
	@bash ./boilerplates/generate.sh ${PYTHON}

.PHONY: dojo-java
dojo-java:
	@bash ./boilerplates/generate.sh ${JAVA}

.PHONY: dojo-js
dojo-js:
	@bash ./boilerplates/generate.sh ${JAVASCRIPT}

.PHONY: dojo-rust
dojo-rust:
	@bash ./boilerplates/generate.sh ${RUST}

.PHONY: dojo-php
dojo-php:
	@bash ./boilerplates/generate.sh ${PHP}

.PHONY: dojo-ruby
dojo-ruby:
	@bash ./boilerplates/generate.sh ${RUBY}

.PHONY: dojo-r
dojo-r:
	@bash ./boilerplates/generate.sh ${R}
