def insertion_sort(sequence_arg):
    sequence = sequence_arg[:]

    for current_pos in range(1, len(sequence)):
        current = sequence[current_pos]
        insertion_pos = current_pos - 1

        while insertion_pos >= 0 and sequence[insertion_pos] > current:
            sequence[insertion_pos + 1] = sequence[insertion_pos]
            insertion_pos -= 1

        sequence[insertion_pos + 1] = current

    return sequence


if __name__ == '__main__':

    import random

    test_seq = [random.randint(0, 99) for _ in range(10)]
    ref_seq = sorted(test_seq)
    seq = insertion_sort(test_seq)

    print('test_seq:\n{}\nref_seq:\n{}\nseq:\n{}'
          ''.format(test_seq, ref_seq, seq))

    assert ref_seq == seq