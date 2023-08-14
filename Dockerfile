FROM amancevice/pandas:alpine

COPY . .

RUN apk --no-cache --update-cache add git
RUN pip3 install --no-cache-dir -r requirements.txt

ENV TRIALRUN=True

CMD ["python", "runHelpers.py"]