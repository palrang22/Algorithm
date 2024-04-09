func solution(_ s:String) -> String {
    let strlen = s.count
    if strlen % 2 == 0 {
        let startIdx = s.index(s.startIndex, offsetBy: (strlen / 2) - 1)
        let endIdx = s.index(s.startIndex, offsetBy: (strlen / 2) + 1)
        return String(s[startIdx..<endIdx])
    } else {
        let midIdx = s.index(s.startIndex, offsetBy: strlen / 2)
        return String(s[midIdx])
    }
}
