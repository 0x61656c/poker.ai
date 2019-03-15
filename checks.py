global_deck = [ 
	 (2,1),(2,2),(2,3),(2,4),
	 (3,1),(3,2),(3,3),(3,4),
	 (4,1),(4,2),(4,3),(4,4),
	 (5,1),(5,2),(5,3),(5,4),
	 (6,1),(6,2),(6,3),(6,4),
	 (7,1),(7,2),(7,3),(7,4),
	 (8,1),(8,2),(8,3),(8,4),
	 (9,1),(9,2),(9,3),(9,4),
	 (10,1),(10,2),(10,3),(10,4),
	 (11,1),(11,2),(11,3),(11,4),
	 (12,1),(12,2),(12,3),(12,4),
	 (13,1),(13,2),(13,3),(13,4),
	 (14,1),(14,2),(14,3),(14,4)]

def suit_elim(card_array):
	result = []
	for element in card_array:
		result.append(element[0])
	return result

def checkPair(card_array):
	c1 = suit_elim(card_array)
	if len(set(c1)) == 6:
		return True
	return False

def testCheckPair():
	c1 = [(2,1),(2,2),(2,3),(3,3),(3,4),
	(4,1),(4,2)]

	c2 = [(2,1),(2,2),(9,3),(10,3),(11,4),
	(12,1),(13,2)]

	c3 = [(2,1),(2,2),(2,3),(10,3),(11,4),
	(12,1),(13,2)]


	print(checkPair(c1)) #False
	print(checkPair(c2)) #True
	print(checkPair(c3)) #False

def main():
	testCheckPair()

if __name__ == "__main__":
	main()

