use std::fs;
mod md5;

fn main() {
    println!("Part 2: {}", part_both());
}

fn step(curr_path: String, dir: char) -> String {
    let mut new_str = "".to_owned();
    new_str.push_str(&curr_path);
    new_str.push_str(&dir.to_string());
    return new_str;
}

fn part_both() -> i32 {
    let keyword = fs::read_to_string("in.txt").unwrap();
    let mut open: Vec<(String, i32, i32)> = Vec::new();
    open.push((keyword.clone(), 0, 0));
    let mut steps = 0;
    let mut remaining = 1;
    let mut maximum = 0;
    loop {
        if remaining == 0 {
            remaining = open.len();
            steps += 1;
            if remaining == 0 {
                return maximum;
            }
        }
        let curr = open[0].clone();
        if (curr.1 != 3) || (curr.2 != 3) {
            let encoding = &format!("{:x}", md5::compute(curr.0.clone()));
            if curr.1 > 0 && (encoding.chars().nth(2).unwrap() as u8) > 97 {
                open.push((step(curr.0.clone(), 'L'), curr.1 - 1, curr.2));
            }
            if curr.2 > 0 && (encoding.chars().nth(0).unwrap() as u8) > 97 {
                open.push((step(curr.0.clone(), 'U'), curr.1, curr.2 - 1));
            }
            if curr.1 < 3 && (encoding.chars().nth(3).unwrap() as u8) > 97 {
                open.push((step(curr.0.clone(), 'R'), curr.1 + 1, curr.2));
            }
            if curr.2 < 3 && (encoding.chars().nth(1).unwrap() as u8) > 97 {
                open.push((step(curr.0.clone(), 'D'), curr.1, curr.2 + 1));
            }
        } else {
            if maximum == 0 {
                println!("Part 1: {}", curr.0);
            }
            maximum = steps;
        }
        open.remove(0);
        remaining -= 1;
    }
}
