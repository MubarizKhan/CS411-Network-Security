from itertools import permutations
co = []
do= []
pc1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,
        10,2,59,51,43,35,27,19,11,3,60,52,44,36,
        63,55,47,39,31,23,15,7,62,54,46,38,30,22,
        14,6,61,53,45,37,29,21,13,5,28,20,12,4]
    

def key_start():
    #this is dividing permuted computation, c0, d0
    for i in range(len(pc1)):
        if i < len(pc1) / 2:
             co.append(pc1[i])
        else:
            do.append(pc1[i])
        

key = 11243341211333411131

if key.bit_length() < 64:
    print("no")
elif key.bit_length() == 64:
    print("yes")

print(key.bit_length())
keyb = bin(key)

print(keyb,"<BIN")
print(len(keyb), "<")

ls = []
for i in range(len(keyb)):
#this loop is converting keyb into the list form for easier mainupluatrion
	ls.append(keyb[i])
ls.pop(0)
ls.pop(1)

rk = []
for i in range(len(pc1)):
#this loop-- stores the value at the i'th index in pc1, and puts it in the ith index of the key
   v1 = int(pc1[i])
 #  print(v1)
   rk.append(ls[v1])
  
print(rk, "<-", len(rk))

#print (C0, D0)
#key_start()

