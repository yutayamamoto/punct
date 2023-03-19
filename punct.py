#!/usr/bin/python3

import re
import sys
import argparse

def replace_punctuation(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    text = re.sub(r'\.\s*\n', r'。\n', text)
    text = re.sub(r',\s*\n', r'、\n', text)
    text = re.sub(r'\.\s+', '。', text)
    text = re.sub(r',\s+', '、', text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="punct.py", description='convert japanese punctuation style')

    parser.add_argument('input_filename')
    parser.add_argument('output_filename')
    args = parser.parse_args()

    if args.input_filename == args.output_filename:
        print('Specify different names for input and output files.')
        sys.exit()

    replace_punctuation(args.input_filename, args.output_filename)

