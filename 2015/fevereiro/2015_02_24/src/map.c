#include <string.h>
#include <stdlib.h>
#include "map.h"

struct map* new_map(int size)
{
  struct map *m = malloc(sizeof (struct map));
  m->size = size;
  m->next_key_index = 0;
  m->keys = malloc(sizeof(int) * size);
  m->values = malloc(sizeof(int) * size);
  m->lop = 0;
  return m;
}

void destroy_map(struct map* m)
{
  free(m->keys);
  free(m->values);
  free(m);
}

void set_value(struct map* m, int key, int value)
{
  int i;
  for (i = 0; i < m->next_key_index; i++) {
    if (m->keys[i] == key) {
      m->values[i] = value;
      m->lop = 0;
      return;
    }
  }

  if (m->next_key_index >= m->size) {
    m->lop = 1;
    return;
  }

  m->keys[m->next_key_index] = key;
  m->values[m->next_key_index] = value;
  m->next_key_index++;
  m->lop = 0;
  return;
}

int get_value(struct map* m, int key)
{
  int i;
  for (i = 0; i < m->next_key_index; i++) {
    if (m->keys[i] == key) {
      m->lop = 0;
      return m->values[i];
    }
  }
  m->lop = 1;
  return 0;
}
