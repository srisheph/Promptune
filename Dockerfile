# Use the official Python image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the project files into the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port (optional, in case of a web service)
EXPOSE 5000  

# Command to run the application
CMD ["python", "main.py"]
