
import Foundation

struct Deque<T> {
    var dequeArray = [T]()
    var enqueArray = [T]()
    var dequeIndex = 0
    var enqueIndex = 0
    
    var isEmpty: Bool {
        return dequeArray.count <= dequeIndex && enqueArray.count <= enqueIndex
    }
    var count: Int {
        return dequeArray.count - dequeIndex + enqueArray.count - enqueIndex
    }
    
    mutating func pushFirst(k: T) {
        dequeArray.append(k)
    }
    mutating func pushLast(k: T) {
        enqueArray.append(k)
    }
    mutating func popFirst() -> T? {
        if isEmpty {
            return nil
        }
        
        if dequeArray.count <= dequeIndex {
            let first = enqueArray[enqueIndex]
            enqueIndex += 1
            return first
        }
        return dequeArray.popLast()
    }
    mutating func popLast() -> T? {
        if isEmpty {
            return nil
        }
        if enqueArray.count <= enqueIndex {
            let last = dequeArray[dequeIndex]
            dequeIndex += 1
            return last
        }
        return enqueArray.popLast()
    }
}

let N = Int(readLine()!)!
let nums = readLine()!.split(separator: " ").compactMap { Int($0) }
var deque = Deque<(Int, Int)>()

for (index, value) in nums.enumerated() {
    deque.pushLast(k: (index + 1, value))
}

var result: [String] = []

while !deque.isEmpty {
    let (idx, count) = deque.popFirst()!
    result.append("\(idx)")

    if deque.isEmpty { break }

    if count > 0 {
        for _ in 0..<(count - 1) {
            if let item = deque.popFirst() {
                deque.pushLast(k: item)
            }
        }
    } else {
        for _ in 0..<(-count) {
            if let item = deque.popLast() {
                deque.pushFirst(k: item)
            }
        }
    }
}

print(result.joined(separator: " "))
