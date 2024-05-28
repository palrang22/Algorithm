import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let patterns: [[Int]] = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    var scores: [Int] = [0, 0, 0]
    var returnArr = [Int]()
    
    for (idx, ans) in answers.enumerated() {
        for (patidx, pat) in patterns.enumerated() {
            if ans == pat[idx % pat.count] {
                scores[patidx] += 1
            }
        }
    }
    
    for (idx,score) in scores.enumerated() {
        if score == scores.max() {
            returnArr.append(idx+1)
        }
    }
    
    return returnArr
}