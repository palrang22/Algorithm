sum_cr = 0
sum_score = 0

for i in range(20):
  _, cr, gr = map(str, input().split())

  match gr:
    case 'A+': gr = 4.5
    case 'A0': gr = 4.0
    case 'B+': gr = 3.5
    case 'B0': gr = 3.0
    case 'C+': gr = 2.5
    case 'C0': gr = 2.0
    case 'D+': gr = 1.5
    case 'D0': gr = 1.0
    case 'F': gr = 0

  if gr == 'P':
    continue
  else:
    cr = float(cr)
    sum_cr += cr
    sum_score += cr*gr

print(sum_score / sum_cr)