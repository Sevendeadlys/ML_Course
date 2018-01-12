#!/usr/bin/env python3
# encoding: utf-8
import os.path
from PIL import Image

word_file = './words.txt'
q1_file = 'Q1.txt'
pic_file = './westbrook.jpg'
q2_file = 'Q2.jpg'


def count_word(input=word_file, output=q1_file):
    if not os.path.exists(input):
        return
    f_in = open(input, "r")
    f_out = open(output, "w+")
    line = f_in.readline()
    l1 = []
    l2 = []
    for w in line.split(' '):
        if w in l1:
            index = l1.index(w)
            l2[index] += 1
        else:
            l1.append(w)
            l2.append(1)

    for w, cnt in zip(l1, l2):
        s = w + " " + str(cnt) + "\n"
        f_out.write(s)

    f_in.close()
    f_out.close()


def half_rgb(input=pic_file, output=q2_file):
    if not os.path.exists(input):
        return
    im = Image.open(input)
    out = im.point(lambda i: i*0.5)
    im.close()
    out.save(output)


if __name__ == "__main__" :
    count_word()
    half_rgb()
