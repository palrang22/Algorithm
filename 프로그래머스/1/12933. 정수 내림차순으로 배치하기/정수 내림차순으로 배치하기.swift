func solution(_ n:Int64) -> Int64 {
    var strnum = String(n)
    let sortedStrnum =  strnum.compactMap{String($0)}.sorted(by:>).joined()
    return Int64(sortedStrnum) ?? 0
}