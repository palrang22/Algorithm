import Foundation

func solution(_ s:String) -> Any {
    var newS = s
    var count = 0
    var removedZero = 0
    
    while newS != "1" {
        var currentCount = Array(newS).count
        let newArr = Array(newS).filter{$0 != "0"}
        removedZero += currentCount-newArr.count
        newS = String(newArr.count, radix: 2)
        count += 1
    }
    
    return [count, removedZero]
}