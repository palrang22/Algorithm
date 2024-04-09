func solution(_ s:String) -> String {
    let strlen = s.count
    if strlen % 2 == 0 {
        return String(Array(s)[(strlen/2 - 1)...strlen/2])
    } else {
        return String(Array(s)[strlen/2])
    }
}
