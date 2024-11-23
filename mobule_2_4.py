numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
primts = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    is_prime = True

    for n in range(2, int(i**0.5)+1):
        if i % n == 0:
            is_prime = False
            break
    if is_prime:
        primts.append(i)
    else:
        not_primes.append(i)
print (primts, not_primes )
