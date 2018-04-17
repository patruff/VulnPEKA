# Use an official Python runtime as a parent image
FROM python:3.6-slim

# Set the working directory to /vulnapp
WORKDIR /vulnapp

# Copy the current directory contents into the container at /vulnapp
ADD . /vulnapp

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define environment variable
ENV NAME World

# Run vulnapp.py when the container launches
CMD ["python", "vulnapp.py"]
