def LoopSolution(target):
    sum = 0
	for i = 1 to target do
		if (i mod 3 = 0) or (i mod 5 = 0) then sum := sum + i
	return sum
