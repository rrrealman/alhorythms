package main

import "fmt"

func process_lps(pattern string) []int {
	lps := make([]int, len(pattern))
	lps[0] = 0
	current_prefix := 0
	for position := 1; position < len(pattern); position++ {
		if pattern[position] == pattern[current_prefix] {
			current_prefix += 1
		} else {
			current_prefix = 0
		}
		lps[position] = current_prefix
	}
	return lps
}



func main() {
	fmt.Println(process_lps("joka_and_boka"))
	fmt.Println(process_lps("AABAACAABAA"))
}

