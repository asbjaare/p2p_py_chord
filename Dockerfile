From python:latest

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD [ "python", "p2p_node.py" ]
