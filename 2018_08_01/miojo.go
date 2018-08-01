package main

func miojo(amp1, amp2, preparo int) int {
	time := 0
	originalAmp1 := amp1
	originalAmp2 := amp2

	for i := 0; i <= 100; i++ {
		if amp1 == 0 {
			amp1 = originalAmp1
		}

		if amp2 == 0 {
			amp2 = originalAmp2
		}

		if amp1 > amp2 {
			if amp2 == preparo {
				return time + amp2
			}
			amp1 -= amp2
			time += amp2
			amp2 = 0
		} else {
			if amp1 == preparo {
				return time + amp1
			}
			time += amp1
			amp2 -= amp1
			amp1 = 0
		}
	}
	return -1
}

func main() {}
