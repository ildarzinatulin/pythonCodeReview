import os
import argparse
import re
import sys


def push(word1, word2):
    if word1 in d:
        if word2 in d[word1]:
            d[word1][word2] += 1
        else:
            d[word1][word2] = 1
    else:
        d[word1] = {}
        d[word1][word2] = 1


def load(line):
    if namespace.lc:
        line.lower()
    reg = re.compile('[^a-zA-Z ]')
    line = reg.sub('', line)
    words = line.split()
    for g in range(len(words) - 1):
        push(words[g], words[g + 1])


Parser = argparse.ArgumentParser()
Parser.add_argument('--input-dir', default=False, help='adress read file')
Parser.add_argument('--model', help='adress write file')
Parser.add_argument('--lc', action='store_const', const=True, help='make text lowercase')

d = {}
namespace = Parser.parse_args()
if namespace.input_dir:
    filesIn = os.listdir(namespace.input_dir)
    for i in filesIn:
        if i != '.DS_Store':
            my_file = open(str(namespace.input_dir + i), 'r').readlines()
            for line in my_file:
                load(line)
else:
    for line in sys.stdin:
        load(line)
fileOut = open(str(namespace.model), 'w')
for key in d:
    for key2 in d[key]:
        fileOut.write(key + " ")
        fileOut.write(key2 + " ")
        fileOut.write(str(d[key][key2]) + '\n')