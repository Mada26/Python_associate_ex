print("insert your text here to encrypt")
text=input()

print("instert your desired shifting value")
val=int(input())

# Caesar cipher.
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
    
    else:
        char1 = char.upper()
        #do encrypting
        code = ord(char1) + val
        #final alphabet
        if code > ord('Z')  :
            code = ord('A')+(val-1)
        elif code > ord('z'):
            code = ord('a')+(val-1)
        #if its number leave number
        #make lower if input lower
        if char1 != char:
            code= chr(code).lower()
        #if not number convert back in string
        if not(isinstance(code,str)):
            code= chr(code)
        cipher += code

print(cipher)
