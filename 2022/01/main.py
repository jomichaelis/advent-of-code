with open("input.txt", "r") as input_file:
	""" PART 1 """
	elves_calories = [0]
	for line in input_file.readlines():
		if line == '\n':
			elves_calories.append(0)
		else:
			elves_calories[-1] += int(line)

	max_calories = max(elves_calories)
	top_elve_index = elves_calories.index(max_calories)
	print(f"Elve number {top_elve_index} is carrying a total of {max_calories} calories.")

	""" PART 2 """
	top_3_calories = sorted(elves_calories, reverse=True)[0:3]
	top_3_indices = [top_elve_index]
	for summed_calories in top_3_calories[1:]:
		top_3_indices.append(elves_calories.index(summed_calories))
	print(f"In total, the Top3-elves (indices {', '.join(map(str,top_3_indices))}) carry {sum(top_3_calories)} calories with them.")
