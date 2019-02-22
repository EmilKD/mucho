########################i thought this was a cool way to generate primes###########
primes=[2]
c=2
while True:
    c += 1
    prime_flag = True
    for num in primes:
        if c%num==0:
            prime_flag=False
    if not prime_flag:
        continue
    else:
        primes.append(c)
        print(c)
######################################10000 is just a test num :) ###################
    if c>=10000:
        print(primes)
        break
