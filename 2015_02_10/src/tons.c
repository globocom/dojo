#include <string.h>
#include <stdlib.h>

static int nota_pra_frequencia(char *nota) {
    char *notas_s[] = {
        "C", "C#", "D", "D#", "E",
        "F", "F#", "G", "G#", "A",
        "A#", "B"
    };
    char *notas_b[] = {
        "C", "Db", "D", "Eb", "E",
        "F", "Gb", "G", "Ab", "A",
        "Bb", "B"
    };

    int total = sizeof(notas_s)/sizeof(char*);

    for (int i = 0; i < total; i++) {
        if (!strcmp(nota, notas_s[i]) || !strcmp(nota, notas_b[i])) {
            return i;
        }
    }

    return -1;
}

int pertence_escala(char *escala, char *nota) {
    int escala_frequencia = nota_pra_frequencia(escala);
    int nota_frequencia = nota_pra_frequencia(nota);

    if (escala_frequencia < 0 || nota_frequencia < 0) {
        return -1;
    }

    int intervalo = nota_frequencia - escala_frequencia;
    if (intervalo < 0) {
        intervalo += 12;
    }

    switch (intervalo) {
        case 0:
        case 2:
        case 4:
        case 5:
        case 7:
        case 9:
        case 11:
            return 1;
    }

    return 0;
}
