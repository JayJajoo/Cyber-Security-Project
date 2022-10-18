import os
import codecs
def decryption(C,d,n):
    P = []
    for i in C:
        P.append(chr((i**d)%n))
    return P
def main():
    FileName = 'Message.txt'
    fd = codecs.open(FileName,'r','utf-8')
    SampleData = fd.read()
    fd.close()
    print("Sample data is ",*SampleData)
    FileName = 'rsa_key.txt'
    fd = open(FileName)
    n = int(fd.readline())
    fd.close()
    C = []
    for i in SampleData:
        C.append(ord(i))
    print(C)
    d = int(input("Enter Private Key : "))
    P = decryption(C,d,n)
    print("msg : ",''.join(P))

if __name__ == '__main__':
    main()