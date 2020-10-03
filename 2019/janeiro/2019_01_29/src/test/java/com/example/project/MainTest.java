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

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

@Tag("fast")
class MainTest {

    @Test
    @DisplayName("Test double slash")
    void doubleSlash() {
        Main main = new Main();
        String str = "// Olá";
        assertFalse(main.isCountLine(str));
    }

    @Test
    @DisplayName("Test no comments")
    void noComments() {
        Main main = new Main();
        String str = "System.out.println(vida)";
        assertTrue(main.isCountLine(str));
    }

    @Test
    @DisplayName("Test no comments")
    void commentsStartWithSpace() {
        Main main = new Main();
        String str = " //";
        assertFalse(main.isCountLine(str));
    }

    @Test
    @DisplayName("Test no comments")
    void startWithSpace() {
        Main main = new Main();
        String str = " print('Vamos acreditar!') //";
        assertTrue(main.isCountLine(str));
    }

    @Test
    @DisplayName("Test no comments")
    void blankLine() {
        Main main = new Main();
        String str = "";
        assertTrue(main.isBlankLine(str));
    }

    @Test
    @DisplayName("Test no comments")
    void notABlankLine() {
        Main main = new Main();
        String str = "foo";
        assertFalse(main.isBlankLine(str));
    }

    @Test
    @DisplayName("Test no comments")
    void CountingTheLines() {
        Main main = new Main();
        String str = "foo";
        assertTrue(main.isCountLine(str));
    }

    @Test
    @DisplayName("Test block comments")
    void checkBlock() {
        Main main = new Main();
        String str = "/* teste */";
        assertFalse(main.isCountLine(str));
    }

    @Test
    @DisplayName("Test block comments")
    void checkBlockWithValidCode() {
        Main main = new Main();
        String str = "/* comentario */ print Hello /* teste */ ";
        assertTrue(main.checkBlock(str));
    }

}
