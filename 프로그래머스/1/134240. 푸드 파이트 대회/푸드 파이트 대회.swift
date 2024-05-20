import Foundation

func solution(_ food:[Int]) -> String {
    var newArr: [String] = []
    
    for (idx, num) in food.enumerated() {
        if idx == 0 {
            continue
        } else {
            newArr.append(String(repeating: String(idx), count: Int(num / 2)))
        }
    }
    
    let reversedArr = newArr.reversed()
    
    return newArr.joined() + "0" + reversedArr.joined()
}