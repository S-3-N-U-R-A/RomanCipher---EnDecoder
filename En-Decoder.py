alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
secret_message = input("Type your message here:\n").lower()
key = int(input("Type the key:\n"))

def encode(message, keynumber, operation):
    output_text = ""
    for letter in message:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + keynumber
            shifted_position = shifted_position % len(alphabet)
            output_text = output_text + alphabet[shifted_position]
        else:
            output_text += letter
    print("Here is the encoded text : ", output_text)

if encode_or_decode == "encode":
    encode(message=secret_message, keynumber=key, operation=encode_or_decode)

