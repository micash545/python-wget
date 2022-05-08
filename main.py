import urllib
import wget
import sys

def bar_progress(current, total, width=80):
    progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()

kupa = urllib.error.HTTPError

url = input('paste url')
save_path = "D:\python-wget"

try:
    wget.download(url, save_path, bar=bar_progress)

except Exception as e:
    print(e)




