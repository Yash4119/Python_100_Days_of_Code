# Performing encryption and decryption of strings for enhancing security using Python

'''

** Encryption **
1. If length of string is atleast 3 then remove first letter and append it at the end
   and append any random 3 charachter at the end
2. if length of string is less than 3 then simply reverse the string

** Decryption **
1. if length of string is less than 3 then simply reverse the string
2. if length of string is more than 3 then remove 3 characters from start and end and 
   then remove last character and append at front.
'''

def reverse(str):
    s=0
    e=len(str)-1
    while(s<e):
        ch = str[s]
        str[s] = str[e]
        str[e] = ch
        s+=1
        e-=1
    # print(str)
    


def encode(stri):
    stri = list(stri)
    print(len(stri))
    if(len(stri)<=3):
        reverse(stri)
        ans = ''.join(stri)
    else:
        ch = stri[0]
        stri[0] = stri[len(stri)-1]
        stri[len(stri)-1] = ch
        ans = ''.join(stri)
        ans = "abc" + ans + "abc"
    return ans

str1 = "abc"
str2 = "yash"

en_str1 = encode(str1)
en_str2 = encode(str2)

print(str1," => ",en_str1)
print(str2," => ",en_str2)

# Now we will decode the string

def decode(str):
    str = list(str)
    if(len(str) <= 3):
        reverse(str)
        str = ''.join(str)
        return str
    
    str = str[3:-3]
    ch = str[0]
    str[0] = str[len(str)-1]
    str[len(str)-1] = ch
    str = ''.join(str)
    return str


print(en_str1," => ",decode(en_str1))
print(en_str2," => ",decode(en_str2))
