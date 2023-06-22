# Use the official MySQL image as the base image
FROM mysql:latest

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD almeidapewpew
ENV MYSQL_DATABASE db_test

# Copy the SQL script to create the table into the container
COPY personagens.sql /docker-entrypoint-initdb.d/
COPY locations.sql /docker-entrypoint-initdb.d/

# Expose the MySQL default port (3306)
EXPOSE 3306
