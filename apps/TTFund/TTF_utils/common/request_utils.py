import requests
import re
from bs4 import BeautifulSoup as bs
from apps.TTFund.TTF_utils.common.config_utils import local_config


class PositionGet(object):
    def __init__(self):
        pass

    def get_fund_position(self, fcode=161725, printcontrol=True):
        '''
            获取当前基金持仓dict
        :param fcode: 基金代码，自带转str
        :return: _dict
            {'fname': '易方达消费行业股票',
            'fcode': '110022',
            'fposition': {'1': ['000860', '顺鑫农业', '9.92%'],'2': ['600519', '贵州茅台', '9.52%'],
                        '3': ['000858', '五粮液', '9.46%'],'4': ['600809', '山西汾酒', '8.64%'],
                        '5': ['000333', '美的集团', '8.21%'],'6': ['000568', '泸州老窖', '8.17%'],
                        '7': ['000651', '格力电器', '7.55%'],'8': ['000596', '古井贡酒', '7.44%'],
                        '9': ['600887', '伊利股份', '2.45%'],'10': ['000423', '东阿阿胶', '2.44%'],
                        '11*': ['002032', '苏泊尔', '1.93%'],'12*': ['603833', '欧派家居', '1.67%']
                        }
            }
        '''
        url = str(local_config.position_url).replace('[]', str(fcode))
        content = requests.request('get', url, params=local_config.position_params)  # 使用查询持仓的params
        content_text = re.findall('content:"(.*?)",arryear', content.text)
        content_bs = bs(content_text[0], 'lxml')

        fname = content_bs.select('label', attrs={'class': 'left'})[0].find('a').text

        tr = content_bs.find('tbody').find_all('tr')
        _dict_inside = {}
        for i in tr:
            info = i.find_all('td')
            tor = (i.find_all('td', attrs={'class': 'tor'}))[2].text
            _dict_inside.update({info[0].text: [info[1].text, info[2].text, tor]})

        fposition = _dict_inside
        # 加*号代表进入上市公司的十大流通股东却没有进入单只基金前十大重仓股的个股。
        _dict = {'fname': fname, 'fcode': fcode, 'fposition': fposition}
        if printcontrol == True:
            print(_dict['fname'], _dict['fcode'])
            print(str(_dict['fposition']).replace('],', '],\n'))
        return _dict

    def get_today_data(self, fcode=161725, printcontrol=True):
        url = local_config.current_url.replace('*', fcode)
        content = requests.request('GET', url).text  # res.request('get', url)
        _data = re.findall('jsonpgz\((.*?)\);', str(content))[0]
        try:
            _dict = eval(_data)
            if printcontrol == True:
                print('fundcode:', _dict['fundcode'], 'name:', _dict['name'], 'requstDate:', _dict['jzrq'])
                print('单位/当前净值:', _dict['dwjz'], '今日估值', _dict['gsz'], '涨跌幅', _dict['gszzl'])
            return _dict
        except Exception as e:
            return {'fundcode': fcode, 'name': '', 'jzrq': '', 'dwjz': '', 'gsz': '', 'gszzl': ''}


if __name__ == '__main__':
    rep = PositionGet()
    _list = ['050027', '080002', '007844', '161720', '005176', '007345', '161907', '481012']
    for i in _list:
        data = rep.get_today_data(fcode=i, printcontrol=False)
        print(data['fundcode'], data['gszzl'], data['name'])
    print()
    _list = ['002611', '003634', '007460', '162411', '009360', '002385', '001562', '110003']
    for i in _list:
        data = rep.get_today_data(fcode=i, printcontrol=False)
        print(data['fundcode'], data['gszzl'], data['name'])
