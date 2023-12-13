#ifndef CIRCULAR_BUFFER_H
#define CIRCULAR_BUFFER_H

typedef struct circular_buf_t {
    int head;
    int size;
    float* data;
} circular_buf_t;

inline void circular_buf_init_from_array(circular_buf_t* buf, float* array, unsigned int size) {
    buf->data = array;
    buf->head = 0;
    buf->size = size;
}

inline void circular_buf_add(circular_buf_t* buf, float x) {
    buf->data[buf->head] = x;
    buf->head = (buf->head + 1) % buf->size;
}

inline void dump_to_array(circular_buf_t* buf, float* array) {
    for (int i = 0; i < buf->size; i++) {
        array[i] = buf->data[(buf->head + i) % buf->size];
    }
}

#endif // CIRCULAR_BUFFER_H