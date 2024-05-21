import Foundation

func solution(_ a:Int, _ b:Int, _ n:Int) -> Int {
    var coke = n
    var count: Int = 0
    var cokeLeft: Int = 0
    
    while coke > 0 {
        let cokeRecieved = Int(coke / a) * b
        count += cokeRecieved
        cokeLeft += Int(coke % a)
        coke = cokeRecieved
    }
    
    if cokeLeft >= a {
        count += solution(a, b, cokeLeft)
    }
    
    return count
}
