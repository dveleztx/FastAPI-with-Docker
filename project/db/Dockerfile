# Pull Official Base Image
FROM postgres:13-alpine

# Run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
