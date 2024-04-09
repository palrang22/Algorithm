import Foundation

func solution(_ s:String) -> String {
    let strlen : Int = s.count
    
    if strlen == 1 {
        return s
    }
    
    let strIdx = s.index(s.startIndex, offsetBy: (strlen / 2) - 1)
    let strIdx2 = s.index(s.startIndex, offsetBy: (strlen / 2))
    
    if strlen % 2 == 0 {        
        return String(s[strIdx...strIdx2])
    } else {
        return String(s[strIdx2])
    }
}