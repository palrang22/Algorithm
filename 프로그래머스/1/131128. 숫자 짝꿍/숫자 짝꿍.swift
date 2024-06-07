import Foundation

func solution(_ X:String, _ Y:String) -> String {
    var dictX : [Character:Int] = [:]
    var dictY : [Character:Int] = [:]
    var arr : [String] = []
    
    for i in X {
        dictX[i, default: 0] += 1
    }
    for i in Y {
        dictY[i, default: 0] += 1
    }
    
    for (key,valX) in dictX {
        if let valY = dictY[key] {
            arr.append(String(repeating:key, count:min(valX, valY)))
        }
    }
    
    let returnArr = arr.joined(separator:"")
    
    if returnArr.count == 0 {
        return "-1"
    } else if Set(returnArr) == ["0"] {
        return "0"
    } else {
        return String(returnArr.sorted(by: >))
    }
}