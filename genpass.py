#!/usr/bin/env python3
'''
Generate random password that contains at least 1 lowercase, 1 uppercase,
1 numeric and 1 punctuation.
'''
import argparse
import random
import string

all_chars = (string.ascii_lowercase + string.ascii_uppercase +
             string.digits + string.punctuation)
parser = argparse.ArgumentParser()
parser.add_argument('-l', '--length', help="Password length", default=10)
args = parser.parse_args()


def genpass(length=args.length):
    password = []
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    password.append(random.choice(string.punctuation))
    for i in range(int(length) - 4):
        password.append(random.choice(all_chars))
    random.shuffle(password)
    return ''.join(password)

if __name__ == '__main__':
    print(genpass())
