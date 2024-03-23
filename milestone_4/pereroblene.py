def find_sum(target: int, li: list[int]):
    seen_numbers = set()
    for num in li:
        complement = target - num
        if complement in seen_numbers:
            return (complement, num)
        seen_numbers.add(num)

print(find_sum(5, [1, 2, 3, 4, 5]))