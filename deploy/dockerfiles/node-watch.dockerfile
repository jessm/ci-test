FROM node:16.17.1

WORKDIR /app
COPY package*.json ./

RUN npm install

CMD npm run watch
