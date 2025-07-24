use std::fs;

fn main() {
    print!("Part 1: ");
    part_both(272);
    print!("\nPart 2: ");
    part_both(35651584);
}

fn iterate_step(mut start: Vec<char>) -> Vec<char> {
    let mut end: Vec<char> = Vec::new();
    for i in start.clone() {
        end.push(i);
    }
    end.push('0');
    start.reverse();
    for i in start {
        if i == '0' {
            end.push('1');
        } else {
            end.push('0');
        }
    }
    return end;
}

fn checksum(start: Vec<char>, size: usize) -> Vec<char> {
    let mut end: Vec<char> = Vec::new();
    for i in 0..size {
        if start[(2 * i) as usize] == start[((2 * i) + 1) as usize] {
            end.push('1');
        } else {
            end.push('0');
        }
    }
    return end;
}

fn part_both(fill: usize) {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut data_vec: Vec<char> = Vec::new();
    for i in data.chars() {
        if i == '0' {
            data_vec.push('0');
        } else if i == '1' {
            data_vec.push('1');
        }
    }
    let mut num = data_vec.len();
    while num < fill {
        data_vec = iterate_step(data_vec.clone());
        num = data_vec.len();
    }
    while num > fill || (num % 2) == 0 {
        if num > fill {
            num = fill;
        }
        data_vec = checksum(data_vec.clone(), num / 2);
        num = data_vec.len();
    }
    for i in data_vec {
        print!("{}", i);
    }
    return;
}
