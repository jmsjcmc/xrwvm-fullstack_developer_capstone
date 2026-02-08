FROM python:3.12.0-slim-bookworm

ENV PYTHONBUFFERED 1
ENV PYTHONWRITEBYTECODE 1
ENV APP=/app

# Change the working directory
WORKDIR $APP

# Add the requirements file and install dependencies
COPY requirements.txt $APP
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt

# Copy the rest of the application files
COPY . $APP

# Expose the port your app runs on
EXPOSE 8000

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["/bin/bash", "/app/entrypoint.sh"]

# Default command to run the app
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
