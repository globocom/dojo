#include <ctype.h>
#include <string.h>

int baby_speak(char *vocabulary[], char *word)
{
    int i = 0;
    int start = 0;

    while (isspace(word[0])) {
        word++;
    }

    if (strlen(word) == 0) {
        return 1;
    }

    char *syl;
    int can_speak = 0;
    while ((syl = vocabulary[i++])) {
        int n = strlen(syl);
        if (strnstr(word, syl, n)) {
            can_speak = can_speak || baby_speak(vocabulary, word+n);
        }
    }
    return can_speak;
}
