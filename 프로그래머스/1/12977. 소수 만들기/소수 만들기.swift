import Foundation

func solution(_ nums: [Int]) -> Int {
    var answer = 0
    var comp = [Int]()
    let pn = findPrime(3000)
    
    for i in 0..<nums.count-2 {
        for j in i+1..<nums.count-1 {
            for k in j+1..<nums.count {
                comp.append(nums[i] + nums[j] + nums[k])
            }
        }
    }
    
    for l in comp {
        if pn.contains(l) {
            answer += 1
        }
    }
    
    return answer
}

func findPrime(_ x: Int) -> [Int] {
    var num = [Int](repeating: 1, count: x + 1)
    var primeNum = [Int]()
    
    num[0] = 0
    num[1] = 0
    
    for i in 2...Int(sqrt(Double(x))) {
        if num[i] == 1 {
            for j in stride(from: i * i, through: x, by: i) {
                num[j] = 0
            }
        }
    }
    
    for (idx, isPrime) in num.enumerated() {
        if isPrime == 1 {
            primeNum.append(idx)
        }
    }
    
    return primeNum
}