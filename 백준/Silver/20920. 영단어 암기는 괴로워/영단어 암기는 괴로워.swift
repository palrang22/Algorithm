import Foundation

let nm = readLine()!.split(separator: " ").map { Int($0)! }
let n = nm[0]
let m = nm[1]

var wordDict: [String: Int] = [:]

for _ in 0..<n {
    let word = readLine()!
    if word.count < m { continue}
    wordDict[word, default: 0] += 1
}

let sortedWords = wordDict.sorted { a, b in
    if a.value != b.value {
        return a.value > b.value
    }
    
    if a.key.count != b.key.count {
        return a.key.count > b.key.count
    }
    
    return a.key < b.key
}

var output = ""
for (word, _) in sortedWords {
    output += word + "\n"
}

print(output)
