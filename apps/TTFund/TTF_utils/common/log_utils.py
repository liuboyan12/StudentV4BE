# -*- coding: utf-8 -*-
# @Time    : 2020/5/14/014 16:32
# @Author  : Aliun
# @Email   : 594303711@qq.com
# @File    : log_utils.py
# @Software: PyCharm

import os
import logging
import time
from apps.TTFund.TTF_utils.common.config_utils import local_config

current_path = os.path.dirname(__file__)  # 获取路径
log_path = os.path.join(current_path, '../TTF_logs/log.txt')


class LogUtils:
    def __init__(self, logger=None):
        self.log_path = os.path.join(os.path.dirname(__file__), '../', local_config.log_path)
        self.log_file_path = os.path.join(os.path.dirname(__file__), '../logs')
        self.log_name = os.path.join(self.log_path, 'UITest_%s.log' % time.strftime("%Y-%m-%dT%H:%M:%S"))
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(local_config.log_level)
        self.fh = logging.FileHandler(self.log_file_path, 'a', encoding='utf-8')
        self.fh.setLevel(local_config.log_level)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(local_config.log_level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(formatter)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)
        self.fh.close()
        self.ch.close()

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def get_log(self):
        return self.logger

logger = LogUtils()

if __name__ == '__main__':
    pass
