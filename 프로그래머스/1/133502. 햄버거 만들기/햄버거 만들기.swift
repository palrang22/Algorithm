import Foundation

func solution(_ ingredient:[Int]) -> Int {
    var burgerStack = [Int]()
    var returnCount = 0
    for i in ingredient {
        burgerStack.append(i)
        
        if burgerStack.count >= 4 {
            let cnt = burgerStack.count
            if burgerStack[cnt-4] == 1 && burgerStack[cnt-3] == 2 && burgerStack[cnt-2] == 3 && burgerStack[cnt-1] == 1 {
                returnCount += 1
                    burgerStack.removeLast(4)
            }
        }
    }
    return returnCount
}
