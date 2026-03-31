def Factorial(n):
    """Task 2.1: Calculate factorial using recursion"""
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * Factorial(n - 1)


def Fibonacci(n):
    """Task 2.1: Calculate nth Fibonacci number using recursion"""
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)


def FibonacciIterative(n):
    """Task 2.1: Calculate nth Fibonacci number iteratively"""
    if n < 0:
        return None
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def IsPalindrome(text):
    """Task 2.2: Check if string is palindrome using recursion"""
    text = text.lower()
    
    def check_palindrome(start, end):
        if start >= end:
            return True
        
        if text[start] != text[end]:
            return False
        
        return check_palindrome(start + 1, end - 1)
    
    if len(text) <= 1:
        return True
    
    return check_palindrome(0, len(text) - 1)


def ReverseString(text):
    """Task 2.2: Reverse string using recursion"""
    if len(text) <= 1:
        return text
    
    return text[-1] + ReverseString(text[:-1])


def CountVowels(text):
    """Task 2.2: Count vowels in string using recursion"""
    vowels = "aeiouAEIOU"
    
    def count(start, vowel_count):
        if start >= len(text):
            return vowel_count
        
        if text[start] in vowels:
            vowel_count += 1
        
        return count(start + 1, vowel_count)
    
    return count(0, 0)


def BinarySearchRecursive(data_list, target, left=None, right=None, comparisons=0):
    """Task 2.3: Binary search using recursion"""
    if left is None:
        left = 0
    if right is None:
        right = len(data_list) - 1
    
    if left > right:
        return -1, comparisons
    
    mid = (left + right) // 2
    comparisons += 1
    
    print(f"  Searching [{left}:{right}], mid={mid}, value={data_list[mid]}")
    
    if data_list[mid] == target:
        return mid, comparisons
    elif data_list[mid] < target:
        return BinarySearchRecursive(data_list, target, mid + 1, right, comparisons)
    else:
        return BinarySearchRecursive(data_list, target, left, mid - 1, comparisons)


def SumArray(arr):
    """Task 2.3: Sum array elements using recursion"""
    if len(arr) == 0:
        return 0
    
    return arr[0] + SumArray(arr[1:])


def FindMin(arr):
    """Task 2.3: Find minimum using recursion"""
    if len(arr) == 0:
        return None
    
    if len(arr) == 1:
        return arr[0]
    
    min_rest = FindMin(arr[1:])
    
    return arr[0] if arr[0] < min_rest else min_rest


def CountOccurrences(arr, target):
    """Task 2.3: Count occurrences using recursion"""
    if len(arr) == 0:
        return 0
    
    count = 1 if arr[0] == target else 0
    return count + CountOccurrences(arr[1:], target)


def Power(base, exponent):
    """Task 2.4: Calculate power using recursion"""
    if exponent < 0:
        return None
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    return base * Power(base, exponent - 1)


def PowerEfficient(base, exponent):
    """Task 2.4: Efficient power calculation using recursion"""
    if exponent < 0:
        return None
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    
    if exponent % 2 == 0:
        half_power = PowerEfficient(base, exponent // 2)
        return half_power * half_power
    else:
        return base * PowerEfficient(base, exponent - 1)


def DecimalToBinary(n):
    """Task 2.4: Convert decimal to binary using recursion"""
    if n < 0:
        return None
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    
    return DecimalToBinary(n // 2) + str(n % 2)


def GCD(a, b):
    """Task 2.4: Calculate GCD using recursion (Euclidean algorithm)"""
    if b == 0:
        return a
    return GCD(b, a % b)


def TowersOfHanoi(n, source='A', target='C', auxiliary='B'):
    """Task 2.4: Solve Towers of Hanoi"""
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return 1
    
    moves = 0
    moves += TowersOfHanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    moves += 1
    moves += TowersOfHanoi(n - 1, auxiliary, target, source)
    
    return moves


def DemonstrateRecursion():
    """Demonstrate various recursive functions"""
    print("=" * 80)
    print("Task 2.1: Factorial and Fibonacci")
    print("=" * 80)
    
    for n in [0, 1, 5, 10]:
        print(f"Factorial({n}) = {Factorial(n)}")
    
    print()
    for n in [0, 1, 5, 10]:
        print(f"Fibonacci({n}) = {Fibonacci(n)} (recursive)")
        print(f"Fibonacci({n}) = {FibonacciIterative(n)} (iterative)")
    
    print("\n" + "=" * 80)
    print("Task 2.2: String Operations")
    print("=" * 80)
    
    test_strings = ["radar", "hello", "level", "world", "madam"]
    for s in test_strings:
        print(f"'{s}' is palindrome: {IsPalindrome(s)}")
    
    print()
    for s in ["hello", "python", "recursion"]:
        print(f"'{s}' reversed: {ReverseString(s)}")
    
    print("\n" + "=" * 80)
    print("Task 2.3: Array Operations")
    print("=" * 80)
    
    arr = [1, 2, 3, 4, 5]
    print(f"Array: {arr}")
    print(f"Sum: {SumArray(arr)}")
    print(f"Min: {FindMin(arr)}")
    
    arr_with_dups = [1, 2, 3, 2, 4, 2, 5]
    print(f"\nArray with duplicates: {arr_with_dups}")
    print(f"Count of 2: {CountOccurrences(arr_with_dups, 2)}")
    
    print("\n" + "=" * 80)
    print("Task 2.3: Binary Search")
    print("=" * 80)
    
    sorted_list = [11, 12, 22, 25, 34, 64, 90]
    print(f"Sorted list: {sorted_list}")
    print(f"\nSearching for 25:")
    idx, comps = BinarySearchRecursive(sorted_list, 25)
    print(f"Found at index: {idx}, Comparisons: {comps}")
    
    print(f"\nSearching for 50:")
    idx, comps = BinarySearchRecursive(sorted_list, 50)
    print(f"Found at index: {idx}, Comparisons: {comps}")
    
    print("\n" + "=" * 80)
    print("Task 2.4: Advanced Recursion")
    print("=" * 80)
    
    print(f"2^10 = {Power(2, 10)}")
    print(f"3^5 = {Power(3, 5)}")
    print(f"2^10 (efficient) = {PowerEfficient(2, 10)}")
    print(f"3^5 (efficient) = {PowerEfficient(3, 5)}")
    
    print(f"\nDecimal to Binary:")
    for n in [10, 15, 42, 255]:
        print(f"  {n} = {DecimalToBinary(n)}")
    
    print(f"\nGCD:")
    print(f"  GCD(48, 18) = {GCD(48, 18)}")
    print(f"  GCD(100, 25) = {GCD(100, 25)}")
    
    print(f"\nTowers of Hanoi (3 disks):")
    moves = TowersOfHanoi(3)
    print(f"Total moves: {moves}")


if __name__ == "__main__":
    DemonstrateRecursion()
