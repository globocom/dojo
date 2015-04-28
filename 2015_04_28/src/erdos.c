#include <glib.h>
#include <stdlib.h>
#include <math.h>
#include "erdos.h"

struct person p;
GList* erdos(struct publication* publications, int size) {
    GList *people = NULL;

    for(int position=0; position<size; position++) {
        for(GList *p=g_list_first(publications[position].people); p != NULL; p = g_slist_next()) {
            if (strcmp(p->data->name, "Erdos") != 0) {
                p->data->weight = 1;
                people = g_list_append(people, p->data);
            }
        }
    }

    return people;
}
