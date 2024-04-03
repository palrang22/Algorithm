import Foundation

func solution(_ n:Int64) -> Int64 {
    
    let num = sqrt(Double(n))
    return num.truncatingRemainder(dividingBy: 1) == 0 ? Int64(pow((num+1),2)) : -1
}