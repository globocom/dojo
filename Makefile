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
	@. ./boilerplates/generate.sh ${GO_LANG}

.PHONY: dojo-python
dojo-python:
	@. ./boilerplates/generate.sh ${PYTHON}

.PHONY: dojo-java
dojo-java:
	@. ./boilerplates/generate.sh ${JAVA}

.PHONY: dojo-js
dojo-js:
	@. ./boilerplates/generate.sh ${JAVASCRIPT}

.PHONY: dojo-rust
dojo-rust:
	@. ./boilerplates/generate.sh ${RUST}

.PHONY: dojo-php
dojo-php:
	@. ./boilerplates/generate.sh ${PHP}

.PHONY: dojo-ruby
dojo-ruby:
	@. ./boilerplates/generate.sh ${RUBY}

.PHONY: dojo-r
dojo-r:
	@. ./boilerplates/generate.sh ${R}
