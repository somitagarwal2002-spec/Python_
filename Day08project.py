# Encryption & Decryption Program --------------------------------------

# def encrypt(mess, shift):
#     cipher_text =""
#     for i in mess:
#         shifted = alpha.index(i) + shift
#         shifted %= len(alpha)
#         cipher_text += alpha[shifted]
#     print("The encrypted text is: ",cipher_text)

# def decrypt(cipher_text, shift):
#     original = ""
#     for i in cipher_text:
#         shifted = alpha.index(i) - shift
#         shifted %= len(alpha)
#         original += alpha[shifted]
#     print("The decrypted text is: ",original)

def ceasar(mess, shift, encode_or_decode):
    output_text =""
    if encode_or_decode == "decode":
                shift *= -1
    for i in mess:
        if i not in alpha:
            output_text += i
        else: 
            shifted = alpha.index(i) + shift
            shifted %= len(alpha)
            output_text += alpha[shifted]
    print("The",encode_or_decode,"text is: ",output_text)

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

cont = True
while cont is True:
    code = input("Type 'encode' to encrypt, 'decode' to decrypt: \n").lower()
    mess = input("Type your message \n").lower()
    shift = int(input("Type the shift number \n"))

    ceasar(mess, shift, code)
    restart = input("Type 'yes' if you want to continue or 'no' to stop").lower()
    if restart == "no":
        cont = False
        print("Goodbye")

# encrypt(mess, shift)
# decrypt(mess, shift)



