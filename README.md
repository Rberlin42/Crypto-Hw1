# Crypto-Hw1
### Cryptography and Network Security Homework 1

This program is an implementation of a "toy des", a simplified version of DES that encrypts 8-bit blocks using a 10-bit key over
2 rounds. The program allows for any type of file to be encrypted and sent to another user, and for receiving the 
encrypted file and decrypting it.  To use the program, follow the steps below:
1. Run file_transfer.py from two different locations using **Python 3**. One end will be the sender and the other the receiver
2. It will begin by prompting for the 10-bit key to be used in the encryption\decryption. Be sure that
the same key is used by both the sender and receiver, otherwise the file will not be successfully decrypted.
3. Next, enter either "SEND" or "RECEIVE".
  + RECEIVE: The program will now listen for a connection from the sender, and will display the port it is listening on.
  +	SEND: The program will now issue a series of prompts:
    1. file - name of the file to send
    2. ip - IP address of receiver
    3. port - port of receiver

After all of the inputs have been gathered on both ends, a connection will be established and the file will be encrypted, sent over
TCP, received, and finally decrypted. This program will work on any type of files, text or binary.

## Implementation Details
My program is split into two different files: one being the toy DES implementation (toy_des.py), and the other being the program to
send and receive files over TCP, encrypting on one end and decrypting on the other (file_transfer.py).  I began working in Python 2, but later converted
to python 3 to make use of the bytes object.  I found this to be much easier to use when having to read/write files in bytes, and then
having to do all the encryption\decryption in bits.  The program will read data from the file, encrypt, and send data 1024 bytes at a time. The toy DES implementation is a simplified version of DES that encrypts bits in 8-bit blocks, using a 10-bit key, and only goes through 2
rounds as opposed to 16. My implementation has two functions `encrypt` and `decrypt` that take in any amout of bits and returns the
cyphertext/plaintext.  These both call one main function, `toy_des`, which accepts an 8-bit block and will either encrypt or decrypt it. In addidtion, there are also several helper functions to aid in computing the encryption and decryption. The permutations and S-boxes are
hard coded in for this implementation as well.

The `toy_des` function begins by generating the subkeys for each round from the key provided by the user.  The order of which key is used
during which round depends on if we are encrypting or decrypting.  It then computes the initial permutation and splits the bits into left 
and right.  From there it will compute both rounds of encryption\decryption using the F and XOR functions, and finally it will inverse
the initial permutation and return the cyphertext\plaintext.