
n = int(input())
sum = 0
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
target_list = student_marks.get(query_name)

for ele in target_list:
    sum += ele

res = sum/len(target_list)
format_res = "{:.2f}".format(res)
print(format_res)



