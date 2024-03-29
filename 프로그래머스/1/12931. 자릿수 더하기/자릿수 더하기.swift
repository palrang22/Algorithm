import Foundation

func solution(_ n:Int) -> Int
{
    let num = String(n).compactMap{Int(String($0))}
    
    return num.reduce(0,+)
}