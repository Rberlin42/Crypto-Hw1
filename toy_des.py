import binascii

#permutations
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
Pinital = [2, 6, 3, 1, 4, 8, 5, 7]
Pinverse = [4, 1, 3, 5, 7, 2, 8, 6]
P10to8 = [6, 3, 7, 4, 8, 5, 10, 9]
P4expansion = [4, 1, 2, 3, 2, 3, 4, 1]
P4 = [2, 4, 3, 1]

#S-Box
S0 = [["01", "00", "11", "10"],
	  ["11", "10", "01", "00"],
	  ["00", "10", "01", "11"],
	  ["11", "01", "11", "10"]]
S1 = [["00", "01", "10", "11"],
	  ["10", "00", "01", "11"],
	  ["11", "00", "01", "00"],
	  ["10", "00", "01", "11"]]


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

#returns a permutation of the bits according to the array permutation
def permuteBits(bits, permutation):
	newString = ""
	for p in permutation:
		newString += bits[p-1]
	return newString


#takes 4-bit input and returns 2-bits based on the sbox
def substituteBits(bits, sbox):
	#check length
	if len(bits) != 4:
		raise ValueError("Must enter 4 bits")

	#calculate row using first and last bits
	row = int("0b" + bits[0] + bits[3], 2)
	#calculate col using middle bits
	col = int("0b" + bits[1] + bits[2], 2)

	return sbox[row][col]

#Shifts the bits by amount
#positive amount is left shift, negative is right
def shiftBits(bits, amount):
	shifted = ""
	for i in range(len(bits)):
		i = (i + amount) % len(bits)
		shifted += bits[i]
	return shifted

#takes 10-bit key and returns 8-bit keys (k1, k2)
def getSubKeys(key):
	#Permute
	key = permuteBits(key, P10)
	#split in half
	left = key[:5]
	right = key[5:]
	#left shift each
	left = shiftBits(left, 1)
	right = shiftBits(right, 1)

	#Combine, permute and get k1
	k1 = left + right
	k1 = permuteBits(k1, P10to8)

	#shift again, combine, permute and get k2
	left = shiftBits(left, 1)
	right = shiftBits(right, 1)
	k2 = left + right
	k2 = permuteBits(k2, P10to8)

	return k1, k2



#def encrypt(data, key):


#def decrypt(data, key):

