use std::fs;

fn main() {
    part1();
    part2();
}

fn checkValid(nums : [i32; 3]) -> bool {
    if !(nums[0] + nums[1] <= nums[2] || nums[1] + nums[2] <= nums[0] || nums[0] + nums[2] <= nums[1]) {
        return true;
    }
    return false;
}

fn part1() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut total = 0;
    for i in data.split("\n") {
        let mut flag1 = true;
        let mut flag2 = true;
        let mut nums: [i32; 3]= [0, 0, 0];
        for j in i.split(" ") {
            if j != "" && flag1 {
                flag1 = false;
                nums[0] = j.parse::<i32>().unwrap();
            } else if j != "" && flag2 {
                flag2 = false;
                nums[1] = j.parse::<i32>().unwrap();
            } else if j != "" {
                nums[2] = j.trim().parse::<i32>().unwrap();
            }
        }
        if checkValid(nums) {
            total += 1;
        }
    }
    println!("{}", total);
}

fn part2() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut total = 0;
    let mut step = 0;
    let mut nums1: [i32; 3]= [0, 0, 0];
    let mut nums2: [i32; 3]= [0, 0, 0];
    let mut nums3: [i32; 3]= [0, 0, 0];
    for i in data.split("\n") {
        let mut flag1 = true;
        let mut flag2 = true;
        for j in i.split(" ") {
            if j != "" && flag1 {
                flag1 = false;
                nums1[step] = j.parse::<i32>().unwrap();
            } else if j != "" && flag2 {
                flag2 = false;
                nums2[step] = j.parse::<i32>().unwrap();
            } else if j != "" {
                nums3[step] = j.trim().parse::<i32>().unwrap();
            }
        }
        step += 1;
        if step == 3 {
            step = 0;
            if checkValid(nums1) {total += 1}
            if checkValid(nums2) {total += 1}
            if checkValid(nums3) {total += 1}
            for i in 0..3{
                nums1[i] = 0;
                nums2[i] = 0;
                nums3[i] = 0;
            }
        }
    }
    println!("{}", total);
}