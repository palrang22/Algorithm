import Foundation

func solution(_ angle:Int) -> Int {
    return angle == 180 ? 4 : angle > 90 ? 3 : angle == 90 ? 2 : 1
}