

class Logger():
    def __init__(self,logger,file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.selfLevel(logging.DEBUG)

        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)] - [%(levelname)s] - [%(levelname)s]')

        curr_time = time.strftime("%Y-%m-%d")
        self.LogFileName = '.\\Logs\\log'+curr_time+'.txt'

        fh = logging.FileHandler(self.LogFileName,mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
