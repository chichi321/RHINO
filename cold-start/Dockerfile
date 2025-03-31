FROM alpine:latest

RUN apk add --no-cache bash
ARG FILE_SIZE=1000MB
RUN dd if=/dev/zero of=/dummyfile bs=${FILE_SIZE} count=1

CMD echo "Container started"; sleep 5; echo "Container is stopping"; exit 0