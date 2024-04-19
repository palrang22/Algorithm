func solution(_ n:Int, _ m:Int) -> [Int] {
    return [gcd(n, m), n*m/gcd(n,m)]
}

func gcd(_ x: Int, _ y: Int) -> Int {
    var a = x
    var b = y
    var c = 0
    while true {
        c = b
        b = a%b
        a = c
        if b == 0 {
            return c
        }
    }
}