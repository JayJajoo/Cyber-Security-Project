import math
import random as rm
import elg_key as eleKey
import elg_ency as elgEncy

def main():
    
    eleKey.main()  
    p=17
    q=11
    n = p*q
    e=7
    print("n = ",n,"e = ",e)
    fd = open("rsa_key.txt","w")
    fd.write(str(n)+'\n'+str(e))
    fd.close()
    elgEncy.main()

    d = 23
    print("private key is : ",d)

if __name__ == '__main__':
    main()
