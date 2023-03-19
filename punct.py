#!/usr/bin/python3

# ピリオドカンマを句読点 (。、) に変換するプログラム
# 直後に空白もしくは改行が続かない場合 ("hoge.huga" など) は変換しない。

import re
import sys

def replace_punctuation(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    text = re.sub(r'\.\s*\n', r'。\n', text)
    text = re.sub(r',\s*\n', r'、\n', text)
    text = re.sub(r'\.\s+', '。', text)
    text = re.sub(r',\s+', '、', text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

input_file = sys.argv[1]
output_file = sys.argv[2]

replace_punctuation(input_file, output_file)
