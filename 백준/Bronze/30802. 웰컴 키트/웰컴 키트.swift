import Foundation

let n = readLine()
let clothes = readLine()
let pen = readLine()

func solution() {
    guard let n = n, let clothes = clothes, let pen = pen else { return }
    let N = Int(n)!
    let applicantSize = clothes.split(separator: " ").compactMap{ Int($0) }
    let penList = pen.split(separator: " ").compactMap{ Int($0) }
    let (T, P) = (penList[0], penList[1])
    
    var count = 0
    
    for i in applicantSize {
        if i % T == 0 {
            count += i / T
        } else {
            count += i / T + 1
        }
    }
    
    print(count)
    print(N/P, N%P)
}

solution()