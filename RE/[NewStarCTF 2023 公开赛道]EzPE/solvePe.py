data =[
   10,  12,   4,  31,  38, 108,  67,  45,  60,  12, 
   84,  76,  36,  37,  17,   6,   5,  58, 124,  81, 
   56,  26,   3,  13,   1,  54,  31,  18,  38,   4, 
  104,  93,  63,  45,  55,  42, 125
]
for i in range(len(data)-2,-1,-1):
    data[i] = data[i] ^ (i ^ data[i+1])
print("".join(chr(x) for x in data))