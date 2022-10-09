#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'shiyinde'

import random
import multiprocessing
import time
import datetime
import sys
import os
from ping3 import ping

from read_write_file import Logger


class PingIP(multiprocessing.Process):

    def __init__(self, args):
        multiprocessing.Process.__init__(self)

        self.index = args[0]
        self.dict = {}
        # 传入的参数存入临时字典
        self.dict['process_name'] = args[1]['process_name']  # 进程名
        self.dict['whether_self_start'] = args[1]['whether_self_start']  # 是否自动启动
        self.dict['client_name'] = args[1]['client_name']  # 客户名
        self.dict['tq_account'] = args[1]['tq_account']  # 天勤账号
        self.dict['tq_psd'] = args[1]['tq_psd']  # 天勤密码
        self.dict['futures_company'] = args[1]['futures_company']  # 期货公司
        self.dict['futures_account'] = args[1]['futures_account']  # 期货实盘资金账号
        self.dict['futures_psd'] = args[1]['futures_psd']  # 期货实盘资金密码
        self.dict['symbol'] = args[1]['symbol']  # 合约代码
        self.dict['symbol_period'] = args[1]['symbol_period']  # 合约周期
        self.dict['strategy'] = args[1]['strategy']  # 策略名
        self.dict['whether_live_trading'] = args[1]['whether_live_trading']  # 是否为实盘
        self.dict['whether_backtest'] = args[1]['whether_backtest']  # 是不是回测进程
        self.dict['whether_open_web_services'] = args[1]['whether_open_web_services']  # 是否启动web服务
        self.dict['web_port'] = args[1]['web_port']  # web服务端口

        self.dict['trading_status'] = args[1]['trading_status']  # 交易状态标志位，默认True为正常交易，Flase为停止交易,可在策略中通过开关此位来停止或开启交易
        self.dict['orientation'] = args[1]['orientation']  # 交易方向
        self.dict['initial_capital'] = args[1]['initial_capital']  # 初始资金
        self.dict['final_capital'] = args[1]['final_capital']  # 最终资金
        self.dict['contract_multiples'] = args[1]['contract_multiples']  # 合约倍数
        self.dict['margin_rate'] = args[1]['margin_rate']  # 保证金率
        self.dict['stop_loss'] = args[1]['stop_loss']  # 止损点位
        self.dict['stop_profit'] = args[1]['stop_profit']  # 止盈点位

        self.dict['long_add_times'] = args[1]['long_add_times']  # 多头加仓次数
        self.dict['long_current_position'] = args[1]['long_current_position']  # 多头当前持仓
        self.dict['first_long_price'] = args[1]['first_long_price']  # 多头第一次加仓价格
        self.dict['first_long_deal'] = args[1]['first_long_deal']  # 多头第一次加仓数量
        self.dict['short_add_times'] = args[1]['short_add_times']  # 空头加仓次数
        self.dict['short_current_position'] = args[1]['short_current_position']  # 空头当前持仓
        self.dict['first_short_price'] = args[1]['first_short_price']  # 空头第一次加仓价格
        self.dict['first_short_deal'] = args[1]['first_short_deal']  # 空头第一次加仓数量

        self.dict['whether_open_line'] = args[1]['whether_open_line']  # 是否定义了开仓直线
        self.dict['open_line_Coordinates'] = args[1]['open_line_Coordinates']  # 开仓线坐标
        self.dict['whether_close_line'] = args[1]['whether_close_line']  # 是否定义了平仓直线
        self.dict['close_line_Coordinates'] = args[1]['close_line_Coordinates']  # 平仓线坐标

        self.dict['CP1'] = args[1]['CP1']  # 自定义参数1    Customized_parameters 为了方便使用,缩写为CP
        self.dict['CP2'] = args[1]['CP2']  # 自定义参数2
        self.dict['CP3'] = args[1]['CP3']  # 自定义参数3
        self.dict['CP4'] = args[1]['CP4']  # 自定义参数4
        self.dict['CP5'] = args[1]['CP5']  # 自定义参数5
        self.dict['CP6'] = args[1]['CP6']  # 自定义参数6
        self.dict['CP7'] = args[1]['CP7']  # 自定义参数7
        self.dict['CP8'] = args[1]['CP8']  # 自定义参数8

        # print('进程    ', self.dict['process_name'], '    传入的字典为:\n', self.dict, '\n\n')


    def ping_some_ip(self, host, src_addr=None):
        second = ping(host, src_addr=src_addr)
        return second


    def run(self):
        sys.stdout = Logger(process_name=str(self.dict['process_name']))  # 由 logger 类实例化的对象接管系统标准输出
        try:
            src_addr = None

            while True:

                print('PIng某个网站用来测试\n')
                print('子进程    ' + self.dict['process_name'] + '    正在执行。。。')
                print('当前子进程pid为:  ' + str(os.getpid()))
                result = self.ping_some_ip(str(self.dict['web_port']), src_addr)

                if result:
                    print('当前index为:', self.index, '\n')
                    print('当前进程为: ', self.dict['process_name'], '\n')
                    print('当前时间为: ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '\n')
                    print('ping --> ', self.dict['web_port'], '   成功,  耗时  ', result, '秒\n\n\n')

                else:
                    print('当前index为：', self.index, '\n')
                    print('当前进程为： ', self.dict['process_name'], '\n')
                    print('当前时间为:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '\n')
                    print('ping --> ', self.dict['web_port'], '  失败！\n\n\n')
                time.sleep(20)

        except Exception as ex:
            print('捕获异常: %r' % ex)
            sys.exit(1)  # 退出程序


if __name__ == '__main__':
    index = 0
    my_dict = {'process_name'          : '回测-{2022.08.01-20时01分}-pingTest-DCE.i2209-15min',  # 进程的名称，主要用于区分进程，还有日志文件的命名
            'client_name'              : '小白兔',  # 客户名称
            'tq_account'               : '信易帐户',  # 天勤账号
            'tq_psd'                   : '信易密码',  # 天勤密码
            'futures_company'          : 'Z中信建投',  # 期货公司
            'futures_account'          : '888888888',  # 实盘期货资金账号
            'futures_psd'              : '123456789',  # 实盘期货资金密码
            'symbol'                   : 'DCE.i2209',  # 合约代码
            'symbol_period'            : '15',  # 合约周期
            'strategy'                 : 'pingTest',  # 策略名称
            'whether_self_start'       : 'Ture',  # 是否自启动，此项只有为ture时，才会自启动，在config文件中将对应行的此项改为False，该进程就不会自启动
            'whether_live_trading'     : 'Flase',  # 是否是实盘交易
            'whether_backtest'         : 'Ture',  # 是否是回测
            'whether_open_web_services': 'True',  # 是否开启web服务
            'web_port'                 : 'www.hao123.com',  # web服务端口

            'trading_status'           : True,  # 交易状态标志位，默认True为正常交易，Flase为停止交易,可在策略中通过开关此位来停止或开启交易
            'orientation'              : '1',  # 交易方向，1为多，-1为空
            'initial_capital'          : '10000',  # 初始资金
            'final_capital'            : '10000',  # 最终资金
            'contract_multiples'       : '100',  # 合约乘数
            'margin_rate'              : '12',  # 保证金率
            'stop_loss'                : '3',  # 止损位
            'stop_profit'              : '20',  # 止盈位

            'long_add_times'           : 0,  # 多单加仓次数
            'long_current_position'    : 0,  # 多单当前持仓
            'first_long_price'         : 0,  # 多单第一次成交价格
            'first_long_deal'          : 0,  # 多单第一次成交数量
            'short_add_times'          : 0,  # 空单加仓次数
            'short_current_position'   : 0,  # 空单当前持仓
            'first_short_price'        : 0,  # 空单第一次成交价格
            'first_short_deal'         : 0,  # 空单第一次成交数量

            'whether_open_line'        : False,  # 是否定义了开仓直线
            'open_line_Coordinates'    : '0,0',  # 开仓线坐标
            'whether_close_line'       : False,  # 是否定义了平仓直线
            'close_line_Coordinates'   : '0,0',  # 平仓线坐标

            'CP1'  : '11',  # 自定义参数1    Customized_parameters 为了方便使用,缩写为CP
            'CP2'  : '22',  # 自定义参数2
            'CP3'  : '33',  # 自定义参数3
            'CP4'  : '44',  # 自定义参数4
            'CP5'  : '55',  # 自定义参数5
            'CP6'  : '66',  # 自定义参数6
            'CP7'  : '77',  # 自定义参数7
            'CP8'  : '88'  # 自定义参数8

    }

    backtest_start_date = '2021-09-10'
    backtest_end_date = '2022-03-14'

    # 定义一个元组，用于存储index，字典和回测日期, 这个元组会在进程类初始化的时候传入
    backtest_tuple = (index, my_dict, backtest_start_date, backtest_end_date)

    t = PingIP(args=backtest_tuple)  # 实例化进程类
    t.name = backtest_tuple[1]['process_name']  # 设置进程名称
    t.start()  # 启动进程
