import Foundation

func solution(_ numbers:[Int]) -> Double {
    let sum = Double(numbers.reduce(0,+))
    let len = Double(numbers.count)
    return sum / len
}