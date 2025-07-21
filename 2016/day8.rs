use std::fs;

fn main() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut large_cube : Vec<Vec<bool>> = Vec::new();
    let mut total = 0;
    for _i in 0..6 {
        let mut new_line : Vec<bool> = Vec::new();
        for _j in 0..50 {
            new_line.push(false);
        }
        large_cube.push(new_line);
    }
    for i in data.split("\n") {
        let line: Vec<&str> = i.split(" ").collect();
        if line.len() == 2 {
            let dims: Vec<&str> = line[1].split("x").collect();
            for j in 0..(dims[1].trim().parse::<i32>().unwrap()) {
                for k in 0..(dims[0].parse::<i32>().unwrap()) {
                    large_cube[j as usize][k as usize] = true;
                }
            }
        } else {
            let mut count = line[4].trim().parse::<i32>().unwrap();
            let mut prev = false;
            let relevant : Vec<&str> = line[2].split("=").collect();
            let index = relevant[1].parse::<usize>().unwrap();
            while count > 0 {
                if line[1] == "row" {
                    for j in 0..50 {
                        if j == 0 {
                            prev = large_cube[index][j as usize];
                            large_cube[index][j as usize] = large_cube[index][49 as usize];
                        } else {
                            let temp = large_cube[index][j as usize];
                            large_cube[index][j as usize] = prev;
                            prev = temp;
                        }
                    }
                } else {
                    for j in 0..6 {
                        if j == 0 {
                            prev = large_cube[j as usize][index];
                            large_cube[j as usize][index] = large_cube[5 as usize][index];
                        } else {
                            let temp = large_cube[j as usize][index];
                            large_cube[j as usize][index] = prev;
                            prev = temp;
                        }
                    }
                }
                count -= 1;
            }
        }
    }
    for i in large_cube {
        let mut new_line = "".to_owned();
        for j in i {
            if j {
                total += 1;
                new_line.push_str("#");
            } else {
                new_line.push_str(".");
            }
        }
        println!("{}", new_line);
    }
    println!("Part 1: {}", total);
}