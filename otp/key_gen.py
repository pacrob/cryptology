
import secrets
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--length", required=True, type=int,
	help="length of desired in in bytes")
ap.add_argument("-o", "--outputFile", default='newkey.txt',
	help="name of file to write key out to")
args = vars(ap.parse_args())

hex_string = secrets.token_hex(args["length"])

# create a list of hex bytes as strings (each prefixed with 0x, eg '0xa5', '0xff')
split1 = ['0x' + hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
# convert each hex byte to its associated ascii character
split2 = [chr(int(x, 16)) for x in split1]

new_key = ''.join(split2)

with open(args["outputFile"], 'w') as out_file:
    out_file.write(new_key)
