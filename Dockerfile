FROM node:22-alpine AS base
WORKDIR /app
RUN apk add --no-cache dumb-init
COPY package*.json ./

FROM base AS deps
RUN npm ci --only=production

FROM base AS dev-deps
RUN npm install

FROM base AS dev
COPY --from=dev-deps /app/node_modules ./node_modules
COPY . .
EXPOSE 4321
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD node -e "require('http').get('http://localhost:4321', (r) => {if (r.statusCode !== 200) throw new Error(r.statusCode)})"
ENTRYPOINT ["dumb-init", "--"]
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

FROM deps AS build
COPY . .
RUN npm run build

FROM nginx:alpine AS production
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD wget --quiet --tries=1 --spider http://localhost/ || exit 1
CMD ["nginx", "-g", "daemon off;"]
