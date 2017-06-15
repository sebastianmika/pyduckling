#include "pyduckling_stub.h"

void py_init(int argc, char *argv[]) {
    hs_init(&argc, &argv);
}

void py_exit() {
    hs_exit();
}

char* parse(char* text, char* lang, long time) {
    return hs_parse(text, lang, time);
}
