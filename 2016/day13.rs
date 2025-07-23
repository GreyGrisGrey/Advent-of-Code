use std::fs;

fn main() {
    part_both();
}

fn check_good(x: i32, y: i32, add: i32) -> bool {
    if x < 0 || y < 0 {
        return false;
    }
    if (x * x + 3 * x + 2 * x * y + y + y * y + add).count_ones() % 2 == 0 {
        return true;
    }
    return false;
}

fn part_both() {
    let add_num = fs::read_to_string("in.txt")
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();
    let end: (i32, i32) = (31, 39);
    let mut open: Vec<(i32, i32)> = Vec::new();
    let mut closed: Vec<(i32, i32)> = Vec::new();
    let mut steps: i32 = 0;
    let mut remaining: i32 = 1;
    let mut count: i32 = 0;
    open.push((0, 0));
    loop {
        if remaining == 0 {
            remaining = open.len() as i32;
            steps += 1;
        }
        remaining -= 1;
        let curr = open[0];
        if steps < 50 && !closed.contains(&curr) {
            count += 1;
        }
        if (curr.0 == end.0) && (curr.1 == end.1) {
            println!("Part 1: {}\nPart 2: {}", steps, count);
            return;
        }
        if check_good(curr.0 + 1, curr.1, add_num) && !closed.contains(&curr) {
            open.push((curr.0 + 1, curr.1));
        }
        if check_good(curr.0 - 1, curr.1, add_num) && !closed.contains(&curr) {
            open.push((curr.0 - 1, curr.1));
        }
        if check_good(curr.0, curr.1 + 1, add_num) && !closed.contains(&curr) {
            open.push((curr.0, curr.1 + 1));
        }
        if check_good(curr.0, curr.1 - 1, add_num) && !closed.contains(&curr) {
            open.push((curr.0, curr.1 - 1));
        }
        closed.push(curr);
        open.remove(0);
    }
}
