from itertools import permutations
co = []
do= []
pc1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,
        10,2,59,51,43,35,27,19,11,3,60,52,44,36,
        63,55,47,39,31,23,15,7,62,54,46,38,30,22,
        14,6,61,53,45,37,29,21,13,5,28,20,12,4]
    
pc2 = [
    14, 17, 11, 24, 1,  5,
    3,  28, 15, 6,  21, 10,
    23, 19, 12, 4,  26, 8,
    16, 7,  27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 53, 34, 53,
    46, 42, 50, 36, 29, 32]

def key_div(list):
    #this is dividing permuted computation, c0, d0
    for i in range(len(list)):
        if i < len(list) / 2:
             co.append(list[i])
        else:
            do.append(list[i])
    return(co,do)   

def key_start(key):
	#sees key; checks bit length; now should convert
	#it in list for easier manipulation hence functin call
    key = 11243341211333411131

    if key.bit_length() < 64:
        print("no")
    elif key.bit_length() == 64:
        print("yes")

   # print(key.bit_length()) #Checking bit length
    keyb = bin(key)
    print(keyb,"<BIN")
    print(len(keyb), "<")
    bin_to_list(keyb)	

def bin_to_list(keyb):
    ls = []
    for i in range(len(keyb)):
    #this loop is converting keyb into the list form for easier mainupluatrion
	ls.append(keyb[i])
    ls.pop(0)
    ls.pop(1)
    print("In binary to list")	
    #List is ready, now we should be doing compression algorithm; hence futture function call
    compression_permutation(ls, pc1)

def compression_permutation(ls,pc1, rk = [], flag = False): #first para: key-list, second: pc1/pc2
    for i in range(len(pc1)):
    #this loop-- stores the value at the i'th index in pc1, and puts it in the ith index of the key
	#This the PC1  
       v1 = int(pc1[i])
       rk.append(ls[v1])
    if flag == False:
        divide_nd_shift(rk)
    else:
        return rk

def divide_nd_shift(rk, shift_bit = 1):
    c1,d1 = key_div(rk)
 #   print(c1, len(c1) )
  #  print(d1, len(d1) )
    if shift_bit == 1 or shift_bit == 2 or shift_bit == 9 or shift_bit == 16:
        for i in range(len(c1)):
            var = c1[i]
	    var = int(var)
	    var <<= 1 #a <<= b 
            c1[i] = var
	   
	    var = d1[i]
	    var = int(var)
	    var <<= 1
	    d1[i] = var
	
    else:
	for i in range(len(c1)):
	    var = c1[i]
            var = int(var)
            var <<= 1 #a <<= b 
            c1[i] = var 
            var = d1[i]
            var = int(var)
            var <<= 1
            d1[i] = var
   # print(len(c1), "c1")
  #  print(len(d1), "d1")
    ready_for_round(c1,d1)

def compression_p2(ls, rk = []):
   # rk = []
    for i in range(len(pc2)):
	counter = 0
        v1 = int(pc2[i])
	counter += 1
#	print(v1, "<-v1-")
#	print(len(rk), "len rk")
	rk.append(ls[v1])	
    return rk
	    
def ready_for_round(c1,d1):
    lst = c1 + d1
    print(len(lst))
    print(len(pc2))
  #  print(lst)
    v1 = compression_p2(lst, rk =[])
    print( v1)
    return v1
		
  #  print(c1,d1)
#rint(rk, "<-", len(rk))

#print (C0, D0)
#print(key_div(rk))


if __name__ == '__main__':
    key = 11243341211333411131
    key_start(key)




