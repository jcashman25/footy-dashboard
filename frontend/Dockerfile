FROM node:20-alpine

WORKDIR /app

COPY . .

RUN npm install

CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]