# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/
COPY ./static /app/static
COPY ./media /app/media


# Expose port 8000
EXPOSE 8000

# Run migrations and start the development server
RUN python manage.py collectstatic --noinput
RUN chown -R www-data:www-data /app/static /app/media /app/static_root /app/media_root
CMD ["./entrypoint.sh"]
