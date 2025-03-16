def make_dp(length):
    cache = {}
    def recursive(position, previous_digit, consecutive_count):
        key = (position, previous_digit, consecutive_count)
        if key in cache:
            return cache[key]
        if position == length:
            return 1
        total = 0
        for digit in ['0', '1']:
            if previous_digit is not None and digit == previous_digit and consecutive_count == 2:
                continue
            new_consecutive_count = consecutive_count + 1 if (previous_digit is not None and digit == previous_digit) else 1
            total += recursive(position + 1, digit, new_consecutive_count)
        cache[key] = total
        return total
    return recursive

def rank_of(binary_string, dp):
    length = len(binary_string)
    rank = 0
    previous_digit = None
    consecutive_count = 0
    for i in range(length):
        for digit in ['0', '1']:
            if digit < binary_string[i]:
                if previous_digit is None:
                    new_consecutive_count = 1
                else:
                    if digit == previous_digit and consecutive_count == 2:
                        continue
                    new_consecutive_count = consecutive_count + 1 if (previous_digit is not None and digit == previous_digit) else 1
                rank += dp(i+1, digit, new_consecutive_count)
        if previous_digit is None:
            previous_digit = binary_string[i]
            consecutive_count = 1
        else:
            if binary_string[i] == previous_digit:
                consecutive_count += 1
            else:
                previous_digit = binary_string[i]
                consecutive_count = 1
    return rank

def unrank(rank, length, dp):
    result = ""
    previous_digit = None
    consecutive_count = 0
    for i in range(length):
        for digit in ['0', '1']:
            if previous_digit is not None and digit == previous_digit and consecutive_count == 2:
                continue
            new_consecutive_count = consecutive_count + 1 if (previous_digit is not None and digit == previous_digit) else 1
            count = dp(i+1, digit, new_consecutive_count)
            if rank < count:
                result += digit
                previous_digit = digit
                consecutive_count = new_consecutive_count
                break
            else:
                rank -= count
    return result

def main():
    test_cases = int(input())
    outputs = []
    for _ in range(test_cases):
        binary_string = input().strip()
        length = len(binary_string)
        dp_func = make_dp(length)
        total = dp_func(0, None, 0)
        rank = rank_of(binary_string, dp_func)
        if rank == total - 1:
            outputs.append("None")
        else:
            successor = unrank(rank + 1, length, dp_func)
            outputs.append(successor)
    print("\n".join(outputs))

if __name__ == '__main__':
    main()
