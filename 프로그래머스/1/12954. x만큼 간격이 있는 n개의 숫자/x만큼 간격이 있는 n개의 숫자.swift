func solution(_ x:Int, _ n:Int) -> [Int] {
    
    var arr : [Int] = []
    
    for i in 1...n {
        arr.append(x*i)
    }
    
    return arr
}