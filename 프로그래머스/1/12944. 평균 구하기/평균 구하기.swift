func solution(_ arr:[Int]) -> Double {
    let sum = Double(arr.reduce(0,+))
    let len = Double(arr.count)
    return sum / len
}