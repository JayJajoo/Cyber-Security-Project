import random
import os
from math import pow
 
a = random.randint(2, 10)
 
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
 
# Generating large random numbers
def gen_key(q):
 
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
 
    return key

def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c

def encrypt(msg, q, h, g):
 
    en_msg = []
 
    k = gen_key(q)# Private key for sender
    s = power(h, k, q)
    p = power(g, k, q)
     
    for i in range(0, len(msg)):
        en_msg.append(msg[i])

    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
 
    return en_msg, p

def main():
 
    fp=open("elgamal_keys.txt","r")

    q = int(fp.readline())
    g = int(fp.readline())

    fp.close()

    key = 26483633026457924888110156389934014358938232972367

    h = power(g, key, q)

    
    fp=open("rsa_key.txt","r")
    msg1=fp.readline() #n
    msg2=fp.readline() #e
    fp.close()
    os.remove("rsa_key.txt")

    en_msg1,p1=encrypt(msg1, q, h, g)
    en_msg2,p2=encrypt(msg2, q, h, g)

    fp=open("elgamal_keys.txt","a")

    fp.write("{0}\n{1}\n{2}\n{3}\n".format(str(p1),str(en_msg1)[1:-1],str(p2),str(en_msg2)[1:-1]))

    fp.close()

if __name__ == '__main__':
    main()