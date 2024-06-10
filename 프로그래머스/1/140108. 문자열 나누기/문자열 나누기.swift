import Foundation

func solution(_ s:String) -> Int {
    let arr = Array(s)
    let count = arr.count
    var cursor = 0
    var returnCount = 1
    
    
    while cursor < count{
        var letter = arr[cursor]
        var sameCount = 0
        var diffCount = 0
        
        while cursor < count {
            if letter == arr[cursor] {
                sameCount += 1
            } else {
                diffCount += 1
            }
            
            cursor += 1
            
            if sameCount == diffCount {
                if cursor >= count {
                    break
                } else {
                    letter = arr[cursor]
                    returnCount += 1
                    break
                }
            }
        }
    }
    return returnCount
}