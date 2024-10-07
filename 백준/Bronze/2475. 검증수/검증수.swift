var numbers: [Int] = readLine()!.split(separator: " ").compactMap{ Int($0) }
var sum: Int = 0
for i in numbers {
    sum += i*i
}
print(sum%10)