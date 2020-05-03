FROM alpine:latest
COPY /web /web
WORKDIR /web/api
RUN apk add --update python3 && \
  pip3 install --upgrade pip
RUN pip3 install -r /web/requirements.txt
ENTRYPOINT ["python3"]
CMD ["/web/api/app.py"]
