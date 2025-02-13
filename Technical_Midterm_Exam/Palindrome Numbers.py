with open('numbers.txt', 'r') as file:
    lines = file.readlines()
def is_palindrome(num):
    return str(num) == str(num)[::-1]

def check_palindrome_sum(line):
    numbers = [int(n) for n in line.split(',') if n.strip().isdigit()]
    total_sum = sum(numbers)
    if is_palindrome(total_sum):
        return f"{line} (sum {total_sum}) - Palindrome"
    else:
        return f"{line} (sum {total_sum}) - Not a palindrome"
for i, line in enumerate(lines):
    line = line.strip()
    result = check_palindrome_sum(line)
    print(f"Line {i+1}: {result}")