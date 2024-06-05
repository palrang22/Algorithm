import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var base: Int
    var high: Int
    var lottoArr = lottos
    var winArr = win_nums
    
    let rightNum = lottoArr.filter {winArr.contains($0)}
    
    base = rightNum.count > 1 ? 7-rightNum.count : 6
    
    lottoArr = lottoArr.filter {$0 == 0}
    high = base - lottoArr.count
    if high == 0 { high = 1 }
    
    return [high, base]
}