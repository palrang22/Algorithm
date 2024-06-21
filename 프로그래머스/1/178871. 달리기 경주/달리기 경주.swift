import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {
    var runDict = [String:Int]()
    var newRun = players
    newRun.enumerated().forEach { (idx, i) in runDict[i] = idx }
    
    
    for i in callings {
        let newRank = runDict[i]! - 1
        if newRank >= 0 {
            (newRun[newRank], newRun[newRank+1]) = (i, newRun[newRank])
            (runDict[i], runDict[newRun[newRank+1]]) = (newRank, newRank + 1)
        }
    }
    return newRun
}