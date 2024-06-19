import Foundation

func solution(_ survey:[String], _ choices:[Int]) -> String {
    var psDict: [Character:Int] = ["A":0, "N":0, "C":0, "F":0, "M":0, "J":0, "R":0, "T":0]
    let newChoices = replaceScore(choices)
    for j in newChoices {
        if j[2] == 0 { continue }
        let idx = j[0]
        let type = Array(survey[idx])[j[1]]
        psDict[type]! += j[2]
    }
    return calculateType(psDict)
}

func calculateType(_ psDict: [Character:Int]) -> String {
    var returnStr = ""
    
    returnStr += psDict["R"]! >= psDict["T"]! ? "R" : "T"
    returnStr += psDict["C"]! >= psDict["F"]! ? "C" : "F"
    returnStr += psDict["J"]! >= psDict["M"]! ? "J" : "M"
    returnStr += psDict["A"]! >= psDict["N"]! ? "A" : "N"
    
    return returnStr
}

func replaceScore(_ choices: [Int]) -> [[Int]] {
    var returnArr: [[Int]] = []
    for (idx, i) in choices.enumerated() {
        if i <= 3 {
            returnArr.append([idx, 0, 4-i])
        } else if i == 4 {
            returnArr.append([idx, 0, 0])
        } else {
            returnArr.append([idx, 1, i-4])
        }
    }
    return returnArr
}