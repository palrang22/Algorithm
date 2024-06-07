import Foundation

func solution(_ babbling: [String]) -> Int {
    let can = ["aya", "ye", "woo", "ma"]
    var count = 0
    
    for word in babbling {
        var tempWord = word
        var lastBabble = ""
        var isValid = true
        
        while !tempWord.isEmpty && isValid {
            var matched = false
            for babble in can {
                if tempWord.hasPrefix(babble) {
                    if lastBabble == babble {
                        isValid = false
                        break
                    } else {
                        tempWord.removeFirst(babble.count)
                        lastBabble = babble
                        matched = true
                        break
                    }
                }
            }
            if !matched {
                isValid = false
            }
        }
        
        if isValid && tempWord.isEmpty {
            count += 1
        }
    }
    return count
}