gradecard = []
scorelist = []
secondlowgrades = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    scorelist.append(score)
    gradecard.append([name, score])

flag = True
token = min(scorelist)
while flag:   
    if min(scorelist) == token:
        scorelist.remove(min(scorelist))
        print(scorelist)
    else:
        flag = False

print(scorelist)
for i in gradecard:
    if i[1] == min(scorelist):
        secondlowgrades.append(i[0])

secondlowgrades.sort()
print("\n".join(secondlowgrades), end = "")


    
