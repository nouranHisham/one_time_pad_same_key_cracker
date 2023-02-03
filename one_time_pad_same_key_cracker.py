# -*- coding: utf-8 -*-
"""one_time_pad_same_key_cracker.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1O3zoPPjMzz1HkoM-JvtPu921iJUxlkbr

# **Imports**
"""

import numpy as np
import codecs

"""# **A function to convert a list to string**"""

def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele
        
    return str1

"""# **The list of ciphers**"""

c1 = '68AF0BEF7F39982DA975B5E6D06947E61C22748C94A2155CFCCC464DEAFB6F4844DB2D7312ED192B6B7251580C61D5A296964E824A16648B16B9'
c2 = '70A20FBD7E209324A979BFE2997A46E61B22749692EB1655FA995D46A9FA654F43C93F2114A21E3E227714580A6790B88BD74F9E09107D8B0EAC'
c3 = '6FA20DBA622CDD28EC68F0F0C16D41A7023778C29EB8455EFC894B46EDA96C46459E2D2A1CEF1239707F571604618CEB9DD85E955013628B0DAE'
c4 = '6FA20DBA6220893AA970A4B5CD664CE609286D8799B80010F68A0F56FAE868405BD72A2A51E118386E7214520E6994AC9D964E824A16648B16B9'
c5 = '71A80AAA6227DD20FB68A0E1D6695BA71C3864C285AE1445F09E4A50A9EA6B5B52D82B3F51E3192922645D5100769ABE8B965C89480F6F910BB3'
c6 = '7DA30ABD753A8E63FB70BEF1D66340BC0D24748D99EB065FEC804B03F9FB6F5F52D02A731CE31B24617F5B431C2496AA94DA1D865D17778109B3'
c7 = '75B34EA66369932CFD31A0E7D86D5DAF0F3171C283A44542FC805603FAE6664C5BC77E3C1FA204346F7B51421D6D96EB9DD85E955013628B0DAE'
c8 = '75E71DA771259163E774A6F0CB2E5BA3192378C283A30010EA8D4246A9F96B5A44C9312115A21823227B415A1B6D85A79D965C844A0C638C16B3'

ciphers = [c1, c2, c3, c4, c5, c6, c7, c8]

"""# **Converting the ciphers to bytes**"""

decoded_ciphers = []

for i in range(8):
  ciphers[i] = codecs.decode(ciphers[i],'hex')
  decoded_ciphers.append(ciphers[i])

"""# **Making an array of integers for the ciphers**"""

ciphers_byte_array = []

for i in range(8):
  decoded_ciphers[i] = np.array(list(decoded_ciphers[i]))
  ciphers_byte_array.append(decoded_ciphers[i])

"""# **XORing each cipher with one another**

This would benefit me as by doing this I get the messages xored with one another which is a piece of information that I would use later.
"""

ciphers_xored = []
indices_dict = {}
count = 0

for i in range(8):
  for j in range(i+1, 8):
    r = ciphers_byte_array[i].astype(np.int8) ^ ciphers_byte_array[j].astype(np.int8)
    ciphers_xored.append(r)
    indices_dict[count] = [i+1, j+1]
    count += 1

"""# **XORing the result of xoring each cipher with one another with space**

In this step, after getting the messages xored with one another in the previous step, I xored the messages with space to be able to identify where the spaces are located in each message.
"""

ciphers_xored_with_space = []

for i in range(28):
  s = ciphers_xored[i].astype(np.int8) ^ 0x20
  ciphers_xored_with_space.append(s)

ciphers_xored_with_space[0]

"""# **Trying to find the possible indices of spaces**

Here, to be able to get the possible space indices, I looped around the array looking for ascii numbers between 97 and 122 as these are the represenations of small letters in ascii which would mean that one of the two messages has a space in this specific position.
"""

possible_space_indices_dict = {}

for i in range(28):
  possible_space_indices = []
  for j in range(58):
    if (ciphers_xored_with_space[i][j] >= 97 and ciphers_xored_with_space[i][j] <= 122):
      possible_space_indices.append(j)
  possible_space_indices_dict[i] = possible_space_indices

"""# **A list of possible space indices for each two ciphers**"""

possible_space_indices_dict

"""# **This is just to see which row corresponds to which two xored ciphers**"""

indices_dict

"""# **This is used to gather all the combinations of each cipher together to be able to count the votes on the space indices**"""

c1_spaces = [possible_space_indices_dict[0], possible_space_indices_dict[1], possible_space_indices_dict[2], possible_space_indices_dict[3], possible_space_indices_dict[4], possible_space_indices_dict[5], possible_space_indices_dict[6]]
c2_spaces = [possible_space_indices_dict[0], possible_space_indices_dict[7], possible_space_indices_dict[8], possible_space_indices_dict[9], possible_space_indices_dict[10], possible_space_indices_dict[11], possible_space_indices_dict[12]]
c3_spaces = [possible_space_indices_dict[1], possible_space_indices_dict[7], possible_space_indices_dict[13], possible_space_indices_dict[14], possible_space_indices_dict[15], possible_space_indices_dict[16], possible_space_indices_dict[17]]
c4_spaces = [possible_space_indices_dict[2], possible_space_indices_dict[8], possible_space_indices_dict[13], possible_space_indices_dict[18], possible_space_indices_dict[19], possible_space_indices_dict[20], possible_space_indices_dict[21]]
c5_spaces = [possible_space_indices_dict[3], possible_space_indices_dict[9], possible_space_indices_dict[14], possible_space_indices_dict[18], possible_space_indices_dict[22], possible_space_indices_dict[23], possible_space_indices_dict[24]]
c6_spaces = [possible_space_indices_dict[4], possible_space_indices_dict[10], possible_space_indices_dict[15], possible_space_indices_dict[19], possible_space_indices_dict[22], possible_space_indices_dict[25], possible_space_indices_dict[26]]
c7_spaces = [possible_space_indices_dict[5], possible_space_indices_dict[11], possible_space_indices_dict[16], possible_space_indices_dict[20], possible_space_indices_dict[23], possible_space_indices_dict[25], possible_space_indices_dict[27]]
c8_spaces = [possible_space_indices_dict[6], possible_space_indices_dict[12], possible_space_indices_dict[17], possible_space_indices_dict[21], possible_space_indices_dict[24], possible_space_indices_dict[26], possible_space_indices_dict[27]]

"""# **This a 2-D counting matrix to count how many times a certain position is said to a space index in each cipher**

The aim of this 2-D counting matrix is to gather votes on the positions that most likely contain space in each cipher and then looping around this matrix by a certain threshold (4) to consider this as an actual space index.
"""

counting_matrix = np.zeros((8, 58)).astype(np.int8)

for i in range(7):
  for j in range(len(c1_spaces[i])):
    counting_matrix[0][c1_spaces[i][j]] += 1

for i in range(7):
  for j in range(len(c2_spaces[i])):
    counting_matrix[1][c2_spaces[i][j]] += 1

for i in range(7):
  for j in range(len(c3_spaces[i])):
    counting_matrix[2][c3_spaces[i][j]] += 1

for i in range(7):
  for j in range(len(c4_spaces[i])):
    counting_matrix[3][c4_spaces[i][j]] += 1

for i in range(7):
  for j in range(len(c5_spaces[i])):
    counting_matrix[4][c5_spaces[i][j]] += 1

for i in range(7):
  for j in range(len(c6_spaces[i])):
    counting_matrix[5][c6_spaces[i][j]] += 1

for i in range(7):
  for j in range(len(c7_spaces[i])):
    counting_matrix[6][c7_spaces[i][j]] += 1

for i in range(7):
  for j in range(len(c8_spaces[i])):
    counting_matrix[7][c8_spaces[i][j]] += 1

counting_matrix

import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)
display(pd.DataFrame(counting_matrix))

"""# **I used a threshold of 4 to consider the position an actual space index.**

# **Then I filled the key at these positions by xoring space with eachcipher at these ceratin positions as well**

By xoring space with with the ciphers at the space indices, the corresponding part of the key is going to be revealed at each position so that I can be able to find as many letters as possible and guess the rest.
"""

possible_key1 = np.empty(58)

for i in range(58):
  if (counting_matrix[0][i] >= 4):
    possible_key1[i] = ciphers_byte_array[0][i].astype(np.int8) ^ 0x20

for i in range(58):
  if (counting_matrix[1][i] >= 4):
    possible_key1[i] = ciphers_byte_array[1][i].astype(np.int8) ^ 0x20

for i in range(58):
  if (counting_matrix[2][i] >= 4):
    possible_key1[i] = ciphers_byte_array[2][i].astype(np.int8) ^ 0x20

for i in range(58):
  if (counting_matrix[3][i] >= 4):
    possible_key1[i] = ciphers_byte_array[3][i].astype(np.int8) ^ 0x20

for i in range(58):
  if (counting_matrix[4][i] >= 4):
    possible_key1[i] = ciphers_byte_array[4][i].astype(np.int8) ^ 0x20

for i in range(58):
  if (counting_matrix[5][i] >= 4):
    possible_key1[i] = ciphers_byte_array[5][i].astype(np.int8) ^ 0x20

for i in range(58):
  if (counting_matrix[6][i] >= 4):
    possible_key1[i] = ciphers_byte_array[6][i].astype(np.int8) ^ 0x20

for i in range(58):
  if (counting_matrix[7][i] >= 4):
    possible_key1[i] = ciphers_byte_array[7][i].astype(np.int8) ^ 0x20

possible_key1 = possible_key1.astype(np.int8)

possible_key1

"""# **This is the ascii of the possible messages by xoring the possible key with each cipher**"""

m1 = ciphers_byte_array[0].astype(np.int8) ^ possible_key1
for i in range(58):
   if(ciphers_byte_array[0][i].astype(np.int8) == m1[i].astype(np.int8)):
     m1[i] = 0

m2 = ciphers_byte_array[1].astype(np.int8) ^ possible_key1
for i in range(58):
   if(ciphers_byte_array[1][i].astype(np.int8) == m2[i].astype(np.int8)):
     m2[i] = 0

m3 = ciphers_byte_array[2].astype(np.int8) ^ possible_key1
for i in range(58):
   if(ciphers_byte_array[2][i].astype(np.int8) == m3[i].astype(np.int8)):
     m3[i] = 0

m4 = ciphers_byte_array[3].astype(np.int8) ^ possible_key1
for i in range(58):
   if(ciphers_byte_array[3][i].astype(np.int8) == m4[i].astype(np.int8)):
     m4[i] = 0

m5 = ciphers_byte_array[4].astype(np.int8) ^ possible_key1
for i in range(58):
   if(ciphers_byte_array[4][i].astype(np.int8) == m5[i].astype(np.int8)):
     m5[i] = 0

m6 = ciphers_byte_array[5].astype(np.int8) ^ possible_key1
for i in range(58):
   if(ciphers_byte_array[5][i].astype(np.int8) == m6[i].astype(np.int8)):
     m6[i] = 0

m7 = ciphers_byte_array[6].astype(np.int8) ^ possible_key1
for i in range(58):
   if(ciphers_byte_array[6][i].astype(np.int8) == m7[i].astype(np.int8)):
     m7[i] = 0

m8 = ciphers_byte_array[7].astype(np.int8) ^ possible_key1
for i in range(58):
   if(ciphers_byte_array[7][i].astype(np.int8) == m8[i].astype(np.int8)):
     m8[i] = 0

possible_messages = [m1, m2, m3, m4, m5, m6, m7, m8]

possible_messages

"""# **This is mapping the ascii to their corresponding characters**"""

possible_message_char = []
for j in range(58):
    if (m1[j].astype(np.int8) >= 97 and m1[j].astype(np.int8) <= 122):
      letter = chr(m1[j].astype(np.int8))
    elif (m1[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    possible_message_char.append(letter)
print("(message 1):", listToString(possible_message_char), "\n")

possible_message_char = []
for j in range(58):
    if (m2[j].astype(np.int8) >= 97 and m2[j].astype(np.int8) <= 122):
      letter = chr(m2[j].astype(np.int8))
    elif (m2[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    possible_message_char.append(letter)
print("(message 2):", listToString(possible_message_char), "\n")

possible_message_char = []
for j in range(58):
    if (m3[j].astype(np.int8) >= 97 and m3[j].astype(np.int8) <= 122):
      letter = chr(m3[j].astype(np.int8))
    elif (m3[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    possible_message_char.append(letter)
print("(message 3):", listToString(possible_message_char), "\n")

possible_message_char = []
for j in range(58):
    if (m4[j].astype(np.int8) >= 97 and m4[j].astype(np.int8) <= 122):
      letter = chr(m4[j].astype(np.int8))
    elif (m4[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    possible_message_char.append(letter)
print("(message 4):", listToString(possible_message_char), "\n")

possible_message_char = []
for j in range(58):
    if (m5[j].astype(np.int8) >= 97 and m5[j].astype(np.int8) <= 122):
      letter = chr(m5[j].astype(np.int8))
    elif (m5[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    possible_message_char.append(letter)
print("(message 5):", listToString(possible_message_char), "\n")

possible_message_char = []
for j in range(58):
    if (m6[j].astype(np.int8) >= 97 and m6[j].astype(np.int8) <= 122):
      letter = chr(m6[j].astype(np.int8))
    elif (m6[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    possible_message_char.append(letter)
print("(message 6):", listToString(possible_message_char), "\n")

possible_message_char = []
for j in range(58):
    if (m7[j].astype(np.int8) >= 97 and m7[j].astype(np.int8) <= 122):
      letter = chr(m7[j].astype(np.int8))
    elif (m7[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    possible_message_char.append(letter)
print("(message 7):", listToString(possible_message_char), "\n")

possible_message_char = []
for j in range(58):
    if (m8[j].astype(np.int8) >= 97 and m8[j].astype(np.int8) <= 122):
      letter = chr(m8[j].astype(np.int8))
    elif (m8[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    possible_message_char.append(letter)
print("(message 8):", listToString(possible_message_char), "\n")

"""# **The cipher I was able to guess is:**

(message 8): i shall never reuse the same password in  multiple accounts

# **Changing the guessed message from characters to ascii**
"""

possible_message8 = "i shall never reuse the same password in multiple accounts"

possible_message8_ascii = []

for i in range(58):
  ascii = ord(possible_message8[i])
  possible_message8_ascii.append(ascii)

"""# **Attempt to find the correct key by xoring the guessed message with its cipher**

By doing this, I'm trying to get the actual key as now I have the message and it's cipher so xoring them would help me get the key and decrypt the rest of the ciphers.
"""

correct_key = possible_message8_ascii ^ ciphers_byte_array[7]

correct_key.astype(np.int8)

possible_key1

"""# **Getting the correct messaged by xoring their ciphers with the correct key**"""

message1 = ciphers_byte_array[0].astype(np.int8) ^ correct_key.astype(np.int8)
message2 = ciphers_byte_array[1].astype(np.int8) ^ correct_key.astype(np.int8)
message3 = ciphers_byte_array[2].astype(np.int8) ^ correct_key.astype(np.int8)
message4 = ciphers_byte_array[3].astype(np.int8) ^ correct_key.astype(np.int8)
message5 = ciphers_byte_array[4].astype(np.int8) ^ correct_key.astype(np.int8)
message6 = ciphers_byte_array[5].astype(np.int8) ^ correct_key.astype(np.int8)
message7 = ciphers_byte_array[6].astype(np.int8) ^ correct_key.astype(np.int8)
message8 = ciphers_byte_array[7].astype(np.int8) ^ correct_key.astype(np.int8)

correct_messages = [message1, message2, message3, message4, message5, message6, message7, message8]

correct_message_char = []
for j in range(58):
    if (message1[j].astype(np.int8) >= 97 and message1[j].astype(np.int8) <= 122):
      letter = chr(message1[j].astype(np.int8))
    elif (message1[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    correct_message_char.append(letter)
print("(correct message 1):", listToString(correct_message_char), "\n")

correct_message_char = []
for j in range(58):
    if (message2[j].astype(np.int8) >= 97 and message2[j].astype(np.int8) <= 122):
      letter = chr(message2[j].astype(np.int8))
    elif (message2[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    correct_message_char.append(letter)
print("(correct message 2):", listToString(correct_message_char), "\n")

correct_message_char = []
for j in range(58):
    if (message3[j].astype(np.int8) >= 97 and message3[j].astype(np.int8) <= 122):
      letter = chr(message3[j].astype(np.int8))
    elif (message3[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    correct_message_char.append(letter)
print("(correct message 3):", listToString(correct_message_char), "\n")

correct_message_char = []
for j in range(58):
    if (message4[j].astype(np.int8) >= 97 and message4[j].astype(np.int8) <= 122):
      letter = chr(message4[j].astype(np.int8))
    elif (message4[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    correct_message_char.append(letter)
print("(correct message 4):", listToString(correct_message_char), "\n")

correct_message_char = []
for j in range(58):
    if (message5[j].astype(np.int8) >= 97 and message5[j].astype(np.int8) <= 122):
      letter = chr(message5[j].astype(np.int8))
    elif (message5[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    correct_message_char.append(letter)
print("(correct message 5):", listToString(correct_message_char), "\n")

correct_message_char = []
for j in range(58):
    if (message6[j].astype(np.int8) >= 97 and message6[j].astype(np.int8) <= 122):
      letter = chr(message6[j].astype(np.int8))
    elif (message6[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    correct_message_char.append(letter)
print("(correct message 6):", listToString(correct_message_char), "\n")

correct_message_char = []
for j in range(58):
    if (message7[j].astype(np.int8) >= 97 and message7[j].astype(np.int8) <= 122):
      letter = chr(message7[j].astype(np.int8))
    elif (message7[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    correct_message_char.append(letter)
print("(correct message 7):", listToString(correct_message_char), "\n")

correct_message_char = []
for j in range(58):
    if (message8[j].astype(np.int8) >= 97 and message8[j].astype(np.int8) <= 122):
      letter = chr(message8[j].astype(np.int8))
    elif (message8[j].astype(np.int8) == 32):
      letter = " "
    else:
      letter = "_."
    correct_message_char.append(letter)
print("(correct message 8):", listToString(correct_message_char))

"""# **The messages after guessing them are:**

(message 1): the open design principle increases confidence in security

(message 2): learning how to write secure software is a necessary skill

(message 3): secure key exchange is needed for symmetric key encryption

(message 4): security at the expense of usability could damage security

(message 5): modern cryptography requires carefull and  rigorous analysis

(message 6): address randomization could prevent malicious call attacks

(message 7): it is not practical to rely solely on symmetric encryption

(message 8): i shall never reuse the same password in multiple accounts
"""

