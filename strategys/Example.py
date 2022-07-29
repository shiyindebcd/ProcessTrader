# coding:utf-8
import multiprocessing
import time
import sys
import os
import random

from tqsdk import TargetPosTask, TqApi, TqSim, TqAuth, TqKq, TqAccount, TqBacktest

from read_write_file import Logger

# 策略示例，用来演示在本框架中如何写天勤策略


class Example(multiprocessing.Process):
    def __init__(self, args):
        multiprocessing.Process.__init__(self)

        self.index = args[0]
        self.dict = {}
        # 传入的参数存入临时字典
        self.dict['process_name'] = args[1]['process_name']
        self.dict['client_name'] = args[1]['client_name']
        self.dict['tq_account'] = args[1]['tq_account']
        self.dict['tq_psd'] = args[1]['tq_psd']
        self.dict['futures_company'] = args[1]['futures_company']
        self.dict['futures_account'] = args[1]['futures_account']
        self.dict['futures_psd'] = args[1]['futures_psd']
        self.dict['symbol'] = args[1]['symbol']
        self.dict['symbol_period'] = args[1]['symbol_period']
        self.dict['strategy'] = args[1]['strategy']
        self.dict['whether_self_start'] = args[1]['whether_self_start']
        self.dict['whether_live_trading'] = args[1]['whether_live_trading']
        self.dict['whether_backtest'] = args[1]['whether_backtest']
        self.dict['whether_web_services'] = args[1]['whether_web_services']
        self.dict['web_port'] = args[1]['web_port']

        self.dict['stop_trading'] = args[1]['stop_trading']
        self.dict['orientation'] = args[1]['orientation']
        self.dict['initial_capital'] = args[1]['initial_capital']
        self.dict['final_capital'] = args[1]['final_capital']
        self.dict['contract_multiples'] = args[1]['contract_multiples']
        self.dict['margin_rate'] = args[1]['margin_rate']
        self.dict['stop_loss'] = args[1]['stop_loss']
        self.dict['stop_profit'] = args[1]['stop_profit']
        self.dict['long_add_times'] = args[1]['long_add_times']
        self.dict['long_current_position'] = args[1]['long_current_position']
        self.dict['first_long_price'] = args[1]['first_long_price']
        self.dict['first_long_deal'] = args[1]['first_long_deal']
        self.dict['short_current_position'] = args[1]['short_current_position']
        self.dict['short_add_times'] = args[1]['short_add_times']
        self.dict['first_short_price'] = args[1]['first_short_price']
        self.dict['first_short_deal'] = args[1]['first_short_deal']
        self.dict['N1'] = args[1]['N1']
        self.dict['N2'] = args[1]['N2']
        self.dict['N3'] = args[1]['N3']
        self.dict['N4'] = args[1]['N4']
        self.dict['N5'] = args[1]['N5']
        self.dict['N6'] = args[1]['N6']            


    def run(self):

        self.kline_period = 60 * int(self.dict['symbol_period'])    # K线周期 分钟数
        self.port = ':' + str(self.dict['web_port'])                # 网页端口前面加 ：
                                                    
        self.api = TqApi(TqKq(), web_gui=str(self.port), auth=TqAuth(self.dict['tq_account'], self.dict['tq_psd']))

        self.quote = self.api.get_quote(self.dict['symbol'])
        self.klines = self.api.get_kline_serial(self.dict['symbol'], duration_seconds=self.kline_period, data_length=300)

        print('当前为模拟盘模式')
        self.target_pos = TargetPosTask(self.api, symbol=self.dict['symbol'])
        self.account = self.api.get_account()
        self.position = self.api.get_position(self.dict['symbol'])

        print('当前账户余额：%s' % self.account.balance)
            
        sys.stdout = Logger(process_name=self.dict['process_name'])
        
        try:
            while True:
                self.api.wait_update()
                if self.api.is_changing(self.klines):
                    print('K线数据更新')
        except Exception as ex:
            print("exception catched: %r" % ex)
            sys.exit(1)


if __name__ == '__main__':
    index = 0
    my_dict = {
                "process_name": "张三@zhangsan@PUBU_five@DCE.c2205@15min",
                "client_name": "张三",
                "tq_account": "shiyindebcd",
                "tq_psd": "shiyinde1234TQ",                
                "futures_company": "Y银河期货",
                "futures_account": 4562132,
                "futures_psd": "zhangsan8888",
                "symbol": "DCE.i2209",
                "symbol_period": 15,
                "strategy": "PUBU_five",
                "whether_self_start": True,
                "whether_live_trading": False,
                # 'whether_backtest': True,
                "whether_backtest": False,
                "whether_web_services": True,
                "web_port": "9999",
                "stop_trading": 0,
                "orientation": 0,
                "initial_capital": 100000,
                "final_capital": 100000,
                "contract_multiples": 10,
                "margin_rate": 12,
                "stop_loss": 3,
                "stop_profit": 10,
                "long_add_times": 0,
                "long_current_position": 0,
                "first_long_price": 0,
                "first_long_deal": 0,
                "short_add_times": 0,
                "short_current_position": 0,
                "first_short_price": 0,
                "first_short_deal": 0,
                "N1": 0,
                "N2": 0,
                "N3": 0,
                "N4": 0,
                "N5": 0,
                "N6": 0,
                }


    backtest_start_date = '2021-09-10'
    backtest_end_date = '2022-03-14'

    # 定义一个元组，用于存储index，字典和回测日期, 这个元组会在进程类初始化的时候传入
    backtest_tuple = (index, my_dict, backtest_start_date, backtest_end_date)

    t = Example(args=backtest_tuple)      # 实例化进程类
    t.name = backtest_tuple[1]['process_name']    # 设置进程名称
    t.start()                                     # 启动进程