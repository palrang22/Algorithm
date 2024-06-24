import Foundation

func solution(_ s:String) -> String {
    var intArr = [Int]()
    for i in s.split(separator:" ") {
        if let num = Int(i) {
            intArr.append(num)
        }
    }
    return String(intArr.min()!) + " " + String(intArr.max()!)
}