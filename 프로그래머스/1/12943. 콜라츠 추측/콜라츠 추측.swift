func solution(_ num: Int) -> Int {
    var count = 0
    var givennum = num
    
    while givennum != 1 {
        if count > 500 {
            return -1
        }
        
        if givennum % 2 == 0 {
            givennum /= 2
        } else {
            givennum = givennum * 3 + 1
        }
        
        count += 1
    }
    
    return count
}
