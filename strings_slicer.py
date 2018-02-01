
from string import ascii_lowercase as letters



class StringsGenerator:

    LAST_LETTER = len(letters) - 1

    def __init__(self):
        self.positions = [0, ]

    def __iter__(self):
        return self

    def next(self):
        res = self.to_string()

        if self.positions[-1] < self.LAST_LETTER:
            self.positions[-1] += 1
        else:
            self.positions[-1] = 0
            self.reset_positions()

        return res

    def to_string(self):
        res = [letters[position] for position in self.positions]
        return ''.join(res)

    def reset_positions(self, ):
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


if __name__ == '__main__':
    import time
    gen = StringsGenerator()
    for word in iter(gen):
        print(word)
        time.sleep(0.5)
