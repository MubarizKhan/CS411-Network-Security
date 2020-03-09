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
	v1 = list1[i] ^ list2[i] 
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
	
	print("[*] kp = ",kp)
	
    
    
   
print(len(plaintext))
print(len(IP))

if __name__ == '__main__':
    # key = 11243341211333411131
    #key_start(key)
    initial_permutation()

