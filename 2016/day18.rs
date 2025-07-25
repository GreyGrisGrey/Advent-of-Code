use std::fs;

fn main() {
    println!("Part 2: {}", part_both());
}

fn step(start: &str) -> String {
    let mut end: String = "".to_owned();
    for i in 0..start.len() {
        if i == 0 {
            if start.chars().nth(1).unwrap() == '.' {
                end.push_str(".");
            } else {
                end.push_str("^");
            }
        } else if i == start.len() - 1 {
            if start.chars().nth(start.len() - 2).unwrap() == '.' {
                end.push_str(".");
            } else {
                end.push_str("^");
            }
        } else {
            if (start.chars().nth(i + 1).unwrap() == '.'
                && start.chars().nth(i - 1).unwrap() != '.')
            {
                end.push_str("^");
            } else if (start.chars().nth(i + 1).unwrap() != '.'
                && start.chars().nth(i - 1).unwrap() == '.')
            {
                end.push_str("^")
            } else {
                end.push_str(".");
            }
        }
    }
    return end;
}

fn part_both() -> i32 {
    let line = fs::read_to_string("in.txt").unwrap();
    let mut curr = line.clone();
    let mut count = 0;
    let mut done_flag = false;
    for i in 0..400000 {
        if i == 40 {
            println!("Part 1: {}", count);
        }
        done_flag = true;
        for j in curr.chars() {
            if j == '.' {
                count += 1;
            } else {
                done_flag = false;
            }
        }
        curr = step(&curr);
    }
    return count;
}
