import Foundation

func solution(_ s:String) -> [Int] {
    var letterDict: [Character: Int] = [:]
    var newArr: [Int] = []
    var letterArr = Array(s)
    
    for (idx, char) in letterArr.enumerated() {
        if let letterIdx = letterDict[char] {
            newArr.append(idx-letterIdx)
        } else {
            letterDict[char] = -1
            newArr.append(-1)
        }
        letterDict[char] = idx
    }
    
    return newArr
}