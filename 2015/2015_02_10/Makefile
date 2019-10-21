.PHONY: tests clean

tests: tests/check
	@./tests/check

clean:
	@rm -f tests/*.o src/*.o tests/check

src/tons.o: src/tons.c src/tons.h
	gcc -c -g $< -o $@

tests/check_tons.o: tests/check_tons.c
	gcc -c -g $< -o $@

tests/check: src/tons.o tests/check_tons.o
	gcc $^ -lcheck -o tests/check
