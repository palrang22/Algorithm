func solution(_ n:Int) -> String {
    return n%2 == 0 ? String(repeating: "수박", count: n/2) : String(repeating: "수박", count: n/2) + "수"
}