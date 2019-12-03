import numpy as np
import sys

def levenshtein(string1, string2):
    '''returns Levenshtein's distance of string1 and string2.\
        source: \
        stackabuse.com/levenshtein-distance-and-text-similarity-in-python/'''
    len_1 = len(string1) + 1
    len_2 = len(string2) + 1
    mat = np.zeros((len_1, len_2))
    for x in range(len_1):
        mat[x, 0] = x
    for y in range(len_2):
        mat[0, y] = y
    for x in range(1, len_1):
        for y in range(1, len_2):
            if string1[x-1] == string2[y-1]:
                mat[x, y] = min(
                  mat[x-1, y],
                  mat[x-1, y-1],
                  mat[x, y-1]
                    )
            else:
                mat[x, y] = min(
                    mat[x-1, y] + 1,
                    mat[x-1, y-1] + 1,
                    mat[x, y-1] + 1
                )
    return (mat[len_1 - 1, len_2 - 1])

#nie napisałem jeszcze, sorry