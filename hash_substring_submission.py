# python3
import random
import sys

def rabin_karp(pattern, text):
    textLength = len(text)
    patternLength = len(pattern)
    
    primeNumber = compute_prime_number(textLength * patternLength)
    randomInteger = random.randint(1, primeNumber -1)
    results = []
    polyHash = compute_polyhash(pattern, primeNumber, randomInteger)
    hashes = precompute_hashes(text, patternLength, primeNumber, randomInteger)
    
    for i in range(textLength - patternLength + 1):
        if polyHash == hashes[i]:
            if text[i: i+patternLength] == pattern:
                results.append(i)
    
    return results

def precompute_hashes(text, patternLength, primeNumber, selectedInteger):
    textLength = len(text)
    hashes = [0 for i in range(textLength - patternLength + 1)]
    lastSubstring = text[(textLength - patternLength):]
    hashes[textLength - patternLength] = compute_polyhash(lastSubstring, primeNumber, selectedInteger)
    y = 1
    for _ in range(patternLength):
        y = (y * selectedInteger) % primeNumber
    for i in range(textLength - patternLength - 1, -1, -1):
        hashes[i] = (selectedInteger * hashes[i+1] + ord(text[i]) - y * ord(text[i + patternLength])) % primeNumber
    return hashes

def compute_polyhash(substring, primeNumber, selectedInteger):
    h = 0
    for i in range(len(substring)-1, -1, -1):
        h = (h * selectedInteger + ord(substring[i])) % primeNumber
    return h

def compute_prime_number(lowerBound):
    for number in range(lowerBound + 1, sys.maxsize):
        if is_prime(number):
            return number

def is_prime(n):
    if n == 1:
        return False          
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i+=1
    return True

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))


if __name__ == '__main__':
    print_occurrences(rabin_karp(*read_input()))

