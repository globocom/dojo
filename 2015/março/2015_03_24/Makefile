.PHONY: tests clean

tests: tests/check
	@./tests/check

clean:
	@rm -f tests/*.o src/*.o tests/check

src/largest_product_grid.o: src/largest_product_grid.c src/largest_product_grid.h
	gcc -c -g $< -o $@

tests/check_largest_product_grid.o: tests/check_largest_product_grid.c
	gcc -c -g $< -o $@

tests/check: src/largest_product_grid.o tests/check_largest_product_grid.o
	gcc $^ -lcheck -o tests/check
