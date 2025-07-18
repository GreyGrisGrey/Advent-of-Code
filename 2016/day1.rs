use std::fs;

fn main() {
    let mut nums = [0, 0];
    let mut direction = [0, -1];
    let data = fs::read_to_string("in.txt").unwrap();
    let mut vec: Vec<i32> = Vec::new();
    let mut flag = true;
    for i in data.split(", ") {
        if i.chars().nth(0).unwrap().to_string() == "L" {
            let temp = direction[0];
            direction[0] = direction[1];
            direction[1] = -temp;
        } else {
            let temp = direction[0];
            direction[0] = -direction[1];
            direction[1] = temp;
        }
        let mut num = &mut i[1..].parse::<i32>().unwrap();
        while *num > 0 {
            *num -= 1;
            nums[0] += direction[0];
            nums[1] += direction[1];
            if vec.contains(&(nums[0] * 10000 + nums[1])) && flag {
                println!("{}", nums[0].abs() + nums[1].abs());
                flag = false;
            }
            vec.push(nums[0] * 10000 + nums[1]);
        }
    }
    println!("{}", nums[0].abs() + nums[1].abs())
}