import Foundation

func solution(_ s:String) -> String {
    var returnStr = [String]()
    for i in s.components(separatedBy:" ").map{String($0)} {
        returnStr.append(String(i.prefix(1)).uppercased() + i.lowercased().dropFirst())
    }
    return returnStr.joined(separator:" ")
}