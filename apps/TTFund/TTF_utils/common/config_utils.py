import os
import configparser


class ConfigUtils(object):
    def __init__(self, conf_path='../config/local_config.ini'):
        self.current_path = os.path.dirname(__file__)
        self.conf_path = os.path.join(self.current_path, conf_path)
        self.conf = configparser.ConfigParser()
        self.conf_data = self.conf.read(self.conf_path, encoding='utf-8')

    def tprint(self, name, value):
        print(name, type(value), value)

    def read_test_def(self):
        self.tprint('self.current_path', self.current_path)
        self.tprint('self.conf_path', self.conf_path)
        self.tprint('self.conf_data', self.conf_data)


if __name__ == '__main__':
    c = ConfigUtils()
    c.read_test_def()
