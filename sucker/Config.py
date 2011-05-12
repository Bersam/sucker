import glib

class Config:
    def __init__(self):
        pass

    def get_default_download_dir(self):
        return glib.get_user_special_dir(glib.USER_DIRECTORY_DOWNLOAD)
