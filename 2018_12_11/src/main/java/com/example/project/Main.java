/*
 * Copyright 2015-2018 the original author or authors.
 *
 * All rights reserved. This program and the accompanying materials are
 * made available under the terms of the Eclipse Public License v2.0 which
 * accompanies this distribution and is available at
 *
 * http://www.eclipse.org/legal/epl-v20.html
 */

package com.example.project;

import java.util.ArrayList;

class Main {


    int doubleNumber(int number) {
        int doubleValue = number * 2;
        return doubleValue >= 10 ? doubleValue - 9 : doubleValue;
    }

    String removeSpacesFromString(String number) {
        return number.replace(" ", "");
    }

    ArrayList iterateNumber(String number) {

        ArrayList numbers = new ArrayList();
        for (int i = number.length() - 1; i >= 0; i--) {
            if (i % 2 != 0)
                numbers.add(this.doubleNumber(Integer.parseInt(String.valueOf(number.charAt(i)))));
            else
                numbers.add(Integer.parseInt(String.valueOf(number.charAt(i))));
        }
        return numbers;
    }

}
