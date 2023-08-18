import click
import random
import string

letter_frequency = {
    'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702,
    'f': 2.228, 'g': 2.015, 'h': 6.094, 'i': 6.966, 'j': 0.153,
    'k': 0.772, 'l': 4.025, 'm': 2.406, 'n': 6.749, 'o': 7.507,
    'p': 1.929, 'q': 0.095, 'r': 5.987, 's': 6.327, 't': 9.056,
    'u': 2.758, 'v': 0.978, 'w': 2.360, 'x': 0.150, 'y': 1.974, 'z': 0.074
}

letter_frequency_sorted = sorted(letter_frequency.items(), key=lambda x: x[1], reverse=True)


@click.command()
@click.argument('message', type=str)
def main(message):

    message = message.lower().strip()
    letter_count = {}
    for letter in message:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    message_letter_freq = {}
    for letter in letter_count:
        message_letter_freq[letter] = letter_count[letter] / len(message) * 100

    all_alphas = string.ascii_lowercase
    for letter in all_alphas:
        if letter not in message_letter_freq:
            message_letter_freq[letter] = 0
            
    message_letter_freq_sorted = sorted(message_letter_freq.items(), key=lambda x: x[1], reverse=True)

    decoded_message = ""
    for letter in message:
        if letter.isalpha():
            for i in range(len(letter_frequency_sorted)):
                if letter == letter_frequency_sorted[i][0]:
                    decoded_message += message_letter_freq_sorted[i][0]
        else:
            decoded_message += letter

    print(f"Decoded message: {decoded_message}")


if __name__ == '__main__':
    main()

