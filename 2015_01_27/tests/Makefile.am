## Process this file with automake to produce Makefile.in

TESTS = check_stack
check_PROGRAMS = check_stack
check_money_SOURCES = check_stack.c $(top_builddir)/src/stack.h
check_money_CFLAGS = @CHECK_CFLAGS@
check_money_LDADD = $(top_builddir)/src/libstack.la @CHECK_LIBS@
