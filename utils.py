from itertools import permutations
import re

class Utilities(object):

    def get_permuations(word, pattern):
        if word == None:
            return ['shite', 'onions']
        print(word, "!")
        print(pattern, "!")
        word_count = len(pattern)
        pattern = compile_pattern(pattern)
        print(pattern, "!")
        letters = []
        [letters.append(i) for i in word]
        perms = []
        perms_beta = permutations(letters, word_count)
        for p in perms_beta:
            w = "".join(p)
            vowels = vowel_checker(w)
            if re.match(pattern, w) and vowels:
                perms.append(w)

        perms = set(perms)
        perms = list(perms)

        perms.sort()

        return perms


def compile_pattern(pattern_string):
    pattern = []
    for p in pattern_string:
        if p == "*":
            pattern.append("[a-z]")
        else:
            pattern.append(p)

    pattern = "".join(pattern)

    return re.compile(pattern)


def vowel_checker(perm):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    for vowel in vowels:
        if vowel in perm:
            return True
    return False