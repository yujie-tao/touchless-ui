import time
import random
import asyncio
import numpy as np
from sklearn import svm


import control

import asyncio
import pyppeteer

def main():

	# Launch classifier
	classifier = train()
	print("Training Completed.")
	
	## Open browser
	# page = asyncio.get_event_loop().run_until_complete(control.launch_page())

	input_data = open("mediapipe/test.txt","r")
	predict(classifier, input_data)
	# print(type(output))

	# if output == [1]:
	# 	print('yes')
		# asyncio.get_event_loop().run_until_complete(control.click_button(page))



async def headless_control():
	browser = await launch()
	page = await browser.newPage()
	await page.goto('google.com')
	await page.screenshot({'path': 'example.png'})
	await browser.close()


# Clsassify input steram
def predict(classifier, input_data):
	page = asyncio.get_event_loop().run_until_complete(control.launch_page())


	on = True

	input_data = open("mediapipe/test.txt","r")
	gesture_stream = listen(input_data)
	gesture = []

	for finger_coord in gesture_stream:
		if "end" not in finger_coord:
			finger_coord = finger_coord.strip().split(',')
			finger_coord = [float(i) for i in finger_coord]
			gesture.extend(finger_coord)

			if len(gesture) == 42:
				test_gesture = np.asarray(gesture).reshape(1,42)
				prediction = classifier.predict(test_gesture)
				print(prediction)


				if prediction == [1] and on is False:
					# if asyncio.get_event_loop() == None:
					# 	asyncio.set_event_loop(acontrol.click_button(page))
					# loop = asyncio.get_event_loop()
					# while True:
					# try:
					# 	loop = asyncio.get_event_loop()
					# 	print('hello')
					# 	# break
					# 	# loop.create_connection()

					# except:
					# 	print('ok')
					# 	asyncio.set_event_loop(syncio.new_event_loop())
					# 	loop = asyncio.get_event_loop()

					loop = asyncio.get_event_loop()
					loop.run_until_complete(control.click_button(page))
					# try:
					# 	loop.run_until_complete(control.click_button(page))

					# except RuntimeError: 
					# 	loop = asyncio.new_event_loop()
					# 	asyncio.set_event_loop(loop)
					# 	loop_new = asyncio.get_event_loop()

					# 	print(loop_new.is_closed())
					# 	loop_new.run_until_complete(control.click_button(page))

					# loop.close()
					on = True
				else:
					if prediction == [2] and on is True:
						# loop = asyncio.get_event_loop()
						loop = asyncio.get_event_loop()
						loop.run_until_complete(control.click_button(page))
						# try:
						# 	loop.run_until_complete(control.click_button(page))

						# except RuntimeError:
						# 	loop = asyncio.new_event_loop()
						# 	asyncio.set_event_loop(loop)
						# 	loop_new = asyncio.get_event_loop()

						# 	print(loop_new.is_closed())
						# 	loop_new.run_until_complete(control.click_button(page))


						# loop.close()
						on = False

				gesture.clear()


# Listen the output update from mediapipe
def listen(file_name):
    file_name.seek(0,2)
    while True:
        finger_coord = file_name.readline()
        if not finger_coord:
            time.sleep(0.1)
            continue
        yield finger_coord


def train():
	palm_data = load_data("palm.txt")
	stone_data = load_data("stone.txt")
	noise_data = load_data("noise.txt")
	train_data = np.concatenate([palm_data, stone_data, noise_data])

	palm_label = [1 for i in range(len(palm_data))]
	stone_label = [2 for i in range(len(stone_data))]
	noise_label = [-1 for i in range(len(noise_data))]
	train_label = np.concatenate([palm_label,stone_label, noise_label])

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

	# Reshape into 2D as original datat is in 3D, which is not spported in SVM
	output = np.asarray(output).reshape(len(output),42)
	
	return output

  
if __name__== "__main__":
  main()
