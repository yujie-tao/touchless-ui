# Use an official Python runtime as a parent image
FROM jjanzic/docker-python3-opencv:opencv-3.4.1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
#RUN dnf install git-all
#RUN pip install tensorflow==1.2.1
#RUN pip install keras==2.0.2
#RUN pip install Theano==0.9.0
#RUN pip uninstall numpy
#RUN pip install numpy==1.16.2
RUN git clone https://github.com/asingh33/CNNGestureRecognizer.git
RUN cd CNNGestureRecognizer
RUN gdown https://drive.google.com/uc\?id\=0B6cMRAuImU69SHNCcXpkT3RpYkE
#RUN chmod +x bazel-<0.4.5>-installer-linux-x86_64.sh
#RUN bazel-<0.4.5>-installer-linux-x86_64.sh --user
# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["bash"]
