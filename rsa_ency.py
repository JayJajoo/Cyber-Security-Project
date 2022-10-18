def encryption(P, e, n):
    C = []
    new = []
    for i in P:
        new.append(ord(i))
    print(new)
    for i in new:
        C.append((int(int(i) ** e)) % n)
    print(C)
    return C

def main():
    FileName = 'rsa_key.txt'
    fd = open(FileName)
    n = int(fd.readline())
    e = int(fd.readline())
    fd.close()
    P = input("Enter Message : ")
    data1 = encryption(P, e, n)
    EncryptedData = []
    for i in data1:
        EncryptedData.append(chr(i))
    string=""
    string=string.join(EncryptedData)
    with open('Message.txt', 'w', encoding='utf-8') as f:
        f.write(string)
    f.close()

if __name__ == '__main__':
    main()
