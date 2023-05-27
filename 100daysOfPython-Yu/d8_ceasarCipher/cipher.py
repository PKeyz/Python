alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def caesar(text, shift, direction):
    text_list = list(text)
    cipher_array = []
    cipher_text = ""

    if direction == "encode":
  
        for x in text_list:
            index = alphabet.index(x)

            if (index + shift) >= len(alphabet):
                new_shift = (index + shift) - len(alphabet)
                y = alphabet[new_shift]
                cipher_array += y
            else:
                y = alphabet[index + shift]
                cipher_array += y
        
        cipher_text = "".join(cipher_array)
        print(f"The encoded text is {cipher_text}")
    elif direction == "decode":
        
        for x in text_list:
            index = alphabet.index(x)
            y = alphabet[index - shift]
            cipher_array += y

        cipher_text = "".join(cipher_array)
        print(f"The encoded text is {cipher_text}")
    else:
        print("INPUT WRONG, TRY AGAIN!")


caesar(text,shift,direction)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.