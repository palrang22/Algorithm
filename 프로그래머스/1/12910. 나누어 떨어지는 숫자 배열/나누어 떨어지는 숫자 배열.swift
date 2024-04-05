func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    var newarr: [Int] = []
    for i in arr {
        if i % divisor == 0 {
            newarr.append(i)
        }
    }
    return newarr.count == 0 ? [-1] : newarr.sorted(by:<)
}