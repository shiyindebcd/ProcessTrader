#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'shiyinde'

from tqsdk import TqApi, TargetPosTask, TqKq, TqAuth, TqAccount, TqSim, TqBacktest, tafunc
import time
from datetime import date
import multiprocessing
import sys
import os

from read_write_file import ReadWriteCsv, Logger


class demo(multiprocessing.Process):
    def __init__(self, args):
        multiprocessing.Process.__init__(self)

        self.RWcsv = ReadWriteCsv() # 创建读写csv文件的对象
        self.path = './data/config.csv' # 配置文件路径，在策略向config.csv写入数据时，会用到该路径

        self.index = args[0]
        self.dict = {}
        # 传入的参数存入临时字典
        self.dict['process_name'] = args[1]['process_name']                         # 进程名
        self.dict['whether_self_start'] = args[1]['whether_self_start']             # 是否自动启动
        self.dict['client_name'] = args[1]['client_name']                           # 客户名
        self.dict['tq_account'] = args[1]['tq_account']                             # 天勤账号
        self.dict['tq_psd'] = args[1]['tq_psd']                                     # 天勤密码
        self.dict['futures_company'] = args[1]['futures_company']                   # 期货公司
        self.dict['futures_account'] = args[1]['futures_account']                   # 期货实盘资金账号
        self.dict['futures_psd'] = args[1]['futures_psd']                           # 期货实盘资金密码
        self.dict['symbol'] = args[1]['symbol']                                     # 合约代码
        self.dict['symbol_period'] = args[1]['symbol_period']                       # 合约周期
        self.dict['strategy'] = args[1]['strategy']                                 # 策略名
        self.dict['whether_live_trading'] = args[1]['whether_live_trading']         # 是否为实盘
        self.dict['whether_backtest'] = args[1]['whether_backtest']                 # 是不是回测进程
        self.dict['whether_open_web_services'] = args[1]['whether_open_web_services']         # 是否启动web服务
        self.dict['web_port'] = args[1]['web_port']                                 # web服务端口

        self.dict['trading_status'] = args[1]['trading_status']  # 交易状态标志位，默认True为正常交易，Flase为停止交易,可在策略中通过开关此位来停止或开启交易
        self.dict['orientation'] = args[1]['orientation']                           # 交易方向
        self.dict['initial_capital'] = args[1]['initial_capital']                   # 初始资金
        self.dict['final_capital'] = args[1]['final_capital']                       # 最终资金
        self.dict['contract_multiples'] = args[1]['contract_multiples']             # 合约倍数
        self.dict['margin_rate'] = args[1]['margin_rate']                           # 保证金率
        self.dict['stop_loss'] = args[1]['stop_loss']                               # 止损点位
        self.dict['stop_profit'] = args[1]['stop_profit']                           # 止盈点位
        
        self.dict['long_add_times'] = args[1]['long_add_times']                     # 多头加仓次数
        self.dict['long_current_position'] = args[1]['long_current_position']       # 多头当前持仓
        self.dict['first_long_price'] = args[1]['first_long_price']                 # 多头第一次加仓价格
        self.dict['first_long_deal'] = args[1]['first_long_deal']                   # 多头第一次加仓数量
        self.dict['short_add_times'] = args[1]['short_add_times']                   # 空头加仓次数
        self.dict['short_current_position'] = args[1]['short_current_position']     # 空头当前持仓
        self.dict['first_short_price'] = args[1]['first_short_price']               # 空头第一次加仓价格
        self.dict['first_short_deal'] = args[1]['first_short_deal']                 # 空头第一次加仓数量

        self.dict['whether_open_line'] = args[1]['whether_open_line']                # 是否定义了开仓直线
        self.dict['open_line_Coordinates'] = args[1]['open_line_Coordinates']        # 开仓线坐标
        self.dict['whether_close_line'] = args[1]['whether_close_line']              # 是否定义了平仓直线
        self.dict['close_line_Coordinates'] = args[1]['close_line_Coordinates']      # 平仓线坐标
        
        self.dict['CP1'] = args[1]['CP1']   # 自定义参数1    Customized_parameters 为了方便使用,缩写为CP
        self.dict['CP2'] = args[1]['CP2']   # 自定义参数2
        self.dict['CP3'] = args[1]['CP3']   # 自定义参数3
        self.dict['CP4'] = args[1]['CP4']   # 自定义参数4
        self.dict['CP5'] = args[1]['CP5']   # 自定义参数5
        self.dict['CP6'] = args[1]['CP6']   # 自定义参数6
        self.dict['CP7'] = args[1]['CP7']   # 自定义参数7
        self.dict['CP8'] = args[1]['CP8']   # 自定义参数8

        if len(args) > 2:   # 判断传入的元组是否有第三第四项参数，回测时才有第三第四项，不回测的情况下只有第一第二项
            self.backtest_start_date = args[2]                      # 回测开始日期,传入的是一个 '2022-03-03' 格式的字符串
            self.backtest_end_date = args[3]  

        print('进程    ', self.dict['process_name'], '    传入的字典为:\n', self.dict, '\n\n')
                         
    def create_api_by_situation(self):  # 根据不同情况创建不同的api

        self.kline_period = 60 * int(self.dict['symbol_period'])    # K线周期 分钟数
        
        if self.dict['whether_open_web_services'] == 'True':  # 判断是否启用了web服务
            self.port = ':' + str(self.dict['web_port'])                # 网页端口前面加 ：
        else:
            pass

        if self.dict['whether_backtest'] == 'True':                   # 如果whether_backtest为True，则创建回测api       

            # 从传进来的回测时间字符串中分别提取出年月日，并转换为时间戳，用于后面的回测
            self.start_date_Y = int(self.backtest_start_date[0:4])
            if self.backtest_start_date[5] == '0':                  # 月份和日期都是两位数，所以要判断一下，第一位如果为0，就光取后面一位，转为int型，以下几行同理
                self.start_date_M = int(self.backtest_start_date[6])
            else:
                self.start_date_M = int(self.backtest_start_date[5:7])
            if self.backtest_start_date[8] == '0':
                self.start_date_D = int(self.backtest_start_date[9])
            else:
                self.start_date_D = int(self.backtest_start_date[8:10])

            self.end_date_Y = int(self.backtest_end_date[0:4])
            if self.backtest_end_date[5] == '0':
                self.end_date_M = int(self.backtest_end_date[6])
            else:
                self.end_date_M = int(self.backtest_end_date[5:7])
            if self.backtest_end_date[8] == '0':
                self.end_date_D = int(self.backtest_end_date[9])
            else:
                self.end_date_D = int(self.backtest_end_date[8:10])

            if self.dict['whether_open_web_services'] == 'True':  # 判断是否启用了web服务
                self.api = TqApi(   # 启用web服务的情况下回测
                    TqSim(init_balance=int(self.dict['initial_capital'])), web_gui=str(self.port),
                    backtest=TqBacktest(start_dt=date(self.start_date_Y, self.start_date_M, self.start_date_D), end_dt=date(self.end_date_Y, self.end_date_M, self.end_date_D)),
                    auth=TqAuth(self.dict['tq_account'], self.dict['tq_psd']),
                )
                print('\n\n当前为回测模式，web服务已启用，端口为：', self.dict['web_port'], '\n\n')
            else:
                self.api = TqApi(   # 不启用web服务的情况下回测
                    TqSim(init_balance=int(self.dict['initial_capital'])),
                    backtest=TqBacktest(start_dt=date(self.start_date_Y, self.start_date_M, self.start_date_D), end_dt=date(self.end_date_Y, self.end_date_M, self.end_date_D)),
                    auth=TqAuth(self.dict['tq_account'], self.dict['tq_psd']),
                )
                print('\n\n当前为回测模式，web服务未启用\n\n')
        else:

            if self.dict['whether_open_web_services'] == 'True':  # 启用了web服务的情况下，创建实盘和模拟盘api

                if self.dict['whether_live_trading'] == 'True':     # 如果whether_live_trading为True，则创建实盘交易api
                    self.api = TqApi(TqAccount(self.dict['futures_company'], self.dict['futures_account'], self.dict['futures_psd']), web_gui=str(self.port), auth=TqAuth(self.dict['tq_account'], self.dict['tq_psd']))
                    print('\n\n当前为实盘模式，web服务已启用，端口为：', self.dict['web_port'], '\n\n')
                else:                                               # 非回测和实盘时，创建模拟盘交易api
                    self.api = TqApi(TqKq(), web_gui=str(self.port), auth=TqAuth(self.dict['tq_account'], self.dict['tq_psd']))
                    print('\n\n当前为模拟盘模式，web服务已启用，端口为：', self.dict['web_port'], '\n\n')
            else:                                                # 不启用web服务的情况下，创建模拟盘交易api
                if self.dict['whether_live_trading'] == 'True':     # 如果whether_live_trading为True，则创建实盘交易api
                    self.api = TqApi(TqAccount(self.dict['futures_company'], self.dict['futures_account'], self.dict['futures_psd']), auth=TqAuth(self.dict['tq_account'], self.dict['tq_psd']))
                    print('\n\n当前为实盘模式，web服务未启用\n\n')
                else:                                               # 非回测和非实盘时，创建模拟盘交易api
                    self.api = TqApi(TqKq(), auth=TqAuth(self.dict['tq_account'], self.dict['tq_psd']))
                    print('\n\n当前为模拟盘模式，web服务未启用\n\n')

        self.quote = self.api.get_quote(self.dict['symbol'])
        self.klines = self.api.get_kline_serial(self.dict['symbol'], duration_seconds=self.kline_period, data_length=300)

        self.target_pos = TargetPosTask(self.api, symbol=self.dict['symbol'])
        self.account = self.api.get_account()
        self.position = self.api.get_position(self.dict['symbol'])

        # print('\n获取的kline数据为:\n\n', self.klines, '\n\n')    



    def run(self):  #重写Process类的run函数，你所有的天勤代码都要放在这个函数里面

        sys.stdout = Logger(process_name=self.dict['process_name']) # 由Logger实例化后的对象接管系统标准输出，加了这一句进程才会自动保存log
        self.create_api_by_situation()                             # 按不同情形创建api

        try:        # 循环语句最好放在try里面，如果有异常，直接结束进程即可，以免出现僵尸进程，进程结束后，主进程会在60秒后重启该进程
            while True:

                print(self.klines)
                self.api.wait_update()

                # 这里写你代码中的循环部分
                # 这里写你代码中的循环部分
                # 这里写你代码中的循环部分

                

        except Exception as ex:
            print("exception catched: %r" % ex)
            sys.exit(1)



my_dict = {

        'process_name': '回测-{2022.08.01-20时01分}-pingTest-DCE.i2209-15min',   # 进程的名称，主要用于区分进程，还有日志文件的命名
        'whether_self_start': 'True',   # 是否自启动，此项只有为ture时，才会自启动，在config文件中将对应行的此项改为False，该进程就不会自启动
        # 回测进程的命名规则：回测-{日期}-策略名-合约-周期，调试时可以自己任意设置，回测log就保存在这个文件夹下
        'client_name': '小白兔',                                                 # 客户名称
        'tq_account': '信易帐户',                                                # 天勤账号
        'tq_psd': '信易密码',                                                    # 天勤密码
        'futures_company': 'Z中信建投',                                          # 期货公司
        'futures_account': '888888888',                                         # 实盘期货资金账号
        'futures_psd': '123456789',                                             # 实盘期货资金密码
        'symbol': 'DCE.i2209',                                                  # 合约代码
        'symbol_period': '15',                                                  # 合约周期
        'strategy': 'pingTest',                                                 # 策略名称
        'whether_live_trading': 'Flase',                                        # 是否是实盘交易
        'whether_backtest': 'True',                                             # 是否是回测
        'whether_open_web_services': 'True',                                    # 是否开启web服务
        'web_port': '9999',                                                     # web服务端口

        'trading_status' : True,  # 交易状态标志位，默认True为正常交易，Flase为停止交易,可在策略中通过开关此位来停止或开启交易
        'orientation': '1',                                                     # 交易方向，1为多，-1为空
        'initial_capital': '10000',                                             # 初始资金
        'final_capital': '10000',                                               # 最终资金
        'contract_multiples': '100',                                            # 合约乘数
        'margin_rate': '12',                                                    # 保证金率
        'stop_loss': '3',                                                       # 止损位
        'stop_profit': '20',                                                    # 止盈位

        'long_add_times': 0,                                                    # 多单加仓次数
        'long_current_position': 0,                                             # 多单当前持仓
        'first_long_price': 0,                                                  # 多单第一次成交价格
        'first_long_deal': 0,                                                   # 多单第一次成交数量
        'short_add_times': 0,                                                   # 空单加仓次数
        'short_current_position': 0,                                            # 空单当前持仓
        'first_short_price': 0,                                                 # 空单第一次成交价格
        'first_short_deal': 0,                                                  # 空单第一次成交数量

        'whether_open_line'     : False,                                        # 是否定义了开仓直线
        'open_line_Coordinates' : '0,0',                                        # 开仓线坐标
        'whether_close_line'    : False,                                        # 是否定义了平仓直线
        'close_line_Coordinates': '0,0',                                        # 平仓线坐标

        'CP1': '11',                                        # 自定义参数1    Customized_parameters 为了方便使用,缩写为CP
        'CP2': '22',                                        # 自定义参数2
        'CP3': '33',                                        # 自定义参数3
        'CP4': '44',                                        # 自定义参数4
        'CP5': '55',                                        # 自定义参数5
        'CP6': '66',                                        # 自定义参数6
        'CP7': '77',                                        # 自定义参数7
        'CP8': '88'                                         # 自定义参数8

}
if __name__ == '__main__':
    index = 0

    backtest_start_date = '2021-09-10'
    backtest_end_date = '2022-03-14'

    # 定义一个元组，用于存储index，字典和回测日期, 这个元组会在进程类初始化的时候传入
    backtest_tuple = (index, my_dict, backtest_start_date, backtest_end_date)

    t = demo(args=backtest_tuple)      # 实例化进程类
    t.name = backtest_tuple[1]['process_name']    # 设置进程名称
    t.start()                                            # 启动进程
