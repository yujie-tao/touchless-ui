import time
import random
import numpy as np
from sklearn import svm

def main():
	classifier = train()
	# a = np.asarray([0.513122,0.860783,0.356239,0.790055,0.274009,0.668277,0.246593,0.552753,0.221277,0.469811,0.414848,0.50565 ,0.387338,0.34371 ,0.377919,0.23178,0.373127,0.143402,0.520822,0.508402,0.538382,0.331114,0.547799,0.214045,0.545361,0.124099,0.613324,0.541049,0.643841,0.379376,0.645113,0.273412,0.638148,0.187606,0.703423,0.596537,0.745857,0.481994,0.779236,0.391669,0.80264,0.2922842]).reshape(1,42)
	# print((np.asarray(a)).shape)
	# print(classifier.predict(a))
	# print('classifier done')
	file = open("mediapipe/test.txt","r")
	gesture_stream = follow(file)
	gesture = []
	for finger_coord in gesture_stream:
		if "end" not in finger_coord:
			finger_coord = finger_coord.strip().split(',')
			finger_coord = [float(i) for i in finger_coord]
			gesture.extend(finger_coord)

			if len(gesture) == 42:
				test_gesture = np.asarray(gesture).reshape(1,42)
				print(classifier.predict(test_gesture))
				gesture.clear()


def follow(file_name):
    file_name.seek(0,2)
    while True:
        finger_coord = file_name.readline()
        if not finger_coord:
            time.sleep(0.1)
            continue
        yield finger_coord


def train():
	palm_data = load_data('palm.txt')
	stone_data = load_data('stone.txt')
	train_data = np.concatenate([palm_data, stone_data])

	palm_label = [0 for i in range(len(palm_data))]
	stone_label = [1 for i in range(len(stone_data))]
	train_label = np.concatenate([palm_label,stone_label])

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

		dstring_chunk = (np.asarray(dstring_chunk)).reshape(1,42)
		output.append(dstring_chunk)


	output = np.asarray(output).reshape(len(output),42)
	
	return output

  
if __name__== "__main__":
  main()
