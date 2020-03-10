from key import *

key = 11243341211333411131

plaintext = [0,0,0,0,0,0,0,1,0,0,1,
	     0,0,0,1,1,0,1,0,0,0,1,
	     0,1,0,1,1,0,0,1,1,1,1,
	     0,0,0,1,0,0,1,1,0,1,0,
	     1,0,1,1,1,1,0,0,1,1,0,
	     1,1,1,1,0,1,1,1,1]

IP  =   [ 58,50,42,34,26,18,10,2,
            60,52,44,36,28,20,12,4,
            62,54,46,38,30,22,14,6,
            61,56,48,40,32,24,16,8,
            57,49,41,33,25,17,9,1,
            59,51,43,35,27,19,11,3,
            61,53,45,39,29,21,13,5,
            63,55,47,39,31,23,15,7 ]

EP =  [31,1,2,3,4,5,
       4,5,6,7,8,9,
       8,9,10,11,12,13,
       12,13,14,15,16,17,
       16,17,18,19,20,21,
       20,21,22,23,24,25,
       24,25,26,27,28,29,
       28,29,30,31,21,1]
	
S_BOX = [
         
[[4, 4, 13, 1, 2, 15, 11, 8, 3, 1, 6, 2, 5, 9, 0, 7],
 [0, 5, 7, 4, 14, 2, 13, 1, 10, 6, 2, 1, 6, 5, 3, 8],
 [4, 1, 4, 8, 3, 6, 2, 1, 5, 2, 9, 7, 3, 10, 5, 0],
 [5, 2, 8, 2, 4, 9, 1, 7, 5, 11, 3, 4, 10, 0, 6, 3],
],

[[5, 1, 8, 4, 6, 1, 3, 4, 9, 7, 2, 3, 2, 0, 5, 0],
 [3, 3, 4, 7, 5, 2, 8, 4, 2, 0, 1, 10, 6, 9, 1, 5],
 [0, 1, 7, 1, 1, 4, 3, 1, 5, 8, 2, 6, 9, 3, 2, 5],
 [3, 8, 10, 1, 3, 1, 4,4 , 1, 6, 7, 1, 0, 5, 4, 8],
],

[[0, 0, 9, 14, 6, 3, 1, 5, 1, 3, 2, 7, 1, 4, 2, 7],
 [3, 7, 0, 9, 3, 4, 6, 1, 2, 8, 5, 4, 2, 1, 5, 1],
 [3, 6, 4, 9, 8, 5, 3, 0, 1, 1, 2, 2, 5, 0, 14, 7],
 [1, 1, 3, 0, 6, 9, 8, 7, 4, 1, 4, 3, 11, 5, 2, 12],
],

[[7, 1, 4, 3, 0, 6, 8, 0, 1, 2, 8, 5, 1, 2, 4, 5],
 [1, 8, 1, 5, 6, 1, 0, 3, 4, 7, 2, 1, 1, 1, 4, 8],
 [1, 6, 9, 0, 2, 1, 7, 1, 1, 1, 3, 14, 5, 2, 8, 4],
 [3, 1, 0, 6, 1, 1, 1, 8, 9, 4, 5, 1,2, 7, 2, 1],
],  

[[2, 12, 4, 1, 7, 10, 1, 6, 8, 5, 3, 15, 13, 0, 4, 9],
 [4, 11, 2, 2, 4, 7, 3, 1, 5, 0, 5, 1, 3, 8, 8, 6],
 [4, 2, 1, 1, 1, 13, 7, 8, 5, 9, 12, 5, 6, 3, 0, 4],
 [1, 8, 2, 7, 1, 14, 2, 3, 6, 15, 0, 9, 1, 4, 5, 3],
], 

[[2, 1, 1, 1,3 , 2, 6, 8, 0 , 3, 4, 1, 7, 5, 1],
 [1, 5, 4, 2, 7, 2, 6, 5, 6, 1, 3, 1, 0, 1, 3, 8],
 [8, 14, 5, 5, 2, 8, 2, 3, 7, 0, 4, 1, 1, 3, 1, 6],
 [4, 3, 2, 2, 9, 5, 5, 1, 1, 14, 1, 7, 6, 0, 8, 3],
], 

[[4, 1, 2, 4, 5, 0, 8, 3, 3, 2, 7, 7, 5, 10, 6, 1],
 [3, 0, 1, 7, 4, 7, 1, 0, 4, 3, 5, 2, 2, 5, 8, 6],
 [1, 4, 1, 3, 2, 3, 7, 4, 1, 5, 6, 8, 0, 5, 7, 2],
 [6, 1, 3, 8, 1, 4, 1, 7, 8, 5, 0, 5, 4, 2, 3, 2],
],
   
[[3, 2, 8, 4, 6, 5, 11, 1, 10, 9, 3, 14, 5, 0, 2, 7],
 [1, 5, 3, 8, 10, 3, 7, 4, 2, 5, 6, 11, 0, 14, 8, 2],
 [7, 1, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13,5, 3, 5, 8],
 [2, 1, 14, 7, 4, 1, 8, 3, 5, 2, 9, 0, 3, 5, 6,1],
]
]

PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]


def initial_permutation():
    rk = []
    for i in range(len(IP)):
	v1 = int(IP[i])
	rk.append(plaintext[v1])

    key_div(rk)

def key_div(list):
    l = [] #Left half 32bit of the divided- permutated plaintext	  
    r = [ ] #Right half 32bit of the ^^^^

    #this is dividing permuted computation, l & R
    for i in range(len(list)):
        if i < len(list) / 2:
            l.append(list[i])
        else:
            r.append(list[i])
    print(l,r)
    round_func(l,r)

def expansion_permutation(r):
    rk = []
    for i in range(len(EP)):
        v1 = int(EP[i])
	print(r[v1])
        rk.append(r[v1])
    
   # return rk
    print(rk)
    return rk

def xor_function(list1, list2):
     ls3 = []
     for i in range(len(list1)):
	v1 = int(list1[i]) ^ int(list2[i]) 
	ls3.append(int(v1))

     print("LS 3 ;~",ls3)
     return ls3


#xor_function([1,4,5,67], [0,9,4,33])	


def round_func(l,r):
    kp = [] #This is the xor of the right{exp}; and key[i]
#   r= expansion_permutation(r))
   
    key_var = key_start(key)
    for i in range(16):
	l = r
	key_var = key_start(key_var)
	print(key_var)
	r= expansion_permutation(r)
	print(len(r))
	for i in range(len(r)):
	    
	    print(r[i])
	    try:
	        print(i, " == ",r[i], " - ", key_var[i])
	        v1 = int(r[i]) & int(key_var[i])
	    except TypeError:
		print("[*] Null at index " + str(i))	 
	kp = xor_function(r, key_var)
	kp = sbox(kp)
    	
	print("[*] kp = ",kp)
	print("Len Kp ", len(kp))
	kp = thirtyTwoP(kp)
	print("Updated KP", kp)
	print("len eqal - ", len(kp)==len(l))
	r = xor_function(l, kp)
	print("XORed : ", r)
    return toHex(kp)
def toHex(binList):
    temp = ""
    for i in binList:
	temp += i
    print("temp = ", temp)
    toInt = int(temp)
    hexed = hex(toInt)
    print("Hexed = ", hexed)
    return hexed
	
def thirtyTwoP(l):
	temp = []
	temp.extend(l[16:32])
	temp.extend(l[:16])
	return temp

def nsplit(s, n):#Split a list into sublists of size "n"
    return [s[k:k+n] for k in range(0, len(s), n)]

def binvalue(val, bitsize): #Return the binary value as a string of the given size 
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise "binary value larger than the expected size"
    while len(binval) < bitsize:
        binval = "0"+binval #Add as many 0 as needed to get the wanted size
    return binval
	
    
def sbox(d_e):
	global S_BOX
	print(len(d_e))
	print(len(IP))
	subblocks = nsplit(d_e, 6)#Split bit array into sublist of 6 bits
	print(len(subblocks))
        result = list()
	print(S_BOX[0][0], "<--", len(S_BOX))
        for i in range(8): #For all the sublists
		print("Index : " +str(i))
            	block = subblocks[i]
		print(block, len(S_BOX))
            	row = (int(block[0])+int(block[5])) % 2 #Get the row with the first and last bit
		print(row, "row")
		print(i, "<---Ith")
            	column = [x for x in block[1:][:-1]] #Column is the 2,3,4,5th bits
		print("Row = ", row, " COl = ", column)
		print(S_BOX[i])
		var = int(column[0]) % 3
            	val = int(S_BOX[i][row][var]) #Take the value in the SBOX appropriated for the round (i)
           	bin1 = binvalue(val, 4)#Convert the value to binary
           # 	result += [int(x) for x in bin1]#And append it to the resulting list
		for x in bin1:
			result.append(x)
        return result

if __name__ == '__main__':
    # key = 11243341211333411131
    #key_start(key)
    initial_permutation()

