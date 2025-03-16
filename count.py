def count_valid(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4
    a, b = 2, 4
    for i in range(3, n+1):
        a, b = b, a + b
    return b

def main():
    t = int(input())
    outputs = []
    for _ in range(t):
        n = int(input())
        outputs.append(str(count_valid(n)))
    print("\n".join(outputs))

if __name__ == '__main__':
    main()
