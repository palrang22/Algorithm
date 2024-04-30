func solution(_ s:String, _ n:Int) -> String {
    var asciiArr : [Int] = []
    var newArr : [String] = []
    for i in s.utf16 {
        asciiArr.append(Int(i))
    }
    
    for jj in asciiArr {
    
        var j = jj
        
        if 65 <= j && j <= 90 {
            j += n
                if j > 90 {
                    j -= 26
                }
            } else if 97 <= j && j <= 122 {
                j += n
                if j > 122 {
                    j -= 26
                }
            }
        newArr.append(String(UnicodeScalar(j)!))
    }
    return newArr.joined()
}