FROM node:18-alpine

COPY package.json package.json
COPY package-lock.json package-lock.json

# Same as npm install
RUN npm ci

ENV CI=true
ENV PORT=3000

COPY . .

CMD [ "npm", "start" ]