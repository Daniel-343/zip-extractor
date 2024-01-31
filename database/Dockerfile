# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables for PostgreSQL user credentials
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Copy the SQL script to initialize the database
COPY create.sql /docker-entrypoint-initdb.d/
