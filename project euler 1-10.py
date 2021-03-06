"""
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get
3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def remove_dup(dirty): #there is something like this is numpy
    clean = []
    for i in dirty:
        if i not in clean:
            clean.append(i)
    return clean

def mult_sum(below, nat):
    mult = []
    for i in xrange(1,below):
        for n in nat:
            if i % n == 0:
                mult.append(i)
    mult = remove_dup(mult)
    return sum(mult)
        
# print mult_sum(1000,[3,5])




"""
Even Fibonacci numbers
Problem 2

Each new term in the Fibonacci sequence is generated by adding the previous two 
terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed 
four million, find the sum of the even-valued terms.
"""



def even_fib_sum(limit):
    sum_total = 0
    last_term = 1
    current_term = 2
    while current_term <= limit:
        if current_term % 2 == 0:
            sum_total += current_term
        next_term = current_term + last_term
        last_term = current_term
        current_term = next_term
    return sum_total
            
        

# print even_fib_sum(4000000)



"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# This runs very slow

def is_prime(a_list):
    prime_list = []
    for i in a_list:
        is_prime = True
        j = 2
        while is_prime == True and j <=int(i**.5 + 1):
            if i % j == 0 and i != j:
                is_prime = False
            j+=1
        if is_prime == True:
            prime_list.append(i)
    return prime_list
        
def factors(number):
    factors = []
    for i in xrange(2,number+1):
        if number % i == 0:
            factors.append(i)
    return factors
        
    
def largest_prime_factor(limit):
    prime_limit = int(limit**.5 + 1)
    factor_list = factors(prime_limit)
    primes = is_prime(factor_list)
    return primes[len(primes)-1]
    
 
print largest_prime_factor(13195)










