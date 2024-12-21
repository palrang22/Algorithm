while true {
    var input = readLine()!.split(separator:" ").compactMap{ Int($0) }.sorted()
    let (a, b, c) = (input[0], input[1], input[2])
    
    if input == [0,0,0] {
        break
    }
    
    if (a*a + b*b) == c*c {
        print("right")
    } else {
        print("wrong")
    }
}