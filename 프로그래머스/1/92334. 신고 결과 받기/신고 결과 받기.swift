import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> Any {
    var reportDict = [String:[String]]()
    id_list.forEach{i in reportDict[i] = []}
    
    var newReport = report.map{$0.split(separator:" ").map{String($0)}}
    newReport.forEach{i in reportDict[i[1]]!.append(i[0])}
    
    var returnDict = [String:Int]()
    id_list.forEach{i in returnDict[i] = 0}
    
    for i in id_list {
        if let reports = reportDict[i] {
            let reported = Array(Set(reports))
            if reported.count >= k {
                reported.forEach{i in returnDict[i]! += 1}
            }
        }
    }
    
    var returnArr = [Int]()
    for i in id_list {
        if let j = returnDict[i] {
            returnArr.append(j)
        }
    }
    
    return returnArr
}