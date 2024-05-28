import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let qlen = answers.count
    var ansFst: [Int] = []
    var ansSec: [Int] = []
    var ansTrd: [Int] = []
    var scoreFst = 0
    var scoreSec = 0
    var scoreTrd = 0
    var returnScore: [Int] = []
    
    while ansFst.count < qlen {
        for i in [1, 2, 3, 4, 5] {
            ansFst.append(i)
        }
    }
    
    while ansSec.count < qlen {
        for i in [1, 3, 4, 5] {
            ansSec.append(2)
            ansSec.append(i)
        }
    }
    
    while ansTrd.count < qlen {
        for i in [3, 1, 2, 4, 5] {
                ansTrd.append(i)
                ansTrd.append(i)
            }
    }
    
    ansFst = Array(ansFst.prefix(qlen))
    ansSec = Array(ansSec.prefix(qlen))
    ansTrd = Array(ansTrd.prefix(qlen))
    
    for i in 0..<answers.count {
        if ansFst[i] == answers[i] {
            scoreFst += 1
        }
        if ansSec[i] == answers[i] {
            scoreSec += 1
        }
        if ansTrd[i] == answers[i] {
            scoreTrd += 1
        }
    }
    
    let maxScore = max(scoreFst, scoreSec, scoreTrd)
    if scoreFst == maxScore {
        returnScore.append(1)
    }
    if scoreSec == maxScore {
        returnScore.append(2)
    }
    if scoreTrd == maxScore {
        returnScore.append(3)
    }
    
    return returnScore
}