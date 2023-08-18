import click
import random
import string

def generate_key():
    alphas = string.ascii_lowercase
    
    alphas = string.ascii_lowercase
    my_alphas = list(alphas[:])  # Making a copy of the string as a list
    random.shuffle(my_alphas)
    substitution = my_alphas

    key = {alphas[i]: substitution[i] for i in range(len(alphas))}
    return key


def encode(key, message):
    encoded = ""
    message = message.lower().strip()
    for letter in message:
        if letter.isalpha():
            encoded += key[letter]
        else:
            encoded += letter
    return encoded


def decode(key, message):
    decoded = ""
    message = message.lower().strip()
    inverse_key = {v: k for k, v in key.items()}
    for letter in message:
        if letter.isalpha():
            decoded += inverse_key[letter]
        else:
            decoded += letter

    return decoded

@click.command()
@click.argument('message', type=str)
def main(message):
    """A simple CLI tool to encode or decode a message with a given offset."""
    key = generate_key()
    encoded = encode(key, message)
    decoded = decode(key, encoded)    
    print(f"Key: {key}")
    print(f"Encoded: {encoded}")
    print(f"Decoded: {decoded}")

if __name__ == '__main__':
    main()

