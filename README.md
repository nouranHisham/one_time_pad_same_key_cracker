# one_time_pad_same_key_cracker
This is a way to break the one time pad encryption algorithm if more than one block is encrypted using the same key.

Approach description:

1) XORing each cipher with one another.
This would benefit me as by doing this I get the messages xored with one another which is a piece of information that I would use later.

2) XORing the result of xoring each cipher with one another with space.
In this step, after getting the messages xored with one another in the previous step, I xored the messages with space to be able to identify where the spaces are located in each message.

3) A 2-D counting matrix to count how many times a certain position is said to a space index in each cipher.
The aim of this 2-D counting matrix is to gather votes on the positions that most likely contain space in each cipher and then looping around this matrix by a certain threshold (4) to consider this as an actual space index.

4) I used a threshold of 4 to consider the position an actual space index.
Then I filled the key at these positions by xoring space with eachcipher at these ceratin positions as well.
By xoring space with with the ciphers at the space indices, the corresponding part of the key is going to be revealed at each position so that I can be able to find as many letters as possible and guess the rest.

5) Attempting to find the correct key by xoring the guessed message with its cipher.
By doing this, I'm trying to get the actual key as now I have the message and it's cipher so xoring them would help me get the key and decrypt the rest of the ciphers.

6) Getting the correct messaged by xoring their ciphers with the correct key.
