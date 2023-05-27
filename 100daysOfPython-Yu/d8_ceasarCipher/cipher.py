alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
 #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

def encrypt(text,shift):
  text_list = list(text)
  cipher_array = []
  cipher_text = ""
  
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
  

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
def decrypt(text, shift):
  text_list = list(text)
  cipher_array = []
  cipher_text = ""
  
  for x in text_list:
    index = alphabet.index(x)
    y = alphabet[index - shift]
    
    cipher_array += y
      
  cipher_text = "".join(cipher_array)
  print(f"The encoded text is {cipher_text}")

#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction == "encode":
  encrypt(text, shift)
else:
  decrypt(text, shift)