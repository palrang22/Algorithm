import Foundation

func solution(_ s:String) -> Int {
    var newString = s
    let alphabet: [String : String] = ["zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"]
    
    for (k, v) in alphabet {
        newString = newString.replacingOccurrences(of:k, with:v)
    }
    return Int(newString)!
}