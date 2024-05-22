import Foundation

func solution(_ cards1:[String], _ cards2:[String], _ goal:[String]) -> String {
    var pOne = 0
    var pTwo = 0
    
    for i in goal {
        if pOne < cards1.count && i == cards1[pOne] {
            pOne += 1
        } else if pTwo < cards2.count && i == cards2[pTwo] {
            pTwo += 1
        } else {
            return "No"
        }
    }
    
    return "Yes"
}