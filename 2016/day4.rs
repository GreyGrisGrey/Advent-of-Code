use std::fs;
use std::collections::HashMap;

fn main() {
    part2();
    part1();
}

fn checkLetters(name : &str, checksum : &str) -> bool {
    let mut nums: HashMap<char, i32> = HashMap::new();
    let mut indices: Vec<i32> = Vec::new();
    let mut index = 0;
    for i in name.chars() {
        if i != '-' {
            nums.entry(i).and_modify(|num| *num += 1).or_insert(1);
        }
    }
    for i in nums{
        indices.push((26 - (i.0 as i32 - 97)) + i.1 * 100);
    }
    indices.sort();
    indices.reverse();
    for i in checksum.chars() {
        if i != (((indices[index] % 100) - 26).abs() + 97) as u8 as char {
            return false;
        }
        index += 1;
    }
    return true;
}

fn cutString(line : &str) -> [&str; 3] {
    let mut index = line.len() - 1;
    let mut index2 = 0;
    let line_chars = line.as_bytes();
    while line_chars[index] != '-' as u8 {
        if line_chars[index] == '[' as u8 {
            index2 = index
        }
        index -= 1;
    }
    return [&line[..index], &line[index+1..index2], &line[index2+1..index2+6]]
}

fn decrypt(name : &str, mut count : i32){
    let mut num_vec: Vec<u8> = Vec::new();
    let mut new_string: Vec<char> = Vec::new();
    let original_count = count;
    for i in name.chars() {
        if (i != '-') {
            num_vec.push((i as u8) - 97 as u8);
        } else {
            num_vec.push(100)
        }
    }
    while count > 0 as i32 {
        for i in 0..num_vec.len() {
            if num_vec[i] != 100 {
                num_vec[i] += 1;
            }
            if num_vec[i] == 26 {
                num_vec[i] = 0;
            }
        }
        count -= 1;
    }
    for i in num_vec {
        if i == 100 as u8 {
            new_string.push('-');
        } else {
            new_string.push((i + 97) as char);
        }
    }
    println!("{} {}", new_string.into_iter().collect::<String>(), original_count);
    return
}

fn part1() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut total = 0;
    for i in data.split("\n") {
        let res = cutString(i);
        if checkLetters(res[0], res[2]){
            total += res[1].parse::<i32>().unwrap();
        }
    }
    println!("Part 1: {}", total);
}

fn part2() {
    let data = fs::read_to_string("in.txt").unwrap();
    for i in data.split("\n") {
        let res = cutString(i);
        if (checkLetters(res[0], res[2]) || true){
            decrypt(res[0], res[1].parse::<i32>().unwrap());
        }
    }
}