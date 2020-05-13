import os
import configparser

current_dir = os.path.abspath(os.path.dirname(__file__))
config_path = os.path.join(current_dir, "..", 'conf', "config.ini")


class ConfigUtils(object):
    def __init__(self, path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(path)

    @property
    def ENGINE(self):
        return self.cfg.get('DATABASES', 'ENGINE')

    @property
    def NAME(self):
        return self.cfg.get('DATABASES', 'NAME')

    @property
    def USER(self):
        return self.cfg.get('DATABASES', 'USER')

    @property
    def PASSWORD(self):
        return self.cfg.get('DATABASES', 'PASSWORD')

    @property
    def HOST(self):
        return self.cfg.get('DATABASES', 'HOST')

    @property
    def PORT(self):
        return self.cfg.get('DATABASES', 'PORT')


local_config = ConfigUtils()

if __name__ == '__main__':
    config = ConfigUtils()
    print(type(local_config.ENGINE), local_config.ENGINE)
    print(type(local_config.NAME), local_config.NAME)
    print(type(local_config.USER), local_config.USER)
    print(type(local_config.PASSWORD), local_config.PASSWORD)
    print(type(local_config.HOST), local_config.HOST)
    print(type(local_config.PORT), local_config.PORT)
    print(config_path)
