AC_PREREQ([2.59])
AC_INIT([stack], [1.0], [dojo@globo.com])

AC_CONFIG_AUX_DIR([build-aux])

AM_INIT_AUTOMAKE([-Wall -Werror foreign])
AM_PROG_AR
AC_PROG_CC
AC_PROG_LIBTOOL
AC_CONFIG_SRCDIR([src/stack.c])

PKG_CHECK_MODULES([CHECK], [check >= 0.9.6])

AC_HEADER_STDC
AC_CHECK_HEADERS([stdlib.h])

AC_FUNC_MALLOC

AC_CONFIG_HEADERS([config.h])

AC_CONFIG_FILES([Makefile
                 src/Makefile
                 tests/Makefile])
AC_CONFIG_MACRO_DIRS([m4])

AC_OUTPUT
