# USAGE
# python3 opt.py -k key.txt -m msg.txt

import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--key", required=True,
	help="key file - string >= length of message")
ap.add_argument("-m", "--message", required=True,
	help="text file to xor with the key")
ap.add_argument("-o", "--outputFile", default='output.txt',
	help="name of file to write output string to")
args = vars(ap.parse_args())


msg = ''
key = ''

with open(args["key"]) as key_file:
    key = key_file.read()

with open(args["message"]) as msg_file:
    msg = msg_file.read()

xord = []

for x in range(len(msg)):
    # get the ascii integer for the character in each
    m = ord(msg[x])
    k = ord(key[x])
    # xor the integers and convert back to a character
    out = chr(m ^ k)
    # add the character to the output list
    xord.append(out)

# join the output list into a single string and write it out to file
output = ''.join(xord)

with open(args["outputFile"], 'w') as out_file:
    out_file.write(output)



