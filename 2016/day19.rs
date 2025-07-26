use std::fs;

fn main() {
    let num1 = part1();
    let num2 = part2();
    println!("Part 1: {}", num1);
    println!("Part 2: {}", num2);
}

fn part1() -> i32 {
    let mut num = fs::read_to_string("in.txt")
        .unwrap()
        .parse::<i32>()
        .unwrap();
    let mut total_vec: Vec<i32> = Vec::new();
    for i in 0..num {
        total_vec.push(i + 1);
    }
    let mut size = total_vec.len();
    while size > 1 {
        let mut new_vec: Vec<i32> = Vec::new();
        for i in 0..(size / 2) {
            if size % 2 == 0 {
                new_vec.push(total_vec[2 * i]);
            } else {
                new_vec.push(total_vec[2 * (i + 1)]);
            }
        }
        total_vec = new_vec;
        size = total_vec.len();
    }
    return total_vec[0];
}

fn part2() -> i32 {
    let mut num = fs::read_to_string("in.txt")
        .unwrap()
        .parse::<i32>()
        .unwrap();
    let mut total_vec: Vec<i32> = Vec::new();
    for i in 0..num {
        total_vec.push(i + 1);
    }
    let mut size = total_vec.len();
    let mut curr_step = 0;
    while size > 1 {
        // Takes a while, haven't figured out an analytical solution yet.
        if size % 1000 == 0 {
            println!("{}", size);
        }
        let mut kill_index = curr_step + (size / 2);
        if kill_index >= size {
            kill_index -= size;
        }
        total_vec.remove(kill_index);
        if kill_index > curr_step {
            curr_step += 1;
        }
        size = total_vec.len();
        if (curr_step >= size) {
            curr_step = 0;
        }
    }
    return total_vec[0];
}
