use std::fs;
use std::collections::HashMap;

fn main() {
    let data = fs::read_to_string("in.txt").unwrap();
    let mut mapping: HashMap<i32, Vec<i32>> = HashMap::new();
    let mut vals: HashMap<i32, i32> = HashMap::new();
    for i in data.split("\n") {
        let line = i.split(" ").collect::<Vec<&str>>();
        if line.len() == 6 {
            vals.insert(line[1].parse::<i32>().unwrap(), line[5].trim().parse::<i32>().unwrap());
        } else {
            let mut new_vec: Vec<i32> = Vec::new();
            if line[5] == "output" {
                new_vec.push((line[6].parse::<i32>().unwrap()+1) * 1000);
            } else {
                new_vec.push(line[6].parse::<i32>().unwrap());
            }
            if line[10] == "output" {
                new_vec.push((line[11].trim().parse::<i32>().unwrap()+1) * 1000);
            } else {
                new_vec.push(line[11].trim().parse::<i32>().unwrap());
            }
            mapping.insert(line[1].parse::<i32>().unwrap(), new_vec);
        }
    }
    let mut res = 0;
    let mut flag0 = false;
    let mut flag1 = false;
    let mut flag2 = false;
    let mut mult = 1;
    while !flag0 || !flag1 || !flag2 {
        let mut change0 = -1;
        let mut change1 = -1;
        let mut change2 = -1;
        for i in &vals {
            if (*i.0 == 61 || *i.0 == 17) && (vals.get(&61) == vals.get(&17)) && res == 0 {
                res = 1;
                println!("Part 1 : {}", vals.get(&61).unwrap().to_string());
            }
            for j in &vals {
                if *i.1 == *j.1 && *i.0 != *j.0 {
                    change0 = *j.0;
                    change1 = *i.0;
                    change2 = *i.1;
                }
            }
        }
        if change0 < change1 {
            vals.insert(change0, mapping.get(&change2).unwrap()[0]);
            vals.insert(change1, mapping.get(&change2).unwrap()[1]);
        } else {
            vals.insert(change1, mapping.get(&change2).unwrap()[0]);
            vals.insert(change0, mapping.get(&change2).unwrap()[1]);
        }
        if mapping.get(&change2).unwrap()[0] == 1000 || mapping.get(&change2).unwrap()[1] == 1000 {
            flag0 = true;
        }
        if mapping.get(&change2).unwrap()[0] == 2000 || mapping.get(&change2).unwrap()[1] == 2000 {
            flag1 = true;
        }
        if mapping.get(&change2).unwrap()[0] == 3000 || mapping.get(&change2).unwrap()[1] == 3000 {
            flag2 = true;
        }
    }
    for i in vals {
        if i.1 == 1000 || i.1 == 2000 || i.1 == 3000 {
            mult *= i.0;
        }
    }
    println!("Part 2 : {}", mult.to_string());
    return
}