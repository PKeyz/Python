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