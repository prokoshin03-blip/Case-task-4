def max_dragon_power(n: int) -> int:
    if n <= 4:
        return n
    count_of_3 = n // 3
    remainder = n % 3
    if remainder == 0:
        return 3 ** count_of_3
    elif remainder == 1:
        return (3 ** (count_of_3 - 1)) * 4
    else:
        return (3 ** count_of_3) * 2

if __name__ == "__main__":
    n = int(input("Введите N (0 < N < 100): "))
    print(f"Максимальная сила стаи: {max_dragon_power(n)}")
