# Module-10
import sys

for line in sys.stdin:
  cypher_number = sys.argv
  encoded_message = ""
      for char in line:
          if ord(char) >=65 and ord(char)<=90:
              next_char_index = ord(char) + cypher_number
              #if the index character is more than 90 we use the overflow, which is 90 minus the index character, that gives us the number that needs to be added to "A" index to continue from the beginning of the alphabet
              if next_char_index >90:
                overflow = next_char_index - 90
                next_char_index = 64 + overflow
              encoded_message = encoded_message + chr(next_char_index) 
          elif ord(char) >=97 and ord(char)<=122:
              next_char_index = ord(char) + cypher_number
              if next_char_index >122:
                overflow = next_char_index - 122
                next_char_index = 96 + overflow
              encoded_message = encoded_message + chr(next_char_index)
          else:
              encoded_message += char
      print(encoded_message)
