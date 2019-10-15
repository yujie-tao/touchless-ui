import time
import random
import numpy as np
from sklearn import svm

def main():
	classifier = train()
	print('classifier done')
	file = open("mediapipe/test.txt","r")
	gesture_stream = follow(file)
	for gesture in gesture_stream:
		if "end" not in gesture:
			gesture = gesture.strip().split(',')
			gesture = [[float(i) for i in gesture]]
			print(classifier.predict(gesture))


def follow(file_name):
    file_name.seek(0,2)
    while True:
        gesture = file_name.readline()
        if not gesture:
            time.sleep(0.1)
            continue
        yield gesture


def train():
	palm_data = load_data('palm.txt')
	stone_data = load_data('stone.txt')
	train_data = np.concatenate([palm_data, stone_data])

	palm_label = [0 for i in range(len(palm_data))]
	stone_label = [1 for i in range(len(stone_data))]
	train_label = palm_label + stone_label

	classifier = svm.SVC(gamma='scale')
	classifier.fit(train_data, train_label)  
	return classifier



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

	# Get rid of '\n' and all 'end' elements
	elements_arr = [i.strip() for i in elements if "end" not in i]
	# Split into chunks with each of 21
	elements_chunk = np.array_split(elements_arr, len(elements_arr)/21)

	output = []

	# Clean up data, split int sub chunk and convert coordinate from string to float
	for chunk in elements_chunk:
		new_chunk = [i.split(',') for i in chunk]
		dstring_chunk = []
		for coord in new_chunk:
			dstring = np.asarray([float(i) for i in coord])
			dstring_chunk.append(dstring)

		output.append(np.asarray(dstring_chunk))

	output = np.asarray(output).reshape(len(output)*21,2)
	
	return output

  
if __name__== "__main__":
  main()
