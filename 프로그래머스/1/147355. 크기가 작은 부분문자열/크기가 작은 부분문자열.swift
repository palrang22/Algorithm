import Foundation

func solution(_ t:String, _ p:String) -> Int {
    let numlen : Int = p.count
    let tarr = Array(t)
    let nump = Int(p)!
    var newarr : [Int] = []
    var count = 0
    
    for i in 0...(tarr.count-numlen) {
        var newnum = String(tarr[i..<(i+numlen)])
        newarr.append(Int(newnum)!)
    }
    
    for j in newarr {
        if j <= nump { count+=1 }
    }
    
    return count
}