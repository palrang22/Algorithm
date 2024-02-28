let N = Int(readLine()!)!

for i in stride(from: N, through: 1, by: -1) {
    var star = String(repeating:"*", count:i)
    print(star)
}
