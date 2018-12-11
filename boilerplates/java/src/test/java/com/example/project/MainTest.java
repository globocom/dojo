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

import static org.junit.jupiter.api.Assertions.assertTrue;

@Tag("fast")
class MainTest {

    @Test
    @DisplayName("My 1st JUnit 5 test! 😎")
    void testMain() {
        Main main = new Main();
        assertTrue(main.main(), "Test Assert true");
    }

}
