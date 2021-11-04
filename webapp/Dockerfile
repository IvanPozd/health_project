FROM ubuntu:latest

RUN sudo apt get update && sudo apt get upgrade -y
RUN sudo apt install -y python-pip
RUN sudo apt install -y python-dev
RUN sudo apt install -y build-essential

COPY . /app
WORKDIR /app
RUN pip install -r requirments.txt
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]