validPasswordCount = 0

# returns bool
def isPasswordValid(pstring, char, firstIndex, secondIndex):
	firstCheck = pstring[firstIndex] == char # boolean
	secondCheck = pstring[secondIndex] == char # boolean

	if (firstCheck and secondCheck) or (not firstCheck and not secondCheck):
		return False
	else:
		return True

# read file and parse each line, then validate password
with open('password_input.txt') as f:
	for line in f:
		lineSplit = line.split(":");
		password = lineSplit[1].strip()
		
		reqSplit = lineSplit[0].split()
		reqChar = reqSplit[1]
		
		indexSplit = reqSplit[0].split("-")
		firstIndex = int(indexSplit[0]) - 1
		secondIndex = int(indexSplit[1]) - 1

		if isPasswordValid(password, reqChar, firstIndex, secondIndex):
			validPasswordCount += 1

	print(validPasswordCount)


# [firstIndex]-[secondIndex] [reqChar]: [password]