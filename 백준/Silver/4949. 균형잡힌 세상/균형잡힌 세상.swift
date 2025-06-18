
import Foundation

enum bracketCase: Character {
    case smallLeft = "("
    case smallRight = ")"
    case bigLeft = "["
    case bigRight = "]"
    case finish = "."
}

while true {
    var inputArray = [Character]()
    var isValid: Bool = true
    
    if let sentence = readLine() {
        if sentence == "." { break }
        
        for i in sentence {
            
            switch bracketCase(rawValue: i) {
            case .smallLeft, .bigLeft:
                inputArray.append(i)
                
            case .smallRight:
                if inputArray.last == "(" {
                    inputArray.removeLast()
                } else {
                    isValid = false
                    break
                }
                
            case .bigRight:
                if inputArray.last == "[" {
                    inputArray.removeLast()
                } else {
                    isValid = false
                    break
                }
                
            case .finish:
                break
                
            default:
                continue
            }
            
            if !isValid { break }
        }
        isValid && inputArray.isEmpty ? print("yes") : print("no")
    }
}
