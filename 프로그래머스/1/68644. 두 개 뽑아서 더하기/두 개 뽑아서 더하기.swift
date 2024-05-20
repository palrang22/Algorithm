import Foundation


func solution(_ numbers:[Int]) -> [Int] {

    var newArr = Array(numbers)
    var returnArr : [Int] = []
    let lenArr = newArr.count
    
    for i in 0..<lenArr-1 {
        for j in i+1..<lenArr {
            returnArr.append(newArr[i]+newArr[j])
        }
    }
    
    return Array(Set(returnArr)).sorted()
}