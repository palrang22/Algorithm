func solution(_ x:Int, _ n:Int) -> [Int64] {
    
    return Array(1...n).compactMap{Int64(x * $0)}
    
}