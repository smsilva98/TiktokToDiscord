FROM python:buster

ENV PYTHONUNBUFFERED 1

# active the python virtual environment, might not be needed
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# install bs4, selenium, pydantic and aiohttp with optional speedup packages
RUN python -m pip install --upgrade pip
COPY requirements.txt /requirements.txt
RUN python -m pip install -r requirements.txt

# set the working directory and copy the source code
COPY . ./home/TiktokToDiscord/
WORKDIR ./home/TiktokToDiscord

STOPSIGNAL SIGTERM
ENTRYPOINT ["python", "main.py"]