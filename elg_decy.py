import random
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
 
# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a
 
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
 
    return x % c
 
def decrypt(en_msg, p, key, q):
 
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))
         
    return dr_msg

def main():
    fp=open("elgamal_keys.txt","r")
    q=int(fp.readline())
    g=int(fp.readline())
    p=int(fp.readline())
    key=int(input("Enter your private key :- "))
    en_msg=list(map(int,fp.readline().split(',')))
    dr_msg = decrypt(en_msg, p, key, q)
    dmsg = ''.join(dr_msg)
    print("Decrypted Message :", dmsg);

    fp.close()

    fp=open("elgamal_keys.txt","a")
 
if __name__ == '__main__':
    main()