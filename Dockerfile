# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir fastapi uvicorn pandas scikit-learn

# Expose the port
EXPOSE 8000

# Start FastAPI app
CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]
