import Foundation

func solution(_ n: Int) -> Int {

    guard n > 1 else {
        return n
    }

    var divisors = Set<Int>()

    for divisor in 1...Int(sqrt(Double(n))) {
        if n % divisor == 0 {
            divisors.insert(divisor)
            divisors.insert(n / divisor)
        }
    }
    return divisors.reduce(0, +)
}