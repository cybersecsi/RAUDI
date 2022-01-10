FROM golang:alpine AS builder
RUN apk update && apk add --no-cache alpine-sdk git 
RUN git clone https://github.com/blechschmidt/massdns.git && cd massdns && make && make install  
RUN go install github.com/d3mondev/puredns/v2@latest 

FROM alpine
COPY --from=builder /go/bin/puredns /usr/local/bin/puredns
COPY --from=builder /usr/local/bin/massdns /usr/local/bin/massdns
WORKDIR /current
ENTRYPOINT ["puredns"]