def make_dp(length):
    def recursive(position, previous_digit, consecutive_count, memo={}):
        if position == length:
            return 1
        key = (position, previous_digit, consecutive_count)
        if key in memo:
            return memo[key]
        total = 0
        for digit in ['0', '1']:
            if previous_digit is not None and digit == previous_digit and consecutive_count == 2:
                continue
            new_consecutive_count = consecutive_count + 1 if (previous_digit is not None and digit == previous_digit) else 1
            total += recursive(position + 1, digit, new_consecutive_count, memo)
        memo[key] = total
        return total
    return recursive

def rank_of(number, dp):
    length = len(number)
    rank = 0
    previous_digit = None
    consecutive_count = 0
    for i in range(length):
        for digit in ['0', '1']:
            if digit < number[i]:
                if previous_digit is None:
                    new_consecutive_count = 1
                else:
                    if digit == previous_digit and consecutive_count == 2:
                        continue
                    new_consecutive_count = consecutive_count + 1 if (previous_digit is not None and digit == previous_digit) else 1
                rank += dp(i+1, digit, new_consecutive_count)
        if previous_digit is None:
            previous_digit = number[i]
            consecutive_count = 1
        else:
            if number[i] == previous_digit:
                consecutive_count += 1
            else:
                previous_digit = number[i]
                consecutive_count = 1
    return rank

def main():
    test_cases = int(input())
    results = []
    for _ in range(test_cases):
        number = input().strip()
        length = len(number)
        dp_function = make_dp(length)
        rank = rank_of(number, dp_function)
        results.append(str(rank))
    print("\n".join(results))

if __name__ == '__main__':
    main()
