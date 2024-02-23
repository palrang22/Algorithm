let input = readLine()!
let numbers = input.split(separator: " ").compactMap{Int($0)}
let (a, b) = (numbers[0], numbers[1])

if b >= 45 {
    print(a, b-45)
} else {
    if a == 0 {
        print(23, b+15)
    } else{
        print(a-1, b+15)
    }
}