func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    let arrcnt1 = arr1.count
    let arrcnt2 = arr1[0].count
    var newarr = [[Int]](repeating:[Int](repeating:0, count: arrcnt2), count: arrcnt1)
    for i in 0..<arrcnt1 {
        for j in 0..<arrcnt2 {
            newarr[i][j] = (arr1[i][j]+arr2[i][j])
        }
    }
    return newarr
}