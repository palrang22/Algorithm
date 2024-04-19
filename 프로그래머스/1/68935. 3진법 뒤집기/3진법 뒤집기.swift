import Foundation

func solution(_ n:Int) -> Int {
    return(tertodeci(ternaryrev(n)))
}

func ternaryrev(_ x: Int) -> [Int] {
    var num = x
    var trev: [Int] = []
    while true {
        trev.append(num%3)
        num = num / 3
        if num == 0 {
            return trev
        }
    }
}

func tertodeci(_ m: [Int]) -> Int{
    let tarnary = m
    let cnt: Int = m.count
    var deci: Int = 0
    for i in 1...cnt {
        deci += tarnary[i-1] * Int(pow(3.0, Double((cnt-i))))
    }
    return deci
}