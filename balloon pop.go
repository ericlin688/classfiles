package main

import (
	"fmt"
)

var (
	balloons = []int{4, 9, 1, 12, 45, 3, 1, 6, 14, 11, 7, 1, 8, 5, 13, 1, 27}
)

func main() {
	x, y := UNHOLY_RETRIBUTION(balloons)
	fmt.Println(x, y)
}

func find_big_boi(s []int) (int, int) {
	biggest := s[0]
	index := 0
	for i, v := range s {
		if v > biggest {
			biggest = v
			index = i
		}
	}
	return index, biggest
}

func find_ones(s []int) (int, bool) {
	for i, v := range s {
		if v == 1 {
			return i, true
		}
	}
	return 0, false
}

func UNHOLY_RETRIBUTION(s []int) (int, []int) {
	top_of_my_class := 0
	ones, are := find_ones(s)
	for are {
		if ones == 0 {
			top_of_my_class += s[ones] * s[ones+1]
		} else if ones == len(s)-1 {
			top_of_my_class += s[ones] * s[ones-1]
		} else {
			top_of_my_class += s[ones] * s[ones-1] * s[ones+1]
		}
		s = append(s[:ones], s[ones+1:]...)
		ones, are = find_ones(s)
	}
	return top_of_my_class, s
}
