import Foundation

func solution(_ wallpaper:[String]) -> [Int] {
    var changeToIdx = [[(Int, Int)]]()
    for (idx, i) in wallpaper.enumerated() {
        changeToIdx.append(Array(i).enumerated().filter{$0.element == "#"}.map{($0.offset, idx)})
    }
    var joinedArr = Array(changeToIdx.joined())
    
    var returnArr = [Int]()
    
    returnArr.append(joinedArr.map{$0.1}.min()!)
    returnArr.append(joinedArr.map{$0.0}.min()!)
    returnArr.append(joinedArr.map{$0.1}.max()!+1)
    returnArr.append(joinedArr.map{$0.0}.max()!+1)
    
    return returnArr
}
