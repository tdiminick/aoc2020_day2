validPasswordCount = 0

# returns int
def count(pstring, char):
	cnt = 0
	for i in pstring:
		if i == char:
			cnt += 1 # cnt = cnt + 1

	return cnt

# read file and parse each line, then validate password
with open('password_input.txt') as f:
	for line in f:
		lineSplit = line.split(":");
		password = lineSplit[1].strip()
		
		reqSplit = lineSplit[0].split()
		reqChar = reqSplit[1]
		
		boundSplit = reqSplit[0].split("-")
		lowerBound = int(boundSplit[0])
		upperBound = int(boundSplit[1])

		cnt = count(password, reqChar)

		if cnt >= lowerBound and cnt <= upperBound:
			validPasswordCount += 1

	print(validPasswordCount)


# [lower bound]-[upper bound] [reqChar]: [password]