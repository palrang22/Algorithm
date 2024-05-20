import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    
    var returnArr : [Int] = []
    
    for miniArr in commands {
        var newArr = Array(array[miniArr[0]-1..<miniArr[1]])
        newArr = newArr.sorted()
        returnArr.append(newArr[miniArr[2]-1])
    }
    
    return returnArr
}