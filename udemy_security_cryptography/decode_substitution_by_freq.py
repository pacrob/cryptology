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

def generate_letter_frequency(message):
    letter_count = {}
    for letter in message:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    letter_freq = {}
    for letter in letter_count:
        letter_freq[letter] = letter_count[letter] / len(message) * 100

    return letter_freq


# @click.command()
# @click.argument('message', type=str)
# def main(message):
def main():

    original = "either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her, and to wonder what was going to happen next. first, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves: here and there she saw maps and pictures hung upon pegs. she took down a jar from one of the shelves as she passed; it was labelled 'orange marmalade,' but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody underneath, so managed to put it into one of the cupboards as she fell past it"
    message = "okwcog wco fouu fya vogm doos, zg aco iouu vogm auzfum, izg aco cyd suolwm zi wkeo ya aco folw dzfl wz uzzq ybztw cog, yld wz fzldog fcyw fya rzklr wz cyssol lonw. ikgaw, aco wgkod wz uzzq dzfl yld eyqo ztw fcyw aco fya pzeklr wz, btw kw fya wzz dygq wz aoo ylmwcklr; wcol aco uzzqod yw wco akdoa zi wco fouu, yld lzwkpod wcyw wcom fogo ikuuod fkwc ptsbzygda yld bzzq-acouvoa: cogo yld wcogo aco ayf eysa yld skpwtgoa ctlr tszl sora. aco wzzq dzfl y xyg igze zlo zi wco acouvoa ya aco syaaod; kw fya uybouuod 'zgylro eygeyuydo,' btw wz cog rgoyw dkaysszklweolw kw fya oeswm: aco dkd lzw ukqo wz dgzs wco xyg izg ioyg zi qkuuklr azeobzdm tldogloywc, az eylyrod wz stw kw klwz zlo zi wco ptsbzygda ya aco iouu syaw kw"
    # message = message.lower().strip()

    message_letter_freq = generate_letter_frequency(message)
    original_letter_freq = generate_letter_frequency(original)

    # print(f"Original letter frequency: {original_letter_freq}") 
    # print(f"Message letter frequency: {message_letter_freq}")

    all_alphas = string.ascii_lowercase
    for letter in all_alphas:
        if letter not in message_letter_freq:
            message_letter_freq[letter] = 0
            
    message_letter_freq_sorted = sorted(message_letter_freq.items(), key=lambda x: x[1], reverse=True)
    original_letter_freq_sorted = sorted(original_letter_freq.items(), key=lambda x: x[1], reverse=True)

    decode_dict = {}
    for i in range(len(message_letter_freq_sorted)):
        decode_dict[message_letter_freq_sorted[i][0]] = letter_frequency_sorted[i][0]

    decoded_message = ""
    for letter in message:
        if letter.isalpha():
            decoded_message += decode_dict[letter]
        else:
            decoded_message += letter

    print(f"Decoded message: {decoded_message}")


if __name__ == '__main__':
    main()

