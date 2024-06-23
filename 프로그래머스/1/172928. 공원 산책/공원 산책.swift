import Foundation

func solution(_ park:[String], _ routes:[String]) -> [Int] {
    var newPark = [[Character]]()
    park.forEach{i in newPark.append(Array(i))}
    var currentIdx = findStartIdx(newPark)
    var directionCount = modifyRoutes(routes)
   
    for i in directionCount {
        var direction = i[0]
        var count = Int(i[1])!
        currentIdx = move(currentIdx, newPark, direction, count)
    }
    
    return currentIdx
}

func findStartIdx(_ newPark: [[Character]]) -> [Int] {
    var yIdx = 0
    var xIdx = 0
    for i in newPark {
        if let xidx = i.firstIndex(of:"S") {
            xIdx = xidx
            break
        } else {
            yIdx += 1
        }
    }
    return [yIdx, xIdx]
}

func modifyRoutes(_ routes: [String]) -> [[String]] {
    var directionCount = routes.map{$0.split(separator:" ").map{String($0)}}
    return directionCount
}

func check(_ currentIdx:[Int], _ newPark: [[Character]], _ direction:String, _ count:Int) -> Bool {
    var y = currentIdx[0]
    var x = currentIdx[1]
    
    for _ in 0..<count {
        switch direction {
        case "E":
            x += 1
            if x >= newPark[0].count || newPark[y][x] == "X" { return false }
        case "W":
            x -= 1
            if x < 0 || newPark[y][x] == "X" { return false }
        case "S":
            y += 1
            if y >= newPark.count || newPark[y][x] == "X" { return false }
        case "N":
            y -= 1
            if y < 0 || newPark[y][x] == "X" { return false }
        default:
            break
        }
    }
    return true
}

func move(_ currentIdx:[Int], _ newPark: [[Character]], _ direction:String, _ count:Int) -> [Int] {
    var y = currentIdx[0]
    var x = currentIdx[1]
    
    if check(currentIdx, newPark, direction, count) {
        switch direction {
        case "E":
            x += count
        case "W":
            x -= count
        case "S":
            y += count
        case "N":
            y -= count
        default:
            break
        }
    }
    return [y, x]
}