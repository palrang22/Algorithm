func solution(_ a:Int, _ b:Int) -> String {
    let week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    let day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    var today = day.prefix(a-1).reduce(b, +)
    
    return week[(today+4) % 7]
}
