import crypt

def crack(pas):
    salt=pas[:2]
    wordlist=open('usr/share/wordlist.txt','r')
    for word in wordlist:
        word=word.strip('\n')
        enc=crypt.crypt(word,salt)
        if(enc==pas):
            print('Password was cracked:'+word)
        else:
            print('Password cannot be cracked')



def main():
    f=open('password.txt','r')
    for i in f.readlines():
        i=i.strip('\n')
        if ':' in i:
            user=i.split(':')[0]
            pas=i.split(':')[1].strip(' ')
            crack(pas)

if __name__=='__main__':
    main()