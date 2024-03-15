# To pull your base image
FROM python:3.9-slim

# Current working dir
WORKDIR /app

# install required packages for system
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install application dependencies
RUN pip install Flask==2.0.1
RUN pip install Flask-MySQLdb==0.2.0
RUN pip install requests==2.26.0
RUN pip install Werkzeug==2.2.2
RUN pip install psycopg2-binary


# Copying application code
COPY . .

# Entry point for the application
CMD ["python", "app.py"]