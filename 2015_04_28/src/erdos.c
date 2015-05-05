#include <glib.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "erdos.h"


GList* erdos(struct publication* publications, int size) {
    GHashTable *graph = g_hash_table_new(g_str_hash, g_str_equal);
    GList *people = NULL;

    for (int position=0; position<size; position++) {
        add_publication_to_graph(&publications[position], graph);
    }

    return people;
}

struct graph_value {
    int weight;
    GList *people;
};

static void add_publication_to_graph(const struct publication *publication, GHashTable *graph) {
    for (GList *iter1=g_list_first(publication.people); iter1!=NULL; iter1=g_list_next(iter1)) {
        struct person *p1 = iter1->data;

        for (GList *iter2=g_list_first(publication.people); iter2!=NULL; iter2=g_list_next(iter2)) {
            struct person *p2 = iter2->data;
            if (strcmp(p1->name, p2->name) == 0) {
                continue;
            }

            struct graph_value *value = g_hash_table_lookup(graph, p1->name);
            if (!value) {
                GList *names = g_list_append(names, data2->name);
                value = malloc(sizeof(struct graph_value));
                value->people = names;
                g_hash_table_insert(graph, data->name, value);
            } else {
                value->people = g_list_append(value->people, data2->name);
            }
        }
    }
}
