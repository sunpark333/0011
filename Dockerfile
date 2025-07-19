FROM python:3.10-slim-bullseye

# Install dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    git \
    curl \
    wget \
    bash \
    ffmpeg \
    neofetch \
    software-properties-common && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -U pip wheel && \
    pip3 install --no-cache-dir -U -r requirements.txt

COPY . .

EXPOSE 8080

# Run both commands (Flask and main.py)
CMD bash -c "flask run -h 0.0.0.0 -p 8080 & python3 main.py"
