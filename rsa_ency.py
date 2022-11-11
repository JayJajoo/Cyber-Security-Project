import elg_decy as elgDecy

def encryption(P, e, n):
    encData=[]
    msg=str(P)
    i=0
    while(i<len(msg)):
        s=msg[i]
        if(s!='0'):
            j=i+1
            if(j>=len(msg)):
                encData.append(str((int(s)**e)%n))
                break
            while(int(s+msg[j])<n):
                s+=msg[j]
                j+=1
                if(j==len(msg)):
                    break
            i=j
            encData.append(str((int(s)**e)%n))
        else:
            encData.append('0')
            i+=1
    return encData

def main():
    lst=elgDecy.main()
    n=int(lst[0])
    e=int(lst[1])
    P = input("Enter Messa6ge : ")
    data=""
    for i in P:
        print(str(ord(i)),end=' ')
        data+=str(ord(i))
    data1 = encryption(data, e, n)
    
    encData=' '.join(data1)
    
    with open('Message.txt', 'w', encoding='utf-8') as f:
        f.write(str(encData))
    f.close()

if __name__ == '__main__':
    main()
