import Foundation

while true {
    let num = readLine()
    guard let num = num else { break }
    
    if num == "0" {
        break
    }
    
    var reversedNum = ""
    for i in num.reversed() {
        reversedNum += String(i)
    }
    
    if num == reversedNum {
        print("yes")
    } else {
        print("no")
    }
}
