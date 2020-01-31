package main

import "fmt"

func insertionSort(sequence_arg []int) {
	sequence := make([]int, len(sequence_arg))
	copy(sequence, sequence_arg)
	for insertion_pos, current := range sequence[1:] {
		for insertion_pos >= 0 && sequence[insertion_pos] > current {
			sequence[insertion_pos+1] = sequence[insertion_pos]
			insertion_pos -= 1
		}
		sequence[insertion_pos+1] = current
	}
}

func main() {
	arr := []int{3, 2, 1}
	insertionSort(arr)
	fmt.Println(arr)
}
