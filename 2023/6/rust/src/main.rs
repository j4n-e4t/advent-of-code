use std::fs::File;
use std::io::{self, BufRead};

const FILE: &str = "../input.txt";

fn main() {
    let (time, distances) = parse_input_file();
    println!(
        "Possible holding durations: {}",
        calculate_possible_options(
            format!("{}{}{}{}", time[0], time[1], time[2], time[3])
                .parse::<usize>()
                .unwrap(),
            format!("{}{}{}{}", distances[0], distances[1], distances[2], distances[3])
                .parse::<usize>()
                .unwrap()
        )
    );
}

fn parse_input_file() -> (Vec<usize>, Vec<usize>) {
    if let Ok(file) = File::open(FILE) {
        let mut lines = io::BufReader::new(file).lines();

        let first_line = lines
            .next()
            .unwrap()
            .unwrap()
            .split_whitespace()
            .skip(1)
            .map(|s| s.parse().unwrap())
            .collect();

        let second_line = lines
            .next()
            .unwrap()
            .unwrap()
            .split_whitespace()
            .skip(1)
            .map(|s| s.parse().unwrap())
            .collect();

        (first_line, second_line)
    } else {
        panic!("Failed to open the input file.");
    }
}

fn calculate_possible_options(time: usize, distance: usize) -> usize {
    let mut options = Vec::new();
    for i in 1..time {
        if (time - i) * i > distance {
            options.push(i);
        }
    }
    options.len()
}

