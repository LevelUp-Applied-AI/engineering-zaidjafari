# Docker Notes — Day 9

## Docker Version
[انسخ ناتج أمر docker version هنا]

## Hello World Test
[انسخ ناتج أمر docker run hello-world هنا]

## Postgres Container

Command used:
```bash
docker run -d \
  --name pg-prework \
  -e POSTGRES_PASSWORD=prework \
  -p 5432:5432 \
  postgres:15-alpine 