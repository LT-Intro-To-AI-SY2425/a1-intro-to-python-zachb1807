# Complete your individualized AI problems here

def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num
    


#Palindrome Checker
def is_palindrome(s: str) -> bool:
    for i in range(0,len(s)//2):
        if s[i] != s[-1-i]:
            return False
    return True


#Create a function that returns the first n numbers of the Fibonacci sequence.
def fibonacci(n: int) -> list:
    numbers:list
    if n == 0:
        return 0
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    if n > 2:
        numbers = [1,1,2]
        for i in range(3,n):
            numbers.append(numbers[i-2] + numbers[i-1])
        return numbers
            

def count_vowels(string: str) -> int:
    count = 0
    vowels = "aeiou"
    for i in string:
        if i in vowels: count += 1
    return count

#Tests

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"



assert is_palindrome("racecar") == True, "racecar test"
assert is_palindrome("hello") == False, "hello test"
assert is_palindrome("a") == True, "a test"
assert is_palindrome("ab") == False, "ab test"
assert is_palindrome("aba") == True, "aba test"
assert is_palindrome("abba") == True, "abba test"


print(fibonacci(10))

print(count_vowels("hello world"))