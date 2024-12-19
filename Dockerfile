FROM amancevice/pandas:alpine-2.2.2

COPY . .

RUN apk --no-cache --update-cache add git
RUN pip3 install --no-cache-dir -r requirements.txt

# This makes print statements show up in the logs API
ENV PYTHONUNBUFFERED=1

ENV TRIALRUN=True
ENV SHORTESTEVENT=1
ENV DISABLEEMAIL=True

CMD ["python", "-u", "runHelpers.py"]