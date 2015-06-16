package main

import (
	"os"
	"bufio"
	"time"
)

func checkTimeRange(t time.Time) bool {
	today := time.Now()
	if today.Sub(t) <= 0 {
		return false
	}
	if t.Hour() == 16 && t.Minute() == 0 && t.Second() == 0 {
		return true
	}
	return t.Hour() >= 10 && t.Hour() < 16
}

func ProcessLog(filename string) (int, error) {
	f, err := os.Open(filename)
	if (err != nil) {
		return -1, err
	}
	scanner := bufio.NewScanner(f)
	var count int
	for scanner.Scan() {
		line := scanner.Text()
		t, err := time.Parse("[2006-01-02 15:04:05] - Abertura da Porta OK", line)
		if err == nil && checkTimeRange(t) {
			count++
		}
	}
	return count, nil
}
