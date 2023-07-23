# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install Nginx and certbot
RUN apt-get update && \
    apt-get install -y nginx certbot python3-certbot-nginx && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install gunicorn
RUN pip install gunicorn

# Install all requirements
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80 443

# Run main.py when the container launches
CMD ["gunicorn", "-b", ":8000", "main:app"]