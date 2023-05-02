#!/usr/bin/env python 3
import sys

def encrypt(plaintext, key):
  cyphertext = ''
  my_list = []

  plaintext_up = plaintext.upper()
  for char in plaintext_up:
    if char.isalpha():
      num_form = ord(char)
      num_form += key

      if num_form > ord('Z'):
        num_form -= 26

      elif num_form < ord('A'):
        num_form += 26

      char_form = chr(num_form)

    else:
      continue

    cyphertext += char_form

  for i in range(0, len(cyphertext), 5):
    div = ''
    div += cyphertext[i:i+5]
    i = i + 5

    my_list.append(div)

  return '\n'.join(' '.join(my_list[x:x+10]) for x in range(0, len(my_list), 10))

if __name__ = "__main__":
  key = int(sys.argv[1])

  if len(sys.argv) == 4:
    in_filename = sys.argv[2]
    out_filename = sys.argv[3]

    with open(in_filename, 'r') as file:
      normal_text = file.read()
      #print(normal_text)

    encrypted = encrypt(normal_text, key)
    with open(out_filename, 'w+') as file:
      encrypted_text = file.write(encrypted)

  elif len(sys.argv) == 3:
    with open(sys.argv[2], 'r') as file.h:
      lines = file_h.read()
      print(encrypt(lines, key))