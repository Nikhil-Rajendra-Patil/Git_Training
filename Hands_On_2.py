def countPrimeNumbers(numbers):
    prime_count = 0
    for n in numbers:
        if n == 1:
            continue
        for divisor in range(2,n):
            if n%divisor == 0:
                break
        else :
            prime_count += 1
    return prime_count

if __name__ == '__main__':
    numbers = []
    count = int(input())
    for i in range(count):
        numbers.append(int(input()))
    
    print(countPrimeNumbers(numbers))