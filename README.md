# Advent of Code 2020 Day 2 - Password Philosophy

This is the Advent of Code 2020 day 2 password philosophy solutions. Included is 
the password input file and the project 1 and 2 source codes.

https://adventofcode.com/2020/day/2

## Project 1
This problem involves validating a list of password inputs. You are given a file with the format of lines with
`[lowerbound]-[upperbound] [reqChar]: [password]` and then need to parse the line then check to make sure the required
character shows up in the password the given number of times between the lower and upper bounds. The answer being the 
number of valid password meeting that criteria.

## Project 2
This problem is similar to project 1. It uses the same input file, only instead of the lower and upper bounds, the first
two numbers are indices within the password, `[firstIndex]-[secondIndex] [reqChar]: [password]`. The requirement for this project is that the required character should show
up exactly once between the two indices. If it is at neither or both, it is invalid. Again, this answer is the count of
valid passwords.
