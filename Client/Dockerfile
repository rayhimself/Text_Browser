FROM python

RUN pip3 install bs4
RUN pip3 install requests
RUN pip3 install flask
WORKDIR /home
COPY . .
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
EXPOSE 5000