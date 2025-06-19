import Foundation

let N = Int(readLine()!)!
var vertiLine = [Int]()

var arr = Array(readLine()!.split(separator: " ").map { Int($0)! }.reversed())
var current = 1

while true {
    
    if arr.count == 0 && vertiLine.count == 0 { print("Nice"); break }
    
    if arr.last == current {
        arr.removeLast()
        current += 1
    } else if vertiLine.last == current {
        vertiLine.removeLast()
        current += 1
    } else if let last = arr.last {
        vertiLine.append(last)
        arr.removeLast()
    } else {
        print("Sad")
        break
    }
}
