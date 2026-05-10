# Use a slim Python image
FROM python:3.13-slim-bookworm

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/opt/venv/bin:$PATH"

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install uv for faster package management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uv/bin/uv
ENV PATH="/uv/bin:$PATH"

# Set working directory
WORKDIR /app

# Create a virtual environment
RUN uv venv /opt/venv

# Install dependencies
COPY requirements.txt .
RUN uv pip install -r requirements.txt

# Copy project code
COPY . .

# Create logs directory
RUN mkdir -p logs && chmod 777 logs

# Build-time environment variables for collectstatic
ARG SECRET_KEY="dummy-key-for-build-only"
ARG DATABASE_URL="sqlite:///:memory:"
ARG DEBUG="False"
ARG ALLOWED_HOSTS="*"
ARG CSRF_TRUSTED_ORIGINS="http://localhost:8000"

# Run collectstatic
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Start the application
CMD ["sh", "-c", "python manage.py migrate && gunicorn djangorenteasy.wsgi --bind 0.0.0.0:$PORT --log-file -"]
