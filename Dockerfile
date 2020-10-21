FROM python:3.6-alpine

EXPOSE 5060

WORKDIR /library
ADD ./ /library
RUN pip3 install -r requirements.txt 
RUN apk add gettext libintl

CMD "/library/docker_start.sh"
