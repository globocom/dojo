/*
 * Copyright 2015-2018 the original author or authors.
 *
 * All rights reserved. This program and the accompanying materials are
 * made available under the terms of the Eclipse Public License v2.0 which
 * accompanies this distribution and is available at
 *
 * http://www.eclipse.org/legal/epl-v20 */

package com.example.project;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertTrue;

@Tag("fast")
class MainTest {

    @Test
    @DisplayName("My 1st JUnit 5 test! 😎")
    void testDouble() {
        Main main = new Main();

        Assertions.assertEquals(main.doubleNumber(1), 2, "Double 1");
        Assertions.assertEquals(main.doubleNumber(2), 4, "Double 2");
        Assertions.assertEquals(main.doubleNumber(3), 6, "Double 3");
        Assertions.assertEquals(main.doubleNumber(6), 3, "Double 6");
        Assertions.assertEquals(main.doubleNumber(5), 1, "Double 5");
    }

    @Test
    void stringSplit() {
        Main main = new Main();
        Assertions.assertEquals(main.removeSpacesFromString("123"), "123", "foo");
        Assertions.assertEquals(main.removeSpacesFromString("123 456"), "123456", "foo com espaco");
    }

    @Test
    void testIterate() {
        Main main = new Main();
        ArrayList result = new ArrayList();
        result.add(9);
        result.add(6);
        result.add(5);
        result.add(8);
        Assertions.assertEquals(result, main.iterateNumber("4539"), "foo");
    }
}
