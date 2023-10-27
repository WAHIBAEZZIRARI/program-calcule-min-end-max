def Max(Tab):
    return max(Tab)
def Min(Tab):
    return min(Tab)
def inverse(Tab):
    T1=[] 
    for i in range (3,-2,-1):
        T1.append(Tab[i])
        return T1
T=[]
for i in range (0,4):
    T.append (float(input(f"donner element de la case {i+1}:")))

print(Max(T))
print(Min(T))
print(inverse(T))