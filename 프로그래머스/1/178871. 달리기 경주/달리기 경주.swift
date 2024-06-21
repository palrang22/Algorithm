import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var runDict = [String:Int]()
    var newRun = players
    newRun.enumerated().forEach { (idx, i) in runDict[i] = idx }
    
    
    for i in callings {
        let newRank = runDict[i]! - 1
        let playerLose = newRun[newRank]
        if newRank >= 0 {
            newRun.swapAt(newRank, newRank+1)
            (runDict[i], runDict[playerLose]) = (newRank, newRank + 1)
        }
    }
    return newRun
}