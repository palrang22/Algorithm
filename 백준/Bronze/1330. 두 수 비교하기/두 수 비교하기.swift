
let input = readLine()!
let numbers = input.split(separator: " ").compactMap{Int($0)}
let (a, b) = (numbers[0], numbers[1])

if a > b {
    print(">")
} else if a == b {
    print("==")
} else {
    print("<")
}
