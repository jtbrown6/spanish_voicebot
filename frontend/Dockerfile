# Use an official Node.js runtime as a parent image
FROM node:16

# Set the working directory in the container
WORKDIR /usr/src/app

# Add metadata to the image (optional)
LABEL maintainer="JamalBrown" \
      version="1.0"

# Copy the current directory contents into the container at /app
COPY . /usr/src/app

# Install any needed packages specified in package.json
RUN yarn install --exact

# Expose port 5173
EXPOSE 5173

# Run yarn dev when the container launches
CMD ["yarn", "dev"]
