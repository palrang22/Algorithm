import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    let arrcount = a.count
    var newarr : [Int] = []
    for i in 0..<arrcount {
        newarr.append(a[i]*b[i])
    }
    return newarr.reduce(0,+)
}