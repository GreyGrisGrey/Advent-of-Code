use std::collections::HashMap;
use std::fs;

fn main() {
    part1();
}

fn find_path(
    start_x: u16,
    start_y: u16,
    end_x: u16,
    end_y: u16,
    nodes: HashMap<u16, Vec<u16>>,
    skip_x: u16,
    skip_y: u16,
) -> u16 {
    let mut open: Vec<u16> = Vec::new();
    let mut closed: Vec<u16> = Vec::new();
    open.push(start_x * 100 + start_y);
    let mut curr = start_x * 100 + start_y;
    let mut steps = 0;
    let mut remaining = 1;
    let skip_key = skip_x * 100 + skip_y;
    while open.len() != 0 {
        curr = open[0];
        if remaining == 0 {
            remaining = open.len();
            steps += 1;
        }
        remaining -= 1;
        if curr == end_x * 100 + end_y {
            return steps;
        }
        closed.push(curr);
        if curr >= 100
            && !closed.contains(&(curr - 100))
            && nodes.get(&(curr - 100)).unwrap()[0] < 100
            && curr != skip_key
        {
            open.push(curr - 100);
            closed.push(curr - 100);
        }
        if (&(curr - 1) % 100) < 30
            && !closed.contains(&(curr - 1))
            && nodes.get(&(curr - 1)).unwrap()[0] < 100
            && curr != skip_key
        {
            open.push(curr - 1);
            closed.push(curr - 1);
        }
        if (&(curr + 1) % 100) < 30
            && !closed.contains(&(curr + 1))
            && nodes.get(&(curr + 1)).unwrap()[0] < 100
            && curr != skip_key
        {
            open.push(curr + 1);
            closed.push(curr + 1);
        }
        if curr + 100 < 3200
            && !closed.contains(&(curr + 100))
            && nodes.get(&(curr + 100)).unwrap()[0] < 100
            && curr != skip_key
        {
            open.push(curr + 100);
            closed.push(curr + 100);
        }
        open.remove(0);
    }
    return 0;
}

fn part1() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut node_map: HashMap<u16, Vec<u16>> = HashMap::new();
    let mut x = 0;
    let mut y = 0;
    let mut skip = 0;
    let mut empty_x = 0;
    let mut empty_y = 0;
    for i in data.split("\n") {
        if skip < 2 {
            skip += 1;
        } else {
            let mut line: Vec<&str> = Vec::new();
            for j in i.split(" ") {
                if j != "" {
                    line.push(j.trim());
                }
            }
            let mut new_vec: Vec<u16> = Vec::new();
            let name = (x * 100) + y;
            for j in 1..5 {
                new_vec.push(line[j][..line[j].len() - 1].parse::<u16>().unwrap());
                if line[j][..line[j].len() - 1].parse::<u16>().unwrap() == 0 {
                    empty_x = x;
                    empty_y = y;
                }
            }
            y += 1;
            if y > 29 {
                y = 0;
                x += 1;
            }
            node_map.insert(name, new_vec);
        }
    }
    let mut count = 0;
    for i in 0..32 {
        for j in 0..30 {
            for k in 0..32 {
                for l in 0..30 {
                    if (j != l || k != i)
                        && node_map.get(&(i * 100 + j)).unwrap()[1] != 0
                        && node_map.get(&(i * 100 + j)).unwrap()[1]
                            <= node_map.get(&(k * 100 + l)).unwrap()[2]
                    {
                        count += 1;
                    }
                }
            }
        }
    }
    println!("Part 1: {}", count);
    let mut spaces = 0;
    for i in 0..31 {
        spaces += 1;
        if i != 30 {
            spaces += find_path(i + 2, 0, i, 0, node_map.clone(), i + 1, 0);
        } else {
            spaces += find_path(empty_x, empty_y, 30, 0, node_map.clone(), 50, 50);
        }
    }
    println!("Part 2: {}", spaces);
}
