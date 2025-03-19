import Foundation

var n = Int(readLine()!)!
var count = 0
var currentNum = 665

func check666(_ N: Int) -> Bool {
    var N = N
    while N >= 666 {
        if N % 1000 == 666 {
            return true
        }
        N /= 10
    }
    return false
}

while n > count {
    currentNum += 1
    if check666(currentNum) {
        count += 1
    }
}

print(currentNum)
