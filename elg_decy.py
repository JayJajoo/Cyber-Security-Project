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
    key=26483633026457924888110156389934014358938232972367
    p1=int(fp.readline())
    en_msg1=list(map(int,fp.readline().split(',')))[:-1]
    p2=int(fp.readline())
    en_msg2=list(map(int,fp.readline().split(',')))
    dr_msg1 = decrypt(en_msg1, p1, key, q)
    dr_msg2 = decrypt(en_msg2, p2, key, q)
    dmsg1 = ''.join(dr_msg1)
    dmsg2 = ''.join(dr_msg2)
    print("Decrypted n :",dmsg1);
    print("Decrypted e:",dmsg2);
    fp.close()
    return [dmsg1,dmsg2]
 
if __name__ == '__main__':
    main()