import logging
import time

from base.get_path import Settings


class Logger:

    def __init__(self, logger, CmdLevel=logging.DEBUG, FileLevel=logging.DEBUG):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)  # 设置日志默认级别为DEBUG
        fmt = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] -%(levelname)s - %(message)s')
        curr_time = time.strftime("%Y%m%d", time.localtime(time.time()))  # 格式化当前时间
        path = Settings.LOG_DIR + '/'  # 日志目录地址
        log_name = path + logger + curr_time + '.log'  # 日志名
        # 设置输出的日志文件
        fh = logging.FileHandler(log_name, encoding='utf-8')
        fh.setFormatter(fmt)
        fh.setLevel(FileLevel)
        # 设置控制台显示的log
        sh = logging.StreamHandler(log_name)
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(CmdLevel)

    def __new__(cls, *args, **kwargs):
        if not hasattr(Logger, '_instance'):
            Logger._instance = object.__new__(cls)
        return Logger._instance

    def __call__(self, *args, **kwargs):
        return self.logger


if __name__ == '__main__':
    log = Logger('Base')()
    log.debug('asd')
