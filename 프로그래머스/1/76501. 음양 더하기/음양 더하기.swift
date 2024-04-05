import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    var newarr: [Int] = []
    var newarr2: [Int] = []
    for i in signs {
        if i {
            newarr.append(1)
        } else {
            newarr.append(-1)
        }
    }
    for n in 0..<signs.count {
        newarr2.append(absolutes[n]*newarr[n])
    }
    return newarr2.reduce(0,+)
}