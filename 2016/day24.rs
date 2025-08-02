use std::collections::HashMap;
use std::fs;

fn main() {
    let res = part_both();
    println!("{} {}", res[0], res[1]);
}

fn bfssearch(
    start: i32,
    end: i32,
    mapping: HashMap<i32, bool>,
    maximum_y: i32,
    maximum_x: i32,
) -> i32 {
    let mut open: Vec<i32> = Vec::new();
    let mut closed: Vec<i32> = Vec::new();
    let mut steps = 0;
    let mut remaining = 1;
    open.push(start);
    loop {
        let curr = open[0];
        if remaining == 0 {
            remaining = open.len();
            steps += 1;
        }
        if curr == end {
            return steps;
        }
        closed.push(curr);
        if curr - 1000 > 0
            && !closed.contains(&(curr - 1000))
            && *mapping.get(&(curr - 1000)).unwrap()
        {
            open.push(curr - 1000);
            closed.push(curr - 1000);
        }
        if curr + 1000 < maximum_x * 1000
            && !closed.contains(&(curr + 1000))
            && *mapping.get(&(curr + 1000)).unwrap()
        {
            open.push(curr + 1000);
            closed.push(curr + 1000);
        }
        if (curr - 1) % 1000 < maximum_y
            && !closed.contains(&(curr - 1))
            && *mapping.get(&(curr - 1)).unwrap()
        {
            open.push(curr - 1);
            closed.push(curr - 1);
        }
        if (curr + 1) % 1000 < maximum_y
            && !closed.contains(&(curr + 1))
            && *mapping.get(&(curr + 1)).unwrap()
        {
            open.push(curr + 1);
            closed.push(curr + 1);
        }
        remaining -= 1;
        open.remove(0);
    }
}

fn part_both() -> Vec<i32> {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut goals: Vec<i32> = Vec::new();
    let mut spaces: HashMap<i32, bool> = HashMap::new();
    let mut goal_dict: HashMap<i32, usize> = HashMap::new();
    let mut curr_index = 0;
    let mut x = 0;
    let mut y = 0;
    let maximum_y = data.len();
    let mut maximum_x = 0;
    let mut start = 0;
    for i in data.split("\r\n") {
        for j in i.chars() {
            if j != '\n' {
                if j != '#' {
                    spaces.insert(x * 1000 + y, true);
                    if j != '.' {
                        if j == '0' {
                            start = x * 1000 + y;
                        }
                        goals.push(x * 1000 + y);
                        goal_dict.insert(x * 1000 + y, curr_index);
                        curr_index += 1;
                    }
                } else {
                    spaces.insert(x * 1000 + y, false);
                }
            }
            x += 1;
        }
        maximum_x = x;
        x = 0;
        y += 1;
    }
    let mut distances: Vec<Vec<i32>> = Vec::new();
    for i in goals.clone() {
        let mut new_line: Vec<i32> = Vec::new();
        for j in goals.clone() {
            if i == j {
                new_line.push(0);
            } else {
                new_line.push(bfssearch(i, j, spaces.clone(), maximum_x, maximum_y as i32));
            }
        }
        distances.push(new_line);
    }
    let mut options: Vec<Vec<i32>> = Vec::new();
    let mut start_option: Vec<i32> = Vec::new();
    start_option.push(0);
    start_option.push(start);
    start_option.push(start);
    options.push(start_option);
    let mut step = 0;
    let mut bests = vec![0, 0];
    loop {
        let mut next_options: Vec<Vec<i32>> = Vec::new();
        if (bests[1] == step && bests[1] != 0) || options.len() == 0 {
            return bests;
        }
        for i in 0..options.len() {
            if step == options[i][0] && options[i].len() == 2 + goals.len() {
                if bests[0] == 0 {
                    bests[0] = step;
                }
                let new_num = step
                    + distances[*goal_dict.get(&options[i][1]).unwrap()]
                        [*goal_dict.get(&start).unwrap()];
                if (new_num < bests[1]) || bests[1] == 0 {
                    bests[1] = new_num;
                }
            } else if step == options[i][0] {
                for j in goals.clone() {
                    if !options[i].contains(&j) {
                        let mut new_option = options[i].clone();
                        new_option.push(j);
                        new_option[0] += distances[*goal_dict.get(&new_option[1]).unwrap()]
                            [*goal_dict.get(&j).unwrap()];
                        new_option[1] = j;
                        next_options.push(new_option);
                    }
                }
            } else {
                let new_option = options[i].clone();
                next_options.push(new_option);
            }
        }
        step += 1;
        options = next_options;
    }
}

// 712 high
