FROM amancevice/pandas:2.0.2-alpine

COPY . .

RUN apk --no-cache --update-cache add git
RUN pip3 install --no-cache-dir -r requirements.txt

ENV TRIALRUN=True
ENV EARLIESTDATE=1900-01-01
ENV LATESTDATE=2200-01-01
ENV SHORTESTEVENT=1

CMD ["python", "runHelpers.py"]