func solution(_ n:Int, _ m:Int) -> [Int] {
    let gcdVal = gcd(n, m)
    return [gcdVal, n*m/gcdVal]
}

func gcd(_ x: Int, _ y: Int) -> Int {
    return y == 0 ? x : gcd(y, x%y)
}