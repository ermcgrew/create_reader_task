FROM --platform=linux/amd64 alpine:latest
RUN apk add --no-cache bash \  
    python3 \
    py-pip \
 && pip install flywheel-gear-toolkit flywheel-sdk --break-system-packages \  
 && rm -rf /var/cache/apk/\*  

ENV FLYWHEEL=/flywheel/v0 

RUN mkdir -p ${FLYWHEEL}
COPY run.py ${FLYWHEEL}/run.py 

ENTRYPOINT ["python run.py"]