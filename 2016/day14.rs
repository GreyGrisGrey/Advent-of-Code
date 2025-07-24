use std::fs;
mod md5;

fn main() {
    println!("Part 1: {}", part_both(false));
    println!("Part 2: {}", part_both(true));
}

fn get_triple(line: &str) -> u8 {
    let mut prev = 'g';
    let mut flag1 = false;
    for i in line.chars() {
        if prev == i && flag1 {
            return i as u8;
        } else if prev == i {
            flag1 = true;
        } else {
            flag1 = false;
            prev = i;
        }
    }
    return 0;
}

fn get_quint(line: &str, character: char) -> bool {
    let mut flags = [false, false, false, false];
    for i in line.chars() {
        if character == i && flags[3] {
            return true;
        } else if character == i && flags[2] {
            flags[3] = true;
        } else if character == i && flags[1] {
            flags[2] = true;
        } else if character == i && flags[0] {
            flags[1] = true;
        } else if character == i {
            flags[0] = true;
        } else {
            flags[0] = false;
            flags[1] = false;
            flags[2] = false;
            flags[3] = false;
        }
    }
    return false;
}

fn part_both(second: bool) -> i32 {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut count = 0;
    let mut hash_vec: Vec<Vec<u32>> = Vec::new();
    let mut good_index: Vec<i32> = Vec::new();
    let mut total_hash = 0;
    loop {
        let mut temp = data.to_owned();
        temp.push_str(&count.to_string());
        if second {
            for _i in 0..2016 {
                temp = format!("{:x}", md5::compute(temp));
            }
        }
        let new_hash = &format!("{:x}", md5::compute(temp));
        let res = get_triple(new_hash);
        let mut remove_index: Vec<u8> = Vec::new();
        for i in 0..hash_vec.len() {
            hash_vec[i][1] -= 1;
            if get_quint(new_hash, hash_vec[i][0] as u8 as char) {
                remove_index.push(i as u8);
                total_hash += 1;
                good_index.push(hash_vec[i][2] as i32);
                if total_hash >= 90 {
                    good_index.sort();
                    return good_index[63];
                }
            } else if hash_vec[i][1] <= 0 {
                remove_index.push(i as u8);
            }
        }
        for i in 0..remove_index.len() {
            hash_vec.remove(remove_index[remove_index.len() - (i + 1)] as usize);
        }
        if res != 0 {
            hash_vec.push(Vec::from([res as u32, 1000 as u32, count as u32]));
        }
        count += 1;
    }
}
