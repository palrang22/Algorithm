let input = readLine()!
let numbers = input.split(separator: " ").compactMap{Int($0)}
let (a, b) = (numbers[0], numbers[1])
print(a+b)