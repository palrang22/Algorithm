import Foundation

func solution(_ s:String, _ skip:String, _ index:Int) -> String {
    let skipArr = Array(skip)
    let alpArr = (97...122).map{Character(UnicodeScalar($0))}.filter{ !skipArr.contains($0) }
    let alpCount = alpArr.count
    let alpDict = Dictionary(uniqueKeysWithValues: zip(alpArr, (1...alpArr.count)))
    let revDict = Dictionary(uniqueKeysWithValues: zip((1...alpArr.count), alpArr))
    
    let sArr = Array(s).map{alpDict[$0]!+index > alpCount ? (alpDict[$0]!+index) % alpCount == 0 ? alpCount : (alpDict[$0]!+index) % alpCount : alpDict[$0]!+index}
    
    return sArr.map{String(revDict[$0]!)}.joined(separator: "")
}