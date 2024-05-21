import Foundation

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    var currentScore: [Int] = []
    var returnScore: [Int] = []
    
    for i in score {
        currentScore.append(i)
        currentScore.sort(by: >)
        
        if currentScore.count > k {
            returnScore.append(currentScore[k-1])
        } else {
            returnScore.append(currentScore.last!)
        }
    }
    
    return returnScore
}