group_credit = []
group_grade = []

for i in range(20):
  classname, credit, grade = map(str, input().split())
  group_credit.append(credit)
  group_grade.append(grade)

for j in range(20):
  if group_grade[j] == 'A+':
    group_grade[j] = 4.5
  elif group_grade[j] == 'A0':
    group_grade[j] = 4.0
  elif group_grade[j] == 'B+':
    group_grade[j] = 3.5
  elif group_grade[j] == 'B0':
    group_grade[j] = 3.0
  elif group_grade[j] == 'C+':
    group_grade[j] = 2.5
  elif group_grade[j] == 'C0':
    group_grade[j] = 2.0
  elif group_grade[j] == 'D+':
    group_grade[j] = 1.5
  elif group_grade[j] == 'D0':
    group_grade[j] = 1.0
  elif group_grade[j] == 'F':
    group_grade[j] = 0.0
  else:
    group_grade[j] = 10

group_credit = list(map(float, group_credit))
sum_credit = 0
for i in group_credit:
  sum_credit += i
score = 0

for c, g in zip(group_credit, group_grade):
  if g == 10:
    sum_credit -= c
  else:
   score += (c * g)

print(score / sum_credit)