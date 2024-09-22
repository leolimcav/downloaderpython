# get item or list of items to be downloaded
# it seems the limit of downloads for the site is 6 concurrent downloads
# check if is possible to convert to GoD iso programatically

from threading import Thread
from asyncio import start

threadPool = Thread()