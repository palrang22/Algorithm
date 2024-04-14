func solution(_ s:String) -> String {
    return Array(s).sorted(by: >).compactMap{String($0)}.joined()
}