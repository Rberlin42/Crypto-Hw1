import binascii

#permutation
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
Pinital = [2, 6, 3, 1, 4, 8, 5, 7]
Pinverse = [4, 1, 3, 5, 7, 2, 8, 6]
P10to8 = [6, 3, 7, 4, 8, 5, 10, 9]
P4expansion = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]


#returns a permutation of the bits according to the array permutation
#arguments must have same length
def permuteBits(bits, permutation):
	if len(bits) != len(permutation):
		raise ValueError("length does not match")

	newString = ""
	for p in permutation:
		newString += bits[p-1]
	return newString

#convert bytes to a string of bits
def getBits(str):
	size = len(str)
	binary = bin(int(binascii.hexlify(str), 16))
	#remove the "0b"
	bits = binary[2:]
	#add leading 0s
	while len(bits) < size*8:
		bits = "0" + bits
	return bits

#convert a string of bits to bytes
#bits must be a multiple of 8
def getBytes(binary):
	#check that we have the correct amount of bits
	if len(binary) % 8 != 0:
		raise ValueError("bits must come in multiple of 8")

	#add "0b"
	binary = "0b" + binary
	hex = "%x" % int(binary, 2)
	if len(hex) % 2 != 0:
		hex = "0" + hex
	return binascii.unhexlify(hex)

#def encrypt(data, key):


#def decrypt(data, key):

