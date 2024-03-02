let casenum = Int(readLine()!)!

for _ in 0..<casenum {
    var k = Int(readLine()!)!
    var n = Int(readLine()!)!
    var floor = Array(1...n)
    
    for _ in 0..<k {
        
        for i in 0..<n{
            if i == 0 {
                continue
            } else {
                floor[i] = floor[i] + floor[i-1]
            }
        }
    }
    
    print(floor.last!)
}
