GO_LANG="go"
PYTHON="python"
JAVA="java"
JAVASCRIPT="javascript"

.PHONY: dojo-go
dojo-go:
	bash generate.sh ${GO_LANG}

.PHONY: dojo-python
dojo-python:
	bash generate.sh ${PYTHON}

.PHONY: dojo-java
dojo-java:
	bash generate.sh ${JAVA}

.PHONY: dojo-js
dojo-js:
	bash generate.sh ${JAVASCRIPT}
