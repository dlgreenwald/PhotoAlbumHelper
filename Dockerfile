FROM amancevice/pandas:2.0.2-alpine

COPY . .

RUN apk --no-cache --update-cache add git
RUN pip3 install --no-cache-dir -r requirements.txt

ENV TRIALRUN=True
ENV SHORTESTEVENT=1
ENV DISABLEEMAIL=True

CMD ["python", "runHelpers.py"]