

alphabet = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z'
              ]
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type the message:\n").lower()
steps = int(input("Type the shift number:\n"))


def ceaser(start_text, shift_amount, cipher_direction):
    # clever solution
    # for this to work alphabets should be duplicated twice eg ['a'.....'z','a'...'z']

    '''
    end_text = ""
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"the {cipher_direction}d text is {end_text}")
    
    
    
    '''





    cipher_text = ''
    plain_text = ''
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'encode':
            new_position = position + shift_amount
            if new_position > 26:
                new_pos = new_position - 26
                letter = alphabet[new_pos] 
            elif new_position < 26:
                letter = alphabet[new_position]           
            cipher_text += letter
    
        elif cipher_direction == 'decode':
            new_position = position - shift_amount
            plain_text += alphabet[new_position]
    if cipher_direction == 'encode':
      print(f"The encoded text is {cipher_text}")
    elif cipher_direction == 'decode':
      print(f"The decorded text is {plain_text}")
    else:
        print("Choose either encode or decode !!!")

            

ceaser(text,steps,direction)




# def encrypt(encode, shift):
#   cipher_text = ""
#   for letter in encode:
#       # get the current position of the letter
#       position = alphabet.index(letter)
#       # add the position to the shift value
#       new_position = position + shift
#       if new_position > 26:
#         new_pos = new_position -26
#         letter = alphabet[new_pos]
#       else:
#           letter = alphabet[new_position]
#       cipher_text += letter
#   print(f"The decrypted text is {cipher_text}")

# def decrypt(decode, shift):
#     decoded_text = ""
#     for letter in decode:        
#         position = alphabet.index(letter)
#         new_position = position - shift
#         letter = alphabet[new_position]
#         decoded_text += letter
#     print(f"The decrypted text is {decoded_text}")

# if direction == 'encode':
#   encrypt(text, steps)

# elif direction == 'decode':
#     decrypt(text, steps)
# else:
#     print("choose encode or decode")
