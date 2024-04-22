import Foundation

func solution(_ s:String) -> String {

    let copys = Array(s)
    var newarr : [String] = []
    var count = 0
    for i in copys {
        
        if count % 2 == 0 {
            newarr.append(i.uppercased())
        } else {
            newarr.append(i.lowercased())
        }
        count += 1
        
        if i == " " { count = 0 }
        
    }
    
    return newarr.joined()
}