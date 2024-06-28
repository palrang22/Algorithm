import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    let sum = brown + yellow
    var returnArr = [Int]()
    
    for i in 1...sum {
        if sum % i == 0 {
            let j = sum / i
            if (i-2)*(j-2) == yellow {
                returnArr.append(max(i, j))
                returnArr.append(min(i, j))
                break
            }
        }
    }
    return returnArr
}