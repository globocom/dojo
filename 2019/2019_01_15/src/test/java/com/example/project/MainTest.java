/*
 * Copyright 2015-2018 the original author or authors.
 *
 * All rights reserved. This program and the accompanying materials are
 * made available under the terms of the Eclipse Public License v2.0 which
 * accompanies this distribution and is available at
 *
 * http://www.eclipse.org/legal/epl-v20 */

package com.example.project;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Tag;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

@Tag("fast")
class MainTest {

    @Test
    @DisplayName("My 1st JUnit 5 test! 😎")
    void testMain() {
        Main main = new Main();
        List<Integer> list  = new ArrayList<>();
        list.add(10);
        assertEquals(main.main(10), list);
    }

    @Test
    @DisplayName("My 1st JUnit 5 test! 😎")
    void testMain2() {
        Main main = new Main();
        List<Integer> list  = new ArrayList<>();
        list.add(20);
        assertEquals(main.main(20), list);
    }

    @Test
    @DisplayName("My 1st JUnit 5 test! 😎")
    void testMain3() {
        Main main = new Main();
        List<Integer> list  = new ArrayList<>();
        list.add(20);
        list.add(10);
        assertEquals(main.main(30), list);
    }

    @Test
    @DisplayName("My 1st JUnit 5 test! 😎")
    void testMain4() {
        Main main = new Main();
        List<Integer> list  = new ArrayList<>();
        list.add(20);
        list.add(20);
        assertEquals(main.main(40), list);
    }
    @Test
    @DisplayName("My 1st JUnit 5 test! 😎")
    void testMain5() {
        Main main = new Main();
        assertEquals(main.quantidadeNotas(10,10), 1);
    }
    @Test
    @DisplayName("My 1st JUnit 5 test! 😎")
    void testMain6() {
        Main main = new Main();
        assertEquals(main.quantidadeNotas(10,20), 0);
    }
    @Test
    @DisplayName("My 7st JUnit 5 test! 😎")
    void testMain7() {
        Main main = new Main();
        assertEquals(main.quantidadeNotas(30,20), 1);
    }
    @Test
    @DisplayName("My 8st JUnit 5 test! 😎")
    void testMain8() {
        Main main = new Main();
        assertEquals(main.quantidadeNotas(30,10), 3);
    }
    @Test
    @DisplayName("My 9st JUnit 5 test! 😎")
    void testNotasDisponiveis() {
        Main main = new Main();
        List<Integer> list  = new ArrayList<>();
//        list.add(100);
//        list.add(50);
        list.add(20);
        list.add(10);
        assertEquals(main.getNotas(), list);
    }


    @Test
    @DisplayName("My 9st JUnit 5 test! 😎")
    void testAddNotas() {
        Main main = new Main();
        List<Integer> list1  = new ArrayList<>();
        List<Integer> list  = new ArrayList<>();
        list1.add(10);
        list1.add(10);
        list1.add(10);
        assertEquals(main.addNotas(list, 10, 3), list1);
    }

}
