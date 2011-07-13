import glib

class Config:
    def __init__(self):
        pass

    def get_default_download_dir(self):
        USER_DIRECTORY_DOWNLOAD = glib.get_user_special_dir(glib.USER_DIRECTORY_DOWNLOAD)
        return USER_DIRECTORY_DOWNLOAD
