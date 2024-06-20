import Foundation

func solution(_ today:String, _ terms:[String], _ privacies:[String]) -> Any {
    var termsDict = [String:Int]()
    var modPv = [[String]]()
    let modToday = today.split(separator:".").compactMap{Int(String($0))}
    
    for i in terms {
        let rawTerms = i.split(separator:" ")
        termsDict[String(rawTerms[0])] = Int(rawTerms[1])
    }
    
    for i in privacies {
        let raw = i.split(separator:" ")
        let dateRaw = raw[0].split(separator: ".").map{String($0)}
        modPv.append(dateRaw + [String(raw[1])])
    }
    
    for (idx, i) in modPv.enumerated() {
    
        var newYear = Int(i[0])!
        var newMonth = Int(i[1])!
        var newDate = Int(i[2])!
        
        newMonth += termsDict[i[3]]!
        newDate -= 1
        
        if newDate == 0 {
            newMonth -= 1
            newDate = 28
        }
        
        if newMonth > 12 {
            newYear += newMonth / 12
            newMonth = newMonth % 12
        }
        
        if newMonth == 0 {
            newYear -= 1
            newMonth = 12
        }
        
        modPv[idx][0] = String(newYear)
        modPv[idx][1] = String(newMonth)
        modPv[idx][2] = String(newDate)
    }
    
    let endDate = changeDateToInt(modPv)
    
    var checkDate = [Int]()
    var count = 1
    for i in endDate {
        print(modToday, i)
        if compareDate(modToday, i) {
            checkDate.append(count)
        }
        count += 1
    }
    
    return checkDate
}

func changeDateToInt(_ modPv: [[String]]) -> [[Int]] {
    var returnArr = [[Int]]()
    for i in modPv {
        returnArr.append(i.compactMap{Int($0)})
    }
    return returnArr
}

func compareDate(_ modToday: [Int], _ eachEndDate: [Int]) -> Bool {
    for i in 0..<modToday.count {
        if modToday[i] < eachEndDate[i] {
            return false
        } else if modToday[i] > eachEndDate[i] {
            return true
        }
    }
    return false
}