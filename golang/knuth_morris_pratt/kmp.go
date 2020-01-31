package main

import "fmt"

func process_pattern(pattern string) []int {
	lps := make([]int, len(pattern))
	lps[0] = 0
	current_prefix := 0
	for position := 1; position < len(pattern); position++ {
		if pattern[position] == pattern[current_prefix] {
			current_prefix++
		} else {
			current_prefix = 0
		}
		lps[position] = current_prefix
	}
	return lps
}

func find_pattern(pattern string, text string) []int {
	lps := process_pattern(pattern)
	found := []int{}
	for text_pos, pat_pos := 0, 0; text_pos < len(text); text_pos++ {
		if text[text_pos] != pattern[pat_pos] {
			pat_pos = lps[pat_pos]
		} else {
			if pat_pos < len(pattern)-1 {
				pat_pos++
			} else {
				found = append(found, text_pos-len(pattern)+1)
				pat_pos = lps[pat_pos]
			}
		}
	}
	return found
}

func main() {
	text := "AABAACAABAA"
	pattern := "AAB"
	result := find_pattern(pattern, text)
	fmt.Println("Pattern", pattern, "text:", text, "result:", result)
}
