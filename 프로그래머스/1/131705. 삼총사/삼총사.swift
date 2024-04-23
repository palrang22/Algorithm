import Foundation

func solution(_ number:[Int]) -> Int {
    var newarr = number
    var removed = newarr.remove(at: 0)
    var totalCount = 0
    
    while newarr.count > 1 {
        totalCount += twopointer(newarr, removed)
        removed = newarr.remove(at: 0)
    }
    
    return totalCount
}

func twopointer(_ arr:[Int], _ target: Int) -> Int {
    var pointerCount = 0
    var left = 0
    var right = arr.count - 1
    
    while left < arr.count - 1 {
    
        while left < right {
            if (target + arr[left] + arr[right]) == 0 {
                pointerCount += 1
            }
            right -= 1
        }
        
        left += 1
        right = arr.count - 1
    }
    
    return pointerCount
    
}