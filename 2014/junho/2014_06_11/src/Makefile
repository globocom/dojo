.PHONY: test setup

setup:
	cabal install --only-dependencies --enable-tests
	cabal configure --enable-tests

test:
	cabal build && cabal test
