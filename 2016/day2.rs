use std::fs;

fn main() {
    part1();
    println!("\n");
    part2();
}

fn part1() {
    let mut nums = [1, 1];
    let data = fs::read_to_string("in.txt").unwrap();
    for i in data.split("\n"){
        for j in i.chars() {
            if j == 'D' && nums[1] < 2{
                nums[1] += 1
            } else if j == 'U' && nums[1] > 0 {
                nums[1] -= 1
            } else if j == 'R' && nums[0] < 2 {
                nums[0] += 1
            } else if j == 'L' && nums[0] > 0 {
                nums[0] -= 1
            }
        }
        println!("{}, {}", nums[0], nums[1])
    }
}

fn part2() {
    let mut nums = [0, 2];
    let data = fs::read_to_string("in.txt").unwrap();
    for i in data.split("\n"){
        for j in i.chars() {
            if j == 'D' && (nums[1] < 2 || (nums[1] < 3 && nums[0] != 0 && nums[0] != 4) || (nums[1] < 4 && nums[0] == 2)){
                nums[1] += 1
            } else if j == 'U' && (nums[1] > 2 || (nums[1] > 1 && nums[0] != 0 && nums[0] != 4) || (nums[1] > 0 && nums[0] == 2)) {
                nums[1] -= 1
            } else if j == 'R' && (nums[0] < 2 || (nums[0] < 3 && nums[1] != 0 && nums[1] != 4) || (nums[0] < 4 && nums[1] == 2)) {
                nums[0] += 1
            } else if j == 'L' && (nums[0] > 2 || (nums[0] > 1 && nums[1] != 0 && nums[1] != 4) || (nums[0] > 0 && nums[1] == 2)) {
                nums[0] -= 1
            }
        }
        println!("{}, {}", nums[0], nums[1])
    }
}