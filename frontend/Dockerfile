FROM node:16-buster

WORKDIR /app

COPY package*.json /app/
RUN npm install
RUN chown node:node /app/node_modules

EXPOSE 3000
