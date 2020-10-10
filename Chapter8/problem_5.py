def recursive_multiply(first_num, second_num):
    if second_num == 0 or any(num < 0  for num in (first_num,second_num)):
        return 0

    return first_num + recursive_multiply(first_num, second_num-1)

print(recursive_multiply(-1, -2))