import time

class DataBase:
    def __init__(self):
        pass

    def create_new_id(self):
        id = time.strftime('%y%m%d%H%M%S', time.gmtime())
        return (int(id))
