use std::fs;
use std::collections::HashMap;

fn main() {
    part1();
    part2();
}

fn part1() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut total = 0;
    for i in data.split("\n") {
        let mut flag1 = false;
        let mut flag2 = true;
        let mut flag3 = false;
        for j in 0..i.len()-4 {
            if i.as_bytes()[j] == '[' as u8 {
                flag3 = true;
            } else if i.as_bytes()[j] == ']' as u8 {
                flag3 = false;
            }
            if i.as_bytes()[j] == i.as_bytes()[j+3] && i.as_bytes()[j+1] == i.as_bytes()[j+2] && i.as_bytes()[j+1] != i.as_bytes()[j] {
                if flag3 {
                    flag2 = false;
                } else {
                    flag1 = true;
                }
            }
        }
        if flag1 && flag2 {
            total += 1;
        }
    }
    println!("{}", total);
}

fn part2() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut total = 0;
    for i in data.split("\n") {
        let mut outer_map : HashMap<i32, bool> = HashMap::new();
        let mut inner_map : HashMap<i32, bool> = HashMap::new();
        let mut flag1 = false;
        let mut flag2 = false;
        for j in 0..i.len()-2 {
            if i.as_bytes()[j] == '[' as u8 {
                flag1 = true;
            } else if i.as_bytes()[j] == ']' as u8 {
                flag1 = false;
            }
            if (i.as_bytes()[j] == i.as_bytes()[j+2]) && (i.as_bytes()[j+1] != i.as_bytes()[j]) {
                if flag1 {
                    inner_map.insert((i.as_bytes()[j] as i32) + (i.as_bytes()[j+1] as i32 * 1000), true);
                } else {
                    outer_map.insert((i.as_bytes()[j+1] as i32) + (i.as_bytes()[j] as i32 * 1000), true);
                }
            }
        }
        for j in &outer_map {
            if inner_map.contains_key(j.0){
                flag2 = true;
            }
        }
        if flag2 {
            total += 1;
        }
    }
    println!("{}", total);
}