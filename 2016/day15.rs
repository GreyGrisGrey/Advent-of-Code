fn main() {
    let modulos = [13, 17, 19, 7, 5, 3, 11];
    let goals = [12, 15, 16, 3, 0, 0, 4];
    let mut currs = [10, 15, 17, 1, 0, 1, 0];
    let mut good = 0;
    let mut mult = 1;
    let mut steps1 = 0;
    let mut steps2 = 0;
    while good < 7 {
        for i in good..7 {
            currs[i] += mult;
            currs[i] = currs[i] % modulos[i];
        }
        if good < 6 {
            steps1 += mult;
        }
        steps2 += mult;
        for i in 0..7 {
            if i == good && currs[i] == goals[i] {
                mult *= modulos[i];
                good += 1;
            }
        }
    }
    println!("Part 1: {}", steps1);
    println!("Part 2: {}", steps2);
}
