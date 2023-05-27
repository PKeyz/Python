def caesar(text, shift, direction):
    if direction == "encode":
        text_list = list(text)
        cipher_array = []
        cipher_text = ""
  
        for x in text_list:
            index = alphabet.index(x)

            if (index + shift) >= len(alphabet):
                new_shift = (index + shift) - len(alphabet)
                y = alphabet[new_shift]
            else:
                y = alphabet[index + shift]
    
        cipher_array += y
    elif direction == "decode":
        text_list = list(text)
        cipher_array = []
        cipher_text = ""
        
        for x in text_list:
            index = alphabet.index(x)
            y = alphabet[index - shift]
            
            cipher_array += y
    else:
        print("INPUT WRONG, TRY AGAIN!")