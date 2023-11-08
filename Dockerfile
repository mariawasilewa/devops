# Use nginx:1.20-alpine as the base image
FROM nginx:1.20-alpine

# Copy the local index.html file to the nginx container
COPY index.html /usr/share/nginx/html/
