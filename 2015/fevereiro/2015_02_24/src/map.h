#ifndef MAP_H
#define MAP_H

struct map {
  int lop; // Status of the last operation
  int size;
  int next_key_index;
  int* keys;
  int* values;
};

struct map* new_map(int);
void set_value(struct map*, int, int);
int get_value(struct map*, int);
void destroy_map(struct map*);

#endif
