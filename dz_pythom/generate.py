import argparse
import random


def new_word(lword):
    if d.get(lword):
        my_list = d[lword].keys()
        n = len(my_list)
        for elem in range(n):
            for g in range(d[lword][my_list[elem]] - 1):
                my_list.append(my_list[elem])
        return random.choice(my_list)
    else:
        return random.choice(d.keys())


def push(word1, word2, frncy):
    if word1 in d:
        d[word1][word2] = frncy
    else:
        d[word1] = {}
        d[word1][word2] = frncy


Parser = argparse.ArgumentParser()
Parser.add_argument('--model', help='adress of model')
Parser.add_argument('--seed', default=False, help='start word')
Parser.add_argument('--lenth', default=5, help='text size')
Parser.add_argument('--output', default=False, help='output file')

d = {}
namespace = Parser.parse_args()
my_file = open(str(namespace.model), 'r').readlines()
for line in my_file:
    lst = line.split()
    push(str(lst[0]), str(lst[1]), int(lst[2]))

if namespace.seed == False:
    start_word = random.choice(d.keys())
st = str(start_word)
for i in range(namespace.lenth - 1):
    start_word = new_word(start_word)
    st = st + " " + str(start_word)

if namespace.output:
    fileOut = open(str(namespace.output), 'w')
    fileOut.write(st)
else:
    print(st)
