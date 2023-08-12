import click

def encode(offset, message):
    encoded = ""
    message = message.lower().strip()
    for letter in message:
        if letter.isalpha():
            num = ord(letter)
            num = num + offset
            if num > ord("z"):
                num = num - 26

            encoded += chr(num)
        else:
            encoded += letter

    return encoded


def decode(offset, message):
    decoded = ""
    message = message.lower().strip()
    for letter in message:
        if letter.isalpha():
            num = ord(letter)
            num = num - offset
            if num < ord("a"):
                num = num + 26

            decoded += chr(num)
        else:
            decoded += letter

    return decoded

@click.command()
@click.argument('offset', type=int)
@click.argument('message', type=str)
@click.option('-e', 'operation', flag_value='encode', help='Encode the message')
@click.option('-d', 'operation', flag_value='decode', help='Decode the message')
def main(offset, message, operation):
    """A simple CLI tool to encode or decode a message with a given offset."""
    offset = offset % 26

    if operation == 'encode':
        result = encode(offset, message)
        click.echo(f'Encoded message with offset {offset}: {result}')
    elif operation == 'decode':
        result = decode(offset, message)
        click.echo(f'Decoded message with offset {offset}: {result}')
    else:
        click.echo('Please provide either -e for encode or -d for decode.')

if __name__ == '__main__':
    main()

