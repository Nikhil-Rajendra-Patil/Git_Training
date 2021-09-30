import math
import os
import random
import re
import sys

def isPrime(n):
    if n == 1:
        return False
    for divisor in range(2,n):
        if n%divisor == 0:
            return False
    return True

def countPrimeNumbers(numbers):
    prime_count = 0
    for i in numbers:
        if isPrime(i):
            prime_count += 1
    return prime_count

if __name__ == '__main__':
    numbers = []
    count = int(input())
    for i in range(count):
        numbers.append(int(input()))
    
    print(countPrimeNumbers(numbers))