.PHONY: tests clean

tests: tests/check
	@./tests/check

clean:
	@rm -f tests/*.o src/*.o tests/check

src/baby.o: src/baby.c src/baby.h
	gcc -c -g $< -o $@

tests/check_baby.o: tests/check_baby.c
	gcc -c -g $< -o $@

tests/check: src/baby.o tests/check_baby.o
	gcc $^ -lcheck -o tests/check
