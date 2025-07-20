use std::fs;
use std::collections::HashMap;

fn main() {
    let mut index_nums : Vec<HashMap<char, i32>> = Vec::new();
    let data = fs::read_to_string("in.txt").unwrap();
    for i in data.split("\n") {
        if index_nums.len() == 0 {
            for _j in 0..i.len() {
                let new_map : HashMap<char, i32> = HashMap::new();
                index_nums.push(new_map);
            }
        }
        let mut index = 0;
        for j in i.chars() {
            index_nums[index].entry(j).and_modify(|num| *num += 1).or_insert(1);
            index += 1;
        }
    }
    let mut output1 = "".to_owned();
    let mut output2 = "".to_owned();
    for i in index_nums {
        let mut maximum = 0;
        let mut minimum = 9999;
        let mut curr_max = 'a';
        let mut curr_min = 'a';
        for j in i {
            if j.1 > maximum {
                maximum = j.1;
                curr_max = j.0;
            }
            if j.1 < minimum {
                minimum = j.1;
                curr_min = j.0;
            }
        }
        output1.push_str(&curr_max.to_string());
        output2.push_str(&curr_min.to_string());
    }
    println!("{}", output1);
    println!("{}", output2);
    return
}

//ikerpcty