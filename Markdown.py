#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
File: markdown.py
Author: Tim Coates
Description: Convert markdown text to html
"""

import argparse
import markdown


def markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html


def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content


def process_arguments():
    parser = argparse.ArgumentParser(description="Process command-line arguments.")
    
    # Add command-line arguments
    parser.add_argument('-f', '--file', help='Path to the input file', required=True)
    parser.add_argument('-o', '--output', help='Path to the output file', default='output.txt')
    
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    # Get the command-line arguments
    args = process_arguments()
    
    # Access the values of the arguments
    input_file = args.file
    output_file = args.output

    # Read contents from the input file
    try:
        input_content = read_file(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        exit(1)

    html_output = markdown_to_html(input_content)

    # Write content to the output file
    with open(output_file, 'w') as output:
        output.write(html_output)