import Foundation

func solution(_ k: Int, _ m: Int, _ score: [Int]) -> Int {
    var newScore = score
    var cost = 0
    newScore = newScore.filter { $0 <= k }.sorted(by: >)
    
    let boxCount = newScore.count / m
    
    for i in 0..<boxCount {
        let boxMinValue = newScore[(i * m) + (m - 1)]
        cost += boxMinValue * m
    }
    
    return cost
}