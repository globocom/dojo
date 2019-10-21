#ifndef ERDOS_H
#define ERDOS_H

#include <glib.h>

struct person {
    char* name;
    int weight;
};

struct publication {
    GList* people;
};


GList* erdos(struct publication* publications, int size);

#endif
