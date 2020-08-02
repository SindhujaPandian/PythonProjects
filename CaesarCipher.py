VALID_STRING = 'abcdefghijklmnopqrstuvwxyz'
def encrypt(text,key):
    encrypt_string = 'abcddefghijklmnopqrstuvwxyz' * 2
    output = ' '
    for char in text:
        if char in VALID_STRING:
            index = encrypt_string.index(str(char))
            output+= encrypt_string[index+key]
        else:
            output+= char
    return output

def decrypt(text,day):
    decrypt_string = 'zyxwvutsrqponmlkjihgfedcba' * 2
    output = ''
    for char in text:
        if char in VALID_STRING:
            index = decrypt_string.index(str(char))
            output += decrypt_string[index+key]
        else:
            output += char
    return output

print("                                                               ---------------------------------------------------------------")
print("                                                              |                                    CEASER CIPHER                          |")
print("                                                               ---------------------------------------------------------------")
while True:
    print("\n1. Encryption")
    print("2.Decryption")
    print("3.Both")

    choice = int(input("Choose you choice of input :  "))

    if choice==1:
        input_val = input("Enter the text to encrypt    ")
        key = int(input("Enter the key between 1 to 25   "))
        print("The encrypted value is ")
        print(encrypt(input_val,key))

    elif choice == 2:
            input_val = input("Enter the text to encrypt    ")
            key = int(input("Enter the key between 1 to 25   "))
            print( "The decrypted text is  ")
            print(decrypt(input_val, key))

    elif choice == 3:
        input_val = input("Enter the text to encrypt    ")
        key = int(input("Enter the key between 1 to 25   "))
        print("The encrypted value is ")
        print(encrypt(input_val,key))
        print( "The decrypted text is  ")
        print(decrypt(input_val, key))
    else:
        print("Enter the valid choice")

    print("\nDo you want to try again : \nY - Yes\nN - No\n")
    ans= input("Enter your choice : ")
    if ans[0].lower() == 'y':
        continue
    else:
        break














    
