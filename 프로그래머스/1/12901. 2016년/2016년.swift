func solution(_ a:Int, _ b:Int) -> String {
    let week = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
    let day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    var today = b
    
    for i in 0..<(a-1) {
        today += day[i]
    }
    
    return week[(today+4) % 7]
}