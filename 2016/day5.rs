use std::fs;
mod md5;

fn main() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut count = 0;
    let mut out: Vec<char> = Vec::new();
    let mut checked: Vec<char> = Vec::new();
    while checked.len() != 8 {
        let mut temp = data.to_owned();
        temp.push_str(&count.to_string());
        let res = &format!("{:x}", md5::compute(temp));
        let mut checker = true;
        for i in 0..5 {
            if res.as_bytes()[i] as char != '0' {
                checker = false;
            }
        }
        if checker {
            if out.len() < 8 {
                out.push(res.as_bytes()[5] as char);
            }
            if res.as_bytes()[5] < 56 && res.as_bytes()[5] > 47 && !checked.contains(&(res.as_bytes()[5] as char)) {
                checked.push(res.as_bytes()[5] as char);
                println!("Position {}, Character {}", res.as_bytes()[5] as char, res.as_bytes()[6] as char);
            }
        }
        count += 1;
    }
    println!("Part 1 {}", out.into_iter().collect::<String>());
    return
}