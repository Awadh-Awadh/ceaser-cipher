

alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z'
              ]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
steps = int(input("Type the shift number"))

def encrypt(encode, shift):
   cipher_text = ""
   for letter in encode:
      # get the current position of the letter
      position = alphabet.index(letter)
      # add the position to the shift value
      new_position = position + shift
      if new_position > 26:
         new_pos = new_position -26
         letter = alphabet[new_pos]
      else:
          letter = alphabet[new_position]
      cipher_text += letter
   print(f"The decrypted text is {cipher_text}")

      

encrypt(direction, steps)