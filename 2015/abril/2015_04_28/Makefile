.PHONY: tests clean

tests: tests/check
	@./tests/check

clean:
	@rm -f tests/*.o src/*.o tests/check

src/erdos.o: src/erdos.c src/erdos.h
	gcc -c -I/usr/local/include/glib-2.0 -I/usr/local/lib/glib-2.0/include -g $< -o $@

tests/check_erdos.o: tests/check_erdos.c
	gcc -c -I/usr/local/include/glib-2.0 -I/usr/local/lib/glib-2.0/include -g $< -o $@

tests/check: src/erdos.o tests/check_erdos.o
	gcc $^ -lcheck -lglib-2.0 -o tests/check
