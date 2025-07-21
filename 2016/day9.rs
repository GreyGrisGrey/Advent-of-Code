use std::fs;

fn main() {
    part1();
    part2();
}

fn part1() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut count = 0;
    let mut size = 0;
    let mut skip = 0;
    let mut skip_flag = false;
    let mut skip_size = 0;
    let mut start_skip = 0;
    let mut skip_count_start = 0;
    while count < data.len(){
        if !skip_flag {
            size += 1;
        }
        if data.chars().nth(count) == Some(')') && skip_flag {
            skip_flag = false;
            size += (*&data[skip_count_start..count].parse::<usize>().unwrap()) * skip_size;
            count += skip_size;
        } else if data.chars().nth(count) == Some('(') {
            skip_flag = true;
            size -= 1;
            start_skip = count;
        } else if skip_flag && data.chars().nth(count) == Some('x') {
            skip_size = *&data[start_skip+1..count].parse::<usize>().unwrap();
            skip_count_start = count + 1;
        }
        count += 1;
    }
    println!("{}", size.to_string());
}

fn part2() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut count = 0;
    let mut size = 0;
    let mut skip = 0;
    let mut steps = 0;
    let mut skip_flag = false;
    let mut skip_size = 0;
    let mut start_skip = 0;
    let mut skip_count_start = 0;
    let mut mult = 1;
    let mut mult_sizes: Vec<usize> = Vec::new();
    let mut mult_steps: Vec<usize> = Vec::new();
    while count < data.len(){
        if data.chars().nth(count) == Some(')') && skip_flag {
            skip_flag = false;
            let mut num = 0;
            if mult != 1 {
                num = mult;
            }
            mult *= *&data[skip_count_start..count].parse::<usize>().unwrap();
            mult_sizes.push(*&data[skip_count_start..count].parse::<usize>().unwrap());
            mult_steps.push(skip_size);
            if skip_size > steps {
                steps = skip_size;
            }
        } else if data.chars().nth(count) == Some('(') {
            skip_flag = true;
            start_skip = count;
        } else if skip_flag && data.chars().nth(count) == Some('x') {
            skip_size = *&data[start_skip+1..count].parse::<usize>().unwrap();
            skip_count_start = count + 1;
        } else if !skip_flag {
            size += mult;
        }
        for i in 0..mult_steps.len() {
            if mult_steps[i] == 0 {
                mult /= mult_sizes[i];
                mult_sizes[i] = 1;
            } else {
                mult_steps[i] -= 1;
            }
        }
        count += 1;
    }
    println!("{}", size.to_string());
}