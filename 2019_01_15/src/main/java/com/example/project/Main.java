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
import java.util.List;

class Main {

    List<Integer> main(int i) {
        List<Integer> list = new ArrayList<>();
//        if (i >= 20) {
//            list.add(20);
//            if (i - 20 > 0) {
//                list.add(i - 20);
//            }
//        } else {
//            list.add(i);
//        }

        Integer valor = i;
        List<Integer> notas = getNotas();
        for (Integer nota : notas) {
            int quantidade = quantidadeNotas(valor, nota);
            addNotas(list, nota, quantidade);
            valor = valor - (nota * quantidade);
        }
        return list;
    }

    int quantidadeNotas(int valor, int nota) {
        return valor / nota;
    }

    List<Integer> getNotas() {
        List<Integer> list = new ArrayList<>();
//		list.add(100);
//		list.add(50);
        list.add(20);
        list.add(10);
        return list;
    }


    List<Integer> addNotas(List<Integer> list, int nota, int vezes) {
        for (int i = 0; i < vezes; i++) {
            list.add(nota);
        }
        return list;
    }
}
