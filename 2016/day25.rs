use std::fs;

fn main() {
    let mut curr = 1;
    let data = fs::read_to_string("in.txt").unwrap();
    let lines = data.split("\n").collect::<Vec<&str>>();
    loop {
        if run_attempt(curr, lines.clone()) {
            println!("Part 1: {}", curr);
            return;
        }
        curr += 1;
    }
}

fn run_attempt(start: i32, lines: Vec<&str>) -> bool {
    let mut index: i32 = 0;
    let mut registers = [start, 362, 7, 0];
    let mut prev = 1;
    let mut count2 = 0;
    while index < (lines.len() as i32) {
        let line = lines[index as usize].split(" ").collect::<Vec<&str>>();
        if index == 0 {
            index = 7;
            registers[3] = registers[0] + (7 * 362);
        } else if index >= 21 && registers[2] > 2 {
            return false;
        } else if index == -1 {
            return true;
        } else {
            match line[0] {
                "cpy" => {
                    let mut num = 0;
                    if ((line[1].as_bytes()[0] as usize) as usize) < 90 {
                        num = line[1].parse::<i32>().unwrap();
                    } else {
                        num = registers[(line[1].trim().as_bytes()[0] as usize) - 97 as usize];
                    }
                    registers[(line[2].trim().as_bytes()[0] as usize) - 97 as usize] = num
                }
                "jnz" => {
                    if (line[1].chars().nth(0).unwrap() as u8) < 90 {
                        if (line[1].chars().nth(0).unwrap() as u8) != 48 {
                            index += line[2].trim().parse::<i32>().unwrap();
                            index -= 1;
                        }
                    } else if registers[(line[1].as_bytes()[0] as usize) - 97 as usize] != 0 {
                        index += line[2].trim().parse::<i32>().unwrap();
                        index -= 1;
                    }
                }
                "inc" => registers[(line[1].trim().as_bytes()[0] as usize) - 97 as usize] += 1,
                "out" => {
                    if registers[1] > 1 || registers[1] < 0 || registers[1] == prev {
                        return false;
                    } else {
                        count2 += 1;
                        if count2 > 100 {
                            return true;
                        }
                        prev = (prev + 1) % 2;
                    }
                }
                _ => registers[(line[1].trim().as_bytes()[0] as usize) - 97 as usize] -= 1,
            }
        }
        index += 1;
    }
    return false;
}
