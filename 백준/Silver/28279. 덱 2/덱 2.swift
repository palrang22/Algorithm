//
//  main.swift
//  swiftPlayground
//
//  Created by 김승희 on 6/18/25.
//

import Foundation

// 백준 28279 문제에서는 정수를 사용한다고 나와있지만 그냥 제네릭으로 구현해봤다.
struct Deque<T> {
    // stored property
    var dequeArray = [T]()
    var enqueArray = [T]()
    var dequeIndex = 0
    var enqueIndex = 0
    
    // computed property
    var isEmpty: Bool {
        return dequeArray.count <= dequeIndex && enqueArray.count <= enqueIndex
    }
    
    var count: Int {
        return dequeArray.count - dequeIndex + enqueArray.count - enqueIndex
    }
    
    var first: T? {
        if isEmpty { return nil }
        
        if dequeArray.count <= dequeIndex {
            return enqueArray[enqueIndex]
        }
        return dequeArray.last
    }
    
    var last: T? {
        if isEmpty { return nil }
        
        if enqueArray.count <= enqueIndex {
            return dequeArray[dequeIndex]
        }
        return enqueArray.last
    }
    
    // push
    mutating func pushFirst(k: T) {
        dequeArray.append(k)
    }
    
    mutating func pushLast(k: T) {
        enqueArray.append(k)
    }
    
    // pop
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


enum DequeCase: Int {
    case pushFirst = 1
    case pushLast = 2
    case popFirst = 3
    case popLast = 4
    case printCount = 5
    case isEmpty = 6
    case printFirst = 7
    case printLast = 8
}

var deque = Deque<Int>()
let count = Int(readLine()!)!

for _ in 0..<count {
    let input = readLine()!.split(separator: " ").map { String($0) }
    guard let command = Int(input[0]), let commandCase = DequeCase(rawValue: command) else { continue }
    
    switch commandCase {
    case .pushFirst:
        guard let value = Int(input[1]) else { continue }
        deque.pushFirst(k: value)
    case .pushLast:
        guard let value = Int(input[1]) else { continue }
        deque.pushLast(k: value)
    case .popFirst:
        print(deque.popFirst() ?? -1)
    case .popLast:
        print(deque.popLast() ?? -1)
    case .printCount:
        print(deque.count)
    case .isEmpty:
        print(deque.isEmpty ? 1 : 0)
    case .printFirst:
        print(deque.first ?? -1)
    case .printLast:
        print(deque.last ?? -1)
    }
}
