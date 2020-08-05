names=[]
scores=[]
total=0
highest=0
lowest=100
C=int(input('輸入人數 :'))
for a in range(C):
    A=input('輸入名字 :')
    B=int(input('輸入分數 :'))
    names.append(A)
    scores.append(B)
for b in range(C):
    total=total+scores[b]
print(total)    
def avg(total,C):
    return total/C
print(avg(total,C))

    
