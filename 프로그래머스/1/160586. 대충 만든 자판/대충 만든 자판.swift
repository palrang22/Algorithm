import Foundation

func solution(_ keymap:[String], _ targets:[String]) -> [Int] {
    var keyDict = [Character:Int]()
    var returnArr = [Int]()
    
    for i in keymap {
        var keyCount = 1
        for j in Array(i) {
            if let kdict = keyDict[j] {
                keyDict[j] = min(kdict, keyCount)
            } else {
                keyDict[j] = keyCount
            }
            keyCount += 1
        }
    }
    
    for i in targets {
        var returnInt = 0
        for j in Array(i) {
           if let kdict = keyDict[j] {
               returnInt += kdict
           } else {
               returnInt = -1
               break
           }
        }
        returnArr.append(returnInt)
    }
    
    return returnArr
}