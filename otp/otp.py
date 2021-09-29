# USAGE
# python3 opt.py -k key.txt -m msg.txt

import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-k", "--key", required=True,
	help="key file - hex string >= length of message")
ap.add_argument("-m", "--message", required=True,
	help="text file to xor with the key")
args = vars(ap.parse_args())


msg = ''
key = ''

with open(args["key"]) as key_file:
    key = key_file.read()

with open(args["message"]) as msg_file:
    msg = msg_file.read()

xord = []

for x in range(len(msg)):
    m = ord(msg[x])
    k = ord(key[x])
    out = chr(m ^ k)
    xord.append(out)

output = ''.join(xord)

with open('output.txt', 'w') as out_file:
    out_file.write(output)


# with bob as a hex string
# split1 = ['0x' + bob[i:i+2] for i in range(0, len(bob), 2)]
# will provide put it in a list with 0x prefix
# then
# split2 = [chr(int(x, 16)) for x in split1]
# converts each hex string to its char

