FROM python:3.11-slim

# Install git for cloning the private repo
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# Accept build arguments for GitHub credentials
ARG CHROMA_GITHUB_TOKEN
ARG CHROMADOCS_REPO=https://github.com/iwatkot/maps4fschromadocs.git

# Clone the private repository and extract chroma_db during build
RUN if [ -n "$CHROMA_GITHUB_TOKEN" ]; then \
        git clone --depth 1 https://${CHROMA_GITHUB_TOKEN}@github.com/iwatkot/maps4fschromadocs.git /tmp/chromadocs && \
        cp -r /tmp/chromadocs/chroma_db /usr/src/app/ && \
        rm -rf /tmp/chromadocs; \
    else \
        echo "ERROR: CHROMA_GITHUB_TOKEN is required to build this image" && \
        echo "Please provide it with: docker build --build-arg CHROMA_GITHUB_TOKEN=your_token ." && \
        exit 1; \
    fi

COPY maps4fsbot /usr/src/app/maps4fsbot
COPY requirements.txt /usr/src/app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH .:${PYTHONPATH}
ENV SKIP_CHROMA_DOWNLOAD="1"
ENV PYTHONUNBUFFERED=1
CMD ["python", "-m", "maps4fsbot.main"]