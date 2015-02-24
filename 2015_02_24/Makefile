.PHONY: tests clean

tests: tests/check
	@./tests/check

clean:
	@rm -f tests/*.o src/*.o tests/check

src/map.o: src/map.c src/map.h
	gcc -c -g $< -o $@

tests/check_map.o: tests/check_map.c
	gcc -c -g $< -o $@

tests/check: src/map.o tests/check_map.o
	gcc $^ -lcheck -o tests/check
