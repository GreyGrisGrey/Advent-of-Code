use std::fs;

fn main() {
    part_both();
}

fn part_both() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut intervals: Vec<(u32, u32)> = Vec::new();
    let mut best: u32 = 0;
    let mut count: u32 = 0;
    let mut curr: u32 = 0;
    for i in data.split("\n") {
        let mut min = 4294967295;
        let mut max = 0;
        for j in i.split("-") {
            if min == 4294967295 {
                min = j.parse::<u32>().unwrap();
            } else {
                max = j.trim().parse::<u32>().unwrap();
            }
        }
        intervals.push((min, max));
    }
    intervals.sort();
    for i in intervals {
        while curr < i.0 {
            if best == 0 {
                best = curr;
            }
            curr += 1;
            count += 1;
        }
        if curr < i.1 {
            curr = i.1;
            if curr != 4294967295 {
                curr += 1;
            }
        }
    }
    println!("Part 1: {}", best);
    println!("Part 2: {}", count);
}
