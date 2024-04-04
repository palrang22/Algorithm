func solution(_ x:Int) -> Bool {
    let numarr = String(x).compactMap{Int(String($0))}
    return x % (numarr.reduce(0,+)) == 0 ? true : false
}