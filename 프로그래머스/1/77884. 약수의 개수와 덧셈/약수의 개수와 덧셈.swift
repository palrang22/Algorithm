import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    var newl = sqrt(Double(left))
    let newr = sqrt(Double(right))
    var sum = (right+left)*(right-left+1)/2
    if newl.truncatingRemainder(dividingBy: 1) == 0 {
        for i in Int(newl)...Int(newr) {
            sum -= Int(pow(Double(i),2))*2
        }
    } else {
        for i in (Int(newl)+1)...Int(newr) {
            sum -= Int(pow(Double(i),2))*2
        }
    }
    return sum
}