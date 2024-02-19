.PHONY: tests clean

tests: tests/check
	@./tests/check

clean:
	@rm -f tests/*.o src/*.o tests/check

src/miojo.o: src/miojo.c src/miojo.h
	gcc -c -g $< -o $@

tests/check_miojo.o: tests/check_miojo.c
	gcc -c -g $< -o $@

tests/check: src/miojo.o tests/check_miojo.o
	gcc $^ -lcheck -o tests/check
