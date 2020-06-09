import os
import configparser


class ConfigUtils(object):
    def __init__(self, conf_path='../config/config.ini'):
        self.current_path = os.path.dirname(__file__)
        self.conf_path = os.path.join(self.current_path, conf_path)
        self.conf = configparser.ConfigParser()
        self.conf_data = self.conf.read(self.conf_path, encoding='utf-8')

    def tprint(self, name, value):
        print(name, type(value), value)

    def read_test_def(self):
        # self.tprint('self.current_path', self.current_path)
        # self.tprint('self.conf_path', self.conf_path)
        # self.tprint('self.conf_data', self.conf_data)
        pass

    @property
    def current_url(self):
        '''
            今日数据请求地址
        '''
        return self.conf.get('url', 'current_url')

    @property
    def all_code_url(self):
        '''
            所有可以查询的基金列表
        '''
        return self.conf.get('url', 'all_code_url')

    @property
    def full_info_url(self):
        '''
            基金详情
        '''
        return self.conf.get('url', 'full_info_url')

    @property
    def log_level(self):
        '''
            log等级
        '''
        return self.conf.get('logs', 'log_level')

    @property
    def position_url(self):
        '''
            持仓查询的url
        '''
        return self.conf.get('position_request', 'URL')

    @property
    def position_params(self):
        '''
            持仓查询的params
        '''
        _params_dict = {
            'Accept': self.conf.get('position_request','Accept'),
            'Accept-Encoding': self.conf.get('position_request','Accept-Encoding'),
            'Accept-Language': self.conf.get('position_request','Accept-Language'),
            'Connection': self.conf.get('position_request','Connection'),
            'Host': self.conf.get('position_request','Host'),
            'User-Agent': self.conf.get('position_request','User-Agent'),
        }
        return _params_dict


local_config = ConfigUtils()

if __name__ == '__main__':
    c = ConfigUtils()
    c.read_test_def()
    print(c.current_url)
