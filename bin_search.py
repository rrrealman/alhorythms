def bin_search(target, sequence):
    beg = 0
    end = len(sequence) - 1

    while True:
        mid = (beg + end) // 2

        if sequence[mid] > target:
            end = mid - 1
        elif sequence[mid] < target:
            beg = mid + 1
        else:
            return mid

        if beg == mid or end == mid:
            break


if __name__ == '__main__':

    import random

    forbidden_values = (-10, 110)

    for test_counter in range(12):
        test_seq = sorted(random.randint(0, 99) for counter in range(10))
        print('=============================')

        if test_counter < 10:
            test_target = test_seq[test_counter]
        elif test_counter < 11:
            test_target = forbidden_values[0]
        elif test_counter < 12:
            test_target = forbidden_values[1]

        index = bin_search(test_target, test_seq)

        print('test_seq:\n{}\ntest_target: {}\nindex: {}'
              ''.format(test_seq, test_target, index))

        if index is None:
            assert test_target in forbidden_values
            continue

        assert test_target == test_seq[index]
