use std::collections::HashMap;
use std::fs;

fn main() {
    println!("Part 1: {}", part_both(7));
    println!("Part 2: {}", part_both(12));
}

fn part_both(starter: i32) -> i32 {
    let mut registers = [starter, 0, 0, 0];
    let mut insts: HashMap<u8, Vec<&str>> = HashMap::new();
    let mut curr = 0;
    let data = fs::read_to_string("in.txt").unwrap();
    for i in data.split("\n") {
        let mut new_vec: Vec<&str> = Vec::new();
        for j in i.split(" ") {
            new_vec.push(&(j.trim()));
        }
        insts.insert(curr, new_vec);
        curr += 1;
    }
    let maximum = curr as i32;
    let mut index = 0;
    // most likely not a general solution
    while index < maximum {
        let line = insts.get(&(index as u8)).unwrap();
        if index != 5 && index != 21 {
            match line[0] {
                "cpy" => {
                    let num: i32;
                    if ((line[1].as_bytes()[0] as usize) as usize) < 90 {
                        num = line[1].parse::<i32>().unwrap();
                    } else {
                        num = registers[(line[1].trim().as_bytes()[0] as usize) - 97 as usize];
                    }
                    registers[(line[2].trim().as_bytes()[0] as usize) - 97 as usize] = num
                }
                "jnz" => {
                    if (line[1].chars().nth(0).unwrap() as u8) < 90
                        || registers[(line[1].as_bytes()[0] as usize) - 97 as usize] != 0
                    {
                        if (line[2].chars().nth(0).unwrap() as u8) < 90 {
                            index += line[2].trim().parse::<i32>().unwrap();
                        } else {
                            index +=
                                registers[(line[2].trim().as_bytes()[0] as usize) - 97 as usize];
                        }
                        index -= 1;
                    }
                }
                "tgl" => {
                    let mut num = index;
                    if ((line[1].as_bytes()[0] as usize) as usize) < 90 {
                        num += line[1].parse::<i32>().unwrap();
                    } else {
                        num += registers[(line[1].trim().as_bytes()[0] as usize) - 97 as usize];
                    }
                    if num < maximum && num >= 0 {
                        let new_line = insts.get(&(num as u8)).unwrap();
                        let mut new_vec = Vec::new();
                        if new_line.len() == 2 && new_line[0] == "inc" {
                            new_vec.push("dec");
                            new_vec.push(new_line[1]);
                        } else if new_line.len() == 2 {
                            new_vec.push("inc");
                            new_vec.push(new_line[1]);
                        } else if new_line[0] == "jnz" {
                            new_vec.push("cpy");
                            new_vec.push(new_line[1]);
                            new_vec.push(new_line[2]);
                        } else {
                            new_vec.push("jnz");
                            new_vec.push(new_line[1]);
                            new_vec.push(new_line[2]);
                        }
                        insts.insert(num as u8, new_vec);
                    }
                }
                "inc" => registers[(line[1].trim().as_bytes()[0] as usize) - 97 as usize] += 1,
                _ => registers[(line[1].trim().as_bytes()[0] as usize) - 97 as usize] -= 1,
            }
            index += 1;
        } else {
            if index == 5 {
                registers[0] += registers[2] * registers[3];
                registers[2] = 0;
                registers[3] = 0;
                index += 2;
            } else {
                registers[0] += registers[3] * registers[2];
                registers[3] = 0;
                registers[2] = 0;
                index = 90;
            }
            index += 2;
        }
    }
    return registers[0];
}
