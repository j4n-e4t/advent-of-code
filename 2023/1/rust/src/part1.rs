// Advent of Code 2023 - Day 1 - Part 1

static FILE: &str = "../input.txt";

use std::fs::File;
use std::io::BufRead;

pub fn part1() {
    let mut sum = 0;

    let f = File::open(FILE).unwrap();
    let reader = std::io::BufReader::new(f);
    for line in reader.lines() {
        let numbers = get_numbers(&line.unwrap());
        if numbers.len() < 1 {
            continue;
        } else {
            sum += format!("{}{}", numbers[0], numbers[numbers.len() - 1]).parse::<i32>().unwrap();
        }
    }
    println!("SUM: {}", sum);
}

fn get_numbers(line: &str) -> Vec<i32> {
    let mut numbers = Vec::<i32>::new();
    for char in line.chars() {
        if char.is_digit(10) {
            numbers.push(char.to_digit(10).unwrap() as i32);
        }
    }
    return numbers;
}
