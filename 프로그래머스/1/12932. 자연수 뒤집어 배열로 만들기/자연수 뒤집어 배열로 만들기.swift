func solution(_ n:Int64) -> [Int] {
    var arr = String(n).compactMap{Int(String($0))}
    return arr.reversed()
}