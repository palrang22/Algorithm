func solution(_ arr:[Int]) -> [Int] {
    var newarr = arr
    if let minIdx = newarr.firstIndex(of: newarr.min()!) {
        newarr.remove(at: minIdx)
    }
    return newarr.count == 0 ? [-1] : newarr
}