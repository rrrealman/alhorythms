
from string import ascii_lowercase as letters
from argparse import ArgumentParser


class StringsGenerator:

    LAST_LETTER = len(letters) - 1

    def __init__(self, positions=None):
        self.positions = list(positions) or [0, ]

    def __iter__(self):
        return self

    def next(self):
        res = self.to_string()

        if self.positions[-1] < self.LAST_LETTER:
            self.positions[-1] += 1
        else:
            self.positions[-1] = 0
            self.increment_positions()

        return res

    def to_string(self):
        chars = [letters[position] for position in self.positions]
        return ''.join(chars)

    def increment_positions(self):
        current = len(self.positions) - 2
        while current >= 0:
            if self.positions[current] < self.LAST_LETTER:
                self.positions[current] += 1
                break
            else:
                self.positions[current] = 0
            current -= 1
        else:
            self.positions.append(0)

    @classmethod
    def from_chars(cls, chars):
        positions = [letters.index(char) for char in chars]
        return cls(positions)


def generate_strings(begin, end):
    strings_generator = iter(StringsGenerator.from_chars(begin))
    word = next(strings_generator)
    while len(word) < len(end) or word <= end:
        yield word
        word = next(strings_generator)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--from', dest='begin')
    parser.add_argument('--to', dest='end')
    args = parser.parse_args()
    for word in generate_strings(args.begin, args.end):
        print(word)


