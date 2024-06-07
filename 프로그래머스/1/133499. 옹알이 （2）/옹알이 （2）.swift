import Foundation

func solution(_ babbling: [String]) -> Int {
    let can = ["aya", "ye", "woo", "ma"]
    var newArr = babbling
    var count = 0

    for (idx, i) in newArr.enumerated() {
        var newWord = i
        for (jidx, j) in can.enumerated() {
            newWord = newWord.replacingOccurrences(of:j, with: String(jidx))
        }
        newArr[idx] = newWord
    }
    
    for k in newArr {
        guard let test = Int(k) else {
            continue
        }
        if !k.contains("00") && !k.contains("11") && !k.contains("22") && !k.contains("33") {
            count += 1
        }
    }
    return count
}