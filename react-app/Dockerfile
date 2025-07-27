# Use Node.js 18 Alpine as base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . .

# Expose port 3000
EXPOSE 3000

# Set environment variable to allow connections from any host
ENV WATCHPACK_POLLING=true
ENV CHOKIDAR_USEPOLLING=true
ENV HOST=0.0.0.0

# Start the React development server
CMD ["npm", "start"] 