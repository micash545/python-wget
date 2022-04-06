import wget
import sys

def bar_progress(current, total, width=80):
    progress_message = "Downloading: %d%% [%d / %d] bytes" % (current / total * 100, current, total)
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()


url = 'https://download.jetbrains.com/python/pycharm-community-2021.3.3.exe'
save_path = "D:\python wget"
wget.download(url, save_path, bar=bar_progress)
