func solution(_ strings:[String], _ n:Int) -> [String] {
    var newArr: [[String]] = []
    var sortedArr: [String] = []
    for i in strings {
        var newStr = Array(i)
        newArr.append([i, String(newStr[n])])
    }
    
    newArr = newArr.sorted(by:{
        if $0[1] == $1[1] {
            return $0[0] < $1[0]
        } else {
            return $0[1] < $1[1]
        }
    })
    
    for j in newArr {
        sortedArr.append(j[0])
    }
    return sortedArr
}