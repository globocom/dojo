#include <glib.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include "erdos.h"

GList* erdos(struct publication* publications, int size) {
    GList *people = NULL;

    for (int position=0; position<size; position++) {
        for (GList *p=g_list_first(publications[position].people); p!=NULL; p=g_list_next(p)) {
            struct person *data = p->data;
            if (strcmp(data->name, "Erdos") != 0) {
                data->weight = 1;
                people = g_list_append(people, p->data);
            }
        }
    }

    return people;
}
