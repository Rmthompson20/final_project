# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container
COPY fetch_weather.py .

# Install dependencies
RUN pip install requests

# Run the Python script
CMD ["python", "fetch_weather.py"]

