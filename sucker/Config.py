import glib

class Config:
    def __init__(self):
        pass

    def get_default_download_dir(self):
        USER_DIRECTORY_DOWNLOAD = glib.get_user_special_dir(glib.USER_DIRECTORY_DOWNLOAD)
        if USER_DIRECTORY_DOWNLOAD == None:
            USER_DIRECTORY_DOWNLOAD = "~/Downloads"
            print _("USER_DIRECTORY_DOWNLOAD variable not found, Defaults to ~/Downloads")
        return USER_DIRECTORY_DOWNLOAD
