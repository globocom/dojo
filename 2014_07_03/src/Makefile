.PHONY: test setup

setup:
	cabal install --only-dependencies --enable-tests
	cabal configure --enable-tests

test:
	cabal build && cabal test
	cat dist/test/parentalTesting-0.1-main.log
