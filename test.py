import pickle
import asyncio
from main import main
from config import Settings

# End-to-end live test (will fail if one video is removed)

settings = Settings()

with open('urls.pickle', 'rb') as fd:
    urls: set = pickle.load(fd)

assert urls.issubset(asyncio.run(main(settings.username, settings.webdriver_port)))
