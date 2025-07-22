use std::fs;

fn main() {
    partBoth(false);
    partBoth(true);
}

fn partBoth(part2: bool) {
    let data = fs::read_to_string("in.txt").unwrap();
    let lines = data.split("\n").collect::<Vec<&str>>();
    let mut index: i32 = 0;
    let mut registers = [0, 0, 0, 0, 0, 0, 0];
    if part2 {
        registers[2] = 1;
    }
    while index < (lines.len() as i32) {
        let line = lines[index as usize].split(" ").collect::<Vec<&str>>();
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
                    index += line[2].trim().parse::<i32>().unwrap();
                    index -= 1;
                } else if registers[(line[1].as_bytes()[0] as usize) - 97 as usize] != 0 {
                    index += line[2].trim().parse::<i32>().unwrap();
                    index -= 1;
                }
            }
            "inc" => registers[(line[1].trim().as_bytes()[0] as usize) - 97 as usize] += 1,
            _ => registers[(line[1].trim().as_bytes()[0] as usize) - 97 as usize] -= 1,
        }
        index += 1
    }
    println!("{}", registers[0]);
}
