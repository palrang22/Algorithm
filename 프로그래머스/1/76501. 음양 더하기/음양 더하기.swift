import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    return (0..<absolutes.count).compactMap{signs[$0] ? absolutes[$0] : -absolutes[$0]}.reduce(0,+)
}