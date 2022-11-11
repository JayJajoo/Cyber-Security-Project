import os
import codecs
import elg_decy as eleDecy
def decryption(C,d,n):
    msg=""
    for i in C:
        msg+=str(chr((int(i)**d)%n))
    return msg
def main():
    FileName = 'Message.txt'
    fd = codecs.open(FileName,'r','utf-8')
    SampleData = list(map(int,fd.read().split(' ')))
    fd.close()
    print("Fetched Encrypted data is ",SampleData)
    
    lst=eleDecy.main()
    n=int(lst[0])

    d = int(input("Enter Private Key : "))
    
    P = decryption(SampleData,d,n)
    print("Decrypted message is ",P)

    os.remove("elgamal_keys.txt")
    os.remove("Message.txt")

if __name__ == '__main__':
    main()