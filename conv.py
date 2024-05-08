import os
import sys
import re
import argparse

def convert_punctuation(text):
    punctuation_mapping = {
        "。": ". ",
        "，": ", ",
        "？": "? ",
        "！": "! ",
        "：": ": ",
        "；": "; ",
        "、": "/",
        "“": '"' ,
        "”": '"' ,
        "‘": "'",
        "’": "'",
        "（": "(",
        "）": ")",
        "【": "[",
        "】": "]",
        "｛": "{",
        "｝": "}",
        "《": "<<",
        "》": ">>",
    }

    for ch, en in punctuation_mapping.items():
        text = re.sub(re.escape(ch), en, text)

    return text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert Chinese punctuation to English.')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output file path')

    args = parser.parse_args()
    
    if not os.path.exists(args.input_file):
        print(f"Error: Input file `{args.input_file}` does not exist.")
        sys.exit(0)

    with open(args.input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    converted_text = convert_punctuation(text)

    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(converted_text)