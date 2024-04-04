func solution(_ a:Int, _ b:Int) -> Int64 {
    
    var x = a
    var y = b
    var sum = 0
    
    if x > y {
        (y, x) = (x, y)   
    }
    
    return Int64(((y+x)*(y-x+1))/2)
    
}