import Foundation

func solution(_ number:Int, _ limit:Int, _ power:Int) -> Int {
    var factorCountArr : [Int] = []
    for i in 1...number {
        factorCountArr.append(factorsCount(i))
    }
    for (idx, j) in factorCountArr.enumerated() {
        if j > limit {
            factorCountArr[idx] = power
        }
    }
    
    return factorCountArr.reduce(0,+)
}

func factorsCount(_ x: Int) -> Int {
    var returnCount = 0
    let square = Int(sqrt(Double(x)))
    if x == 1 { return 1 }
    for i in 1...square {
        if x % i == 0 {
            if x / i == i {
                returnCount -= 1
            }
            returnCount += 2
        }
    }
    return returnCount
}