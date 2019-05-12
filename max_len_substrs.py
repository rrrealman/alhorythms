import random
from string import ascii_uppercase as letters


def max_len_substrs(string):
    chars = {}
    counter = 1
    prev_char = string[0]

    for char in string[1:]:
        if char == prev_char:
            counter += 1
        else:
            if chars.get(prev_char, 0) < counter:
                chars[prev_char] = counter
            counter = 1
        prev_char = char
    if chars.get(prev_char, 0) < counter:
        chars[prev_char] = counter
    return chars


def generate_test_string():
    char = random.choice(letters)
    generated_str = ''
    max_seqs = {}

    for sequence_counter in range(0, random.randint(1, 10)):
        multiplier = random.randint(1, 10)

        if char not in max_seqs or max_seqs[char] < multiplier:
            max_seqs[char] = multiplier
        generated_str += char * multiplier

        char = random.choice(letters.replace(char, ''))

    return generated_str, max_seqs


if __name__ == '__main__':

    test_str, ref_chars = generate_test_string()
    chars = max_len_substrs(test_str)

    print('test_str:\n{}\nref_chars:\n{}\nchars:\n{}\n'
          ''.format(test_str, ref_chars, chars))

    assert ref_chars == chars
