import random
import numpy as np
from sklearn import svm

def main():
	palm_data = load_data('palm.txt')
	stone_data = load_data('stone.txt')
	train_data = palm_data + stone_data
	print(train_data)

	palm_label = [0 for i in range(len(palm_data))]
	stone_label = [0 for i in range(len(stone_data))]
	train_label = palm_label + stone_label

	clf = svm.SVC(gamma='scale')
	clf.fit(train_data, train_label)  






def load_data(file_name):
	
	# Load data
	file = open("mediapipe/" + file_name)
	elements = file.readlines()

	# Clean up data

	# Check whether the last element is 'end', if not, delete the elements after the last 'end'
	for i, v in enumerate(reversed(elements)):
		if "end" in v:
			end_index = len(elements)-i-1
			if end_index != len(elements)-1:
				elements = elements[0:end_index]
			break
	elements_arr = [i.strip() for i in elements if "end" not in i]
	elements_chunk = np.array_split(elements_arr, len(elements)/21)

	output = []

	# Clean up data, split int sub chunk and convert coordinate from string to float
	for chunk in elements_chunk:
		new_chunk = [i.split(',') for i in chunk]
		dstring_chunk = []
		for coord in new_chunk:
			dstring = [float(i) for i in coord]
			dstring_chunk.append(dstring)

		output.append(dstring_chunk)
	
	return output

  
if __name__== "__main__":
  main()
