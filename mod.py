# Module-10
import sys

for line in sys.stdin:
  encryption_option = input("Would you like to Encode or Decode? ") 
  should_encode = "encode" in encryption_option.lower()
  should_decode = "decode" in encryption_option.lower()
  cypher_number = int(input("What is your cypher number? "))
  message = input("What is your message? ")
  encoded_message = ""
  if should_encode:
      for char in message:
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

  elif should_decode:
      for char in message:
          if ord(char) >=65 and ord(char)<=90:
              next_char_index = ord(char) - cypher_number
              if next_char_index <65:
                underflow = 65 - next_char_index
                next_char_index = 91 - underflow
              encoded_message = encoded_message + chr(next_char_index)
          elif ord(char) >=97 and ord(char)<=122:
              next_char_index = ord(char) - cypher_number
              if next_char_index <97:
                underflow = 97 - next_char_index
                next_char_index = 123 - underflow
              encoded_message = encoded_message + chr(next_char_index)
          else:
              encoded_message += char
      print(encoded_message)
  else:
      # Print a nice notice that we only support encrypt/decrypt
      # Your code here!
      print("We only support encoding and decoding, sorry!")
