# 
FROM node:alpine

WORKDIR /app

RUN npm i npm@latest -g

COPY package.json ./
COPY package-lock.json ./

# Run `npm ci` to install project dependencies
RUN npm ci

# Set environment variables
ENV CI=true
ENV PORT=3000

# Copy the entire project directory to the image
COPY . .