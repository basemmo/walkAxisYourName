Walk Axis:
 
C = int(input())
B = []
  
def walkAxis(a):
    return int((((a * a) + a) / 2) + a)
  

for i in range(C):
    B.append(int(input()))

    
for x in B:
    print(walkAxis(x))
    

    
    
    
Your Name:

def married(marry):
    if len(marry[0]) > len(marry[1]):
        first = marry[0]
        second = marry[1]
    elif len(marry[0]) == len(marry[1]):
        if marry[0] == marry[1]:
            vows = 'YES'
        else:
            vows = 'NO'
        
        return vows
    else:
        first = marry[1]
        second = marry[0]
    
    f, s = 0, 0
    while f < len(second) and s < len(first):
        if second[f] == first[s]:
            f += 1
            s += 1
        else:
            s += 1
    
    if f == len(second):
        vows = 'YES'
    else:
        vows = 'NO'
    
    return vows

  
B = int(input())
B = []


for i in range(B):
    B.append(input().split(" "))

for x in B:
    print(married(x))
    
