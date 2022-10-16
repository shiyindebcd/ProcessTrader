#!/usr/bin/env python
#  -*- coding: utf-8 -*-
__author__ = 'shiyinde'


from multiprocessing import Process, Manager
import time
import datetime
import sys
import os
import pandas as pd
from tqsdk import TqApi, TqKq, TqSim, TqAuth
from read_write_file import ReadWriteCsv, Logger
import asyncio



class TQServices(Process):

    def __init__(self, args):
        Process.__init__(self)
        self.self_selection_list = args[0]      # 和主程序共享的自选列表
        self.quote_dict = args[1]               # 和主程序共享的行情切片
        self.current_Contracts = args[2]        # 和主程序共享的当前显示的合约列表,该列表只有一项
        self.main_tq_account = args[3]          # 从主程序传过来的天勤账户
        self.main_tq__pwd = args[4]             # 从主程序传过来的天勤密码

        self.current_tmp = []                   # 临时存储当前显示的合约名,用来对比当前所显示的合约是否已改变,该列表只有一项
        self.current_quote = {}                 # 当前显示的k线品种行情切片
        self.quote_assembly_dict = {}           # 行情引用字典集合,该字典的键为 合约名,值为对应的 api.get_quote() 对象

        self.ioModule = ReadWriteCsv()           # 文件读写对象

    async def Statua_Monitoring(self):  # 协程任务,监控主程序的指令变化
        while True:
            self.check_download_klines_and_save_to_csv()
            self.check_create_quote_list_dict()
            print('自选列表为:', self.self_selection_list)
            # print('天勤服务进程读到的当前合约为: ', self.current_Contracts[0])
            if self.current_Contracts:
                if self.current_tmp:
                    if self.current_Contracts[0] == self.current_tmp[0]:
                        pass
                    else:
                        self.current_tmp[0] = self.current_Contracts[0]
                        self.current_quote = self.quote_assembly_dict[self.current_Contracts[0]]

                        if self.current_quote:
                            self.quote_dict_Assignment(self.current_quote)  # 给和程序共享的quote_dict赋值
                        else:
                            print('该合约没有行情切片')
                else:
                    self.current_tmp.append(self.current_Contracts[0])

            await asyncio.sleep(1)
            # print('状态监控运行中:间隔1s')

    def run(self):
        sys.stdout = Logger(process_name='天勤行情数据服务日志')            # 由 logger 类实例化的对象接管系统标准输出,将系统输出保存到 log
        self.api = TqApi(TqKq(), auth=TqAuth(self.main_tq_account, self.main_tq__pwd))      # 创建天勤api
        if self.current_Contracts[0]:                                   # 判断当前显示的合约是否为空
            self.current_quote = self.api.get_quote(self.current_Contracts[0])
        self.get_all_Available_contracts()                              # 获取所有可交易的合约表并保存到文件
        self.check_download_klines_and_save_to_csv()                    # 检查并下载k线数据,保存到csv文件
        time.sleep(3)                                                   # 等待3秒,以便k线下载完毕
        self.api.create_task(self.Statua_Monitoring())                  # 创建协程任务,用来每隔一秒检查和主程序共享的数据是否发生改变
        while True:
            self.api.wait_update()
            if self.current_quote:                                      # 检查是否有当前行情引用
                if self.api.is_changing(self.current_quote, "last_price"):
                    self.quote_dict_Assignment(self.current_quote)      # 给和程序共享的quote_dict赋值
                    # print('当前行情引用为:', self.current_quote['instrument_name'])


    def check_download_klines_and_save_to_csv(self):        # 检查并下载k线数据,保存到csv文件

        for symbol in self.self_selection_list:         # 遍历自选列表

            path_1min = './Klines_data/' + symbol + '_1min.csv'
            if not os.path.exists(path_1min):
                self.api.create_task(self.download_1min_klines(symbol, path_1min))

            path_15min = './Klines_data/' + symbol + '_15min.csv'
            if not os.path.exists(path_15min):
                self.api.create_task(self.download_15min_klines(symbol, path_15min))

            path_30min = './Klines_data/' + symbol + '_30min.csv'
            if not os.path.exists(path_30min):
                self.api.create_task(self.download_30min_klines(symbol, path_30min))

            path_1hour = './Klines_data/' + symbol + '_1hour.csv'
            if not os.path.exists(path_1hour):
                self.api.create_task(self.download_1hour_klines(symbol, path_1hour))

            path_2hour = './Klines_data/' + symbol + '_2hour.csv'
            if not os.path.exists(path_2hour):
                self.api.create_task(self.download_2hour_klines(symbol, path_2hour))

            path_4hour = './Klines_data/' + symbol + '_4hour.csv'
            if not os.path.exists(path_4hour):
                self.api.create_task(self.download_4hour_klines(symbol, path_4hour))

            path_1day = './Klines_data/' + symbol + '_1day.csv'
            if not os.path.exists(path_1day):
                self.api.create_task(self.download_1day_klines(symbol, path_1day))

    def check_create_quote_list_dict(self):
        for symbol in self.self_selection_list:         # 遍历自选列表
            if symbol in self.quote_assembly_dict:
                pass
            else:
                 self.quote_assembly_dict[symbol] = self.api.get_quote(symbol)
                 print('\n\n当前时间为:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '\n')
                 print('已为合约: ', symbol,' 建立新行情引用:\n', self.quote_assembly_dict[symbol])

    def quote_dict_Assignment(self, dict):                  # 给和程序共享的quote_dict赋值
        if len(dict) > 5:
             self.quote_dict['datetime'] = dict['datetime']
             self.quote_dict['ask_price1'] = dict['ask_price1']
             self.quote_dict['ask_volume1'] = dict['ask_volume1']
             self.quote_dict['bid_price1'] = dict['bid_price1']
             self.quote_dict['bid_volume1'] = dict['bid_volume1']
             self.quote_dict['ask_price2'] = dict['ask_price2']
             self.quote_dict['ask_volume2'] = dict['ask_volume2']
             self.quote_dict['bid_price2'] = dict['bid_price2']
             self.quote_dict['bid_volume2'] = dict['bid_volume2']
             self.quote_dict['ask_price3'] = dict['ask_price3']
             self.quote_dict['ask_volume3'] = dict['ask_volume3']
             self.quote_dict['bid_price3'] = dict['bid_price3']
             self.quote_dict['bid_volume3'] = dict['bid_volume3']
             self.quote_dict['ask_price4'] = dict['ask_price4']
             self.quote_dict['ask_volume4'] = dict['ask_volume4']
             self.quote_dict['bid_price4'] = dict['bid_price4']
             self.quote_dict['bid_volume4'] = dict['bid_volume4']
             self.quote_dict['ask_price5'] = dict['ask_price5']
             self.quote_dict['ask_volume5'] = dict['ask_volume5']
             self.quote_dict['bid_price5'] = dict['bid_price5']
             self.quote_dict['bid_volume5'] = dict['bid_volume5']
             self.quote_dict['last_price'] = dict['last_price']
             self.quote_dict['highest'] = dict['highest']
             self.quote_dict['lowest'] = dict['lowest']
             self.quote_dict['open'] = dict['open']
             self.quote_dict['close'] = dict['close']
             self.quote_dict['average'] = dict['average']
             self.quote_dict['volume'] = dict['volume']
             self.quote_dict['amount'] = dict['amount']
             self.quote_dict['open_interest'] = dict['open_interest']
             self.quote_dict['settlement'] = dict['settlement']
             self.quote_dict['upper_limit'] = dict['upper_limit']
             self.quote_dict['lower_limit'] = dict['lower_limit']
             self.quote_dict['pre_open_interest'] = dict['pre_open_interest']
             self.quote_dict['pre_settlement'] = dict['pre_settlement']
             self.quote_dict['pre_close'] = dict['pre_close']
             self.quote_dict['price_tick'] = dict['price_tick']
             self.quote_dict['price_decs'] = dict['price_decs']
             self.quote_dict['volume_multiple'] = dict['volume_multiple']
             self.quote_dict['max_limit_order_volume'] = dict['max_limit_order_volume']
             self.quote_dict['max_market_order_volume'] = dict['max_market_order_volume']
             self.quote_dict['min_limit_order_volume'] = dict['min_limit_order_volume']
             self.quote_dict['min_market_order_volume'] = dict['min_market_order_volume']
             self.quote_dict['underlying_symbol'] = dict['underlying_symbol']
             self.quote_dict['strike_price'] = dict['strike_price']
             self.quote_dict['ins_class'] = dict['ins_class']
             self.quote_dict['instrument_id'] = dict['instrument_id']
             self.quote_dict['instrument_name'] = dict['instrument_name']
             self.quote_dict['exchange_id'] = dict['exchange_id']
             self.quote_dict['expired'] = dict['expired']
             # self.quote_dict['trading_time'] = dict['trading_time']
             self.quote_dict['expire_datetime'] = dict['expire_datetime']
             self.quote_dict['delivery_year'] = dict['delivery_year']
             self.quote_dict['delivery_month'] = dict['delivery_month']
             self.quote_dict['last_exercise_datetime'] = dict['last_exercise_datetime']
             self.quote_dict['exercise_year'] = dict['exercise_year']
             self.quote_dict['exercise_month'] = dict['exercise_month']
             self.quote_dict['option_class'] = dict['option_class']
             self.quote_dict['exercise_type'] = dict['exercise_type']
             self.quote_dict['product_id'] = dict['product_id']
             self.quote_dict['iopv'] = dict['iopv']
             self.quote_dict['public_float_share_quantity'] = dict['public_float_share_quantity']
             self.quote_dict['stock_dividend_ratio'] = dict['stock_dividend_ratio']
             self.quote_dict['cash_dividend_ratio'] = dict['cash_dividend_ratio']
             self.quote_dict['expire_rest_days'] = dict['expire_rest_days']
             # self.quote_dict['commission'] = dict['commission']             #  佣金
             # self.quote_dict['margin'] = dict['margin']                       #  边缘 差价




    def get_all_Available_contracts(self):      # 获取所有可交易的合约表并保存到文件

        DCE_Main = self.api.query_cont_quotes(exchange_id="DCE")  # 主力合约
        DCE_Cont = self.api.query_quotes(ins_class='CONT', exchange_id="DCE")  # 主连
        DCE_Future = self.api.query_quotes(ins_class='FUTURE', exchange_id="DCE")  # 期货
        DCE_Index = self.api.query_quotes(ins_class='INDEX', exchange_id="DCE")  # 指数
        DCE_option = self.api.query_quotes(ins_class='OPTION', exchange_id="DCE")  # 期权

        SHFE_Main = self.api.query_cont_quotes(exchange_id="SHFE")  # 主力合约
        SHFE_Cont = self.api.query_quotes(ins_class='CONT', exchange_id="SHFE")  # 主连
        SHFE_Future = self.api.query_quotes(ins_class='FUTURE', exchange_id="SHFE")  # 期货
        SHFE_Index = self.api.query_quotes(ins_class='INDEX', exchange_id="SHFE")  # 指数
        SHFE_option = self.api.query_quotes(ins_class='OPTION', exchange_id="SHFE")  # 期权

        CZCE_Main = self.api.query_cont_quotes(exchange_id="CZCE")  # 主力合约
        CZCE_Cont = self.api.query_quotes(ins_class='CONT', exchange_id="CZCE")  # 主连
        CZCE_Future = self.api.query_quotes(ins_class='FUTURE', exchange_id="CZCE")  # 期货
        CZCE_Index = self.api.query_quotes(ins_class='INDEX', exchange_id="CZCE")  # 指数
        CZCE_option = self.api.query_quotes(ins_class='OPTION', exchange_id="CZCE")  # 期权

        CFFEX_Main = self.api.query_cont_quotes(exchange_id="CFFEX")  # 主力合约
        CFFEX_Cont = self.api.query_quotes(ins_class='CONT', exchange_id="CFFEX")  # 主连
        CFFEX_Future = self.api.query_quotes(ins_class='FUTURE', exchange_id="CFFEX")  # 期货
        CFFEX_Index = self.api.query_quotes(ins_class='INDEX', exchange_id="CFFEX")  # 指数
        CFFEX_option = self.api.query_quotes(ins_class='OPTION', exchange_id="CFFEX")  # 期权

        INE_Main = self.api.query_cont_quotes(exchange_id="INE")  # 主力合约
        INE_Cont = self.api.query_quotes(ins_class='CONT', exchange_id="INE")  # 主连
        INE_Future = self.api.query_quotes(ins_class='FUTURE', exchange_id="INE")  # 期货
        INE_Index = self.api.query_quotes(ins_class='INDEX', exchange_id="INE")  # 指数
        INE_option = self.api.query_quotes(ins_class='OPTION', exchange_id="INE")  # 期权

        self.write_available_contracts_to_csv(DCE_Main, path = 'DCE_Main')
        self.write_available_contracts_to_csv(DCE_Cont, path = 'DCE_Cont')
        self.write_available_contracts_to_csv(DCE_Future, path = 'DCE_Future')
        self.write_available_contracts_to_csv(DCE_Index, path = 'DCE_Index')
        self.write_available_contracts_to_csv(DCE_option, path = 'DCE_Option')
        self.write_available_contracts_to_csv(SHFE_Main, path = 'SHFE_Main')
        self.write_available_contracts_to_csv(SHFE_Cont, path = 'SHFE_Cont')
        self.write_available_contracts_to_csv(SHFE_Future, path = 'SHFE_Future')
        self.write_available_contracts_to_csv(SHFE_Index, path = 'SHFE_Index')
        self.write_available_contracts_to_csv(SHFE_option, path = 'SHFE_Option')
        self.write_available_contracts_to_csv(CZCE_Main, path = 'CZCE_Main')
        self.write_available_contracts_to_csv(CZCE_Cont, path = 'CZCE_Cont')
        self.write_available_contracts_to_csv(CZCE_Future, path = 'CZCE_Future')
        self.write_available_contracts_to_csv(CZCE_Index, path = 'CZCE_Index')
        self.write_available_contracts_to_csv(CZCE_option, path = 'CZCE_Option')
        self.write_available_contracts_to_csv(CFFEX_Main, path = 'CFFEX_Main')
        self.write_available_contracts_to_csv(CFFEX_Cont, path = 'CFFEX_Cont')
        self.write_available_contracts_to_csv(CFFEX_Future, path = 'CFFEX_Future')
        self.write_available_contracts_to_csv(CFFEX_Index, path = 'CFFEX_Index')
        self.write_available_contracts_to_csv(CFFEX_option, path = 'CFFEX_Option')
        self.write_available_contracts_to_csv(INE_Main, path = 'INE_Main')
        self.write_available_contracts_to_csv(INE_Cont, path = 'INE_Cont')
        self.write_available_contracts_to_csv(INE_Future, path = 'INE_Future')
        self.write_available_contracts_to_csv(INE_Index, path = 'INE_Index')
        self.write_available_contracts_to_csv(INE_option, path = 'INE_Option')




    def write_available_contracts_to_csv(self, list, path):
        self.ioModule.judge_dirs_exist('./available_contracts')
        pth = './available_contracts/' + path + '.csv'
        self.ioModule.judge_file_exist(pth)
        data = pd.DataFrame(data=list)
        self.ioModule.write_datas_to_csv_file(data, pth)


    def get_current_klines(self, symbol):
        self.klines_1min = self.api.get_kline_serial(symbol, duration_seconds=60, data_length=200)
        self.klines_15min = self.api.get_kline_serial(symbol, duration_seconds=60 * 15, data_length=200)
        self.klines_30min = self.api.get_kline_serial(symbol, duration_seconds=60 * 30, data_length=200)
        self.klines_1hour = self.api.get_kline_serial(symbol, duration_seconds=60 * 60, data_length=200)
        self.klines_2hour = self.api.get_kline_serial(symbol, duration_seconds=60 * 60 * 2, data_length=200)
        self.klines_4hour = self.api.get_kline_serial(symbol, duration_seconds=60 * 60 * 4, data_length=100)
        self.klines_1day = self.api.get_kline_serial(symbol, duration_seconds=60 * 60 * 24, data_length=50)


    async def download_1min_klines(self, symbol, path):
        if not os.path.exists(path):
            klines_1min = self.api.get_kline_serial(symbol, duration_seconds=60, data_length=8000)
            await asyncio.sleep(3)
            if self.api.is_serial_ready(klines_1min):
                data = klines_1min.drop(klines_1min[klines_1min['id']<0].index)         # 删除空行
                data1 = data.reset_index(drop=True)  # 重建索引
                self.ioModule.judge_file_exist(path=path)
                self.ioModule.write_datas_to_csv_file(data1, path=path)


    async def download_15min_klines(self, symbol, path):
        if not os.path.exists(path):
            klines_15min = self.api.get_kline_serial(symbol, duration_seconds=60*15, data_length=8000)
            await asyncio.sleep(3)
            if self.api.is_serial_ready(klines_15min):
                data = klines_15min.drop(klines_15min[klines_15min['id'] < 0].index)  # 删除空行
                data1 = data.reset_index(drop=True)  # 重建索引
                self.ioModule.judge_file_exist(path=path)
                self.ioModule.write_datas_to_csv_file(data1, path=path)
    async def download_30min_klines(self, symbol, path):
        if not os.path.exists(path):
            klines_30min = self.api.get_kline_serial(symbol, duration_seconds=60*30, data_length=8000)
            await asyncio.sleep(3)
            if self.api.is_serial_ready(klines_30min):
                data = klines_30min.drop(klines_30min[klines_30min['id'] < 0].index)  # 删除空行
                data1 = data.reset_index(drop=True)  # 重建索引
                self.ioModule.judge_file_exist(path=path)
                self.ioModule.write_datas_to_csv_file(data1, path=path)
    async def download_1hour_klines(self, symbol, path):
        if not os.path.exists(path):
            klines_1hour = self.api.get_kline_serial(symbol, duration_seconds=60*60, data_length=8000)
            await asyncio.sleep(3)
            if self.api.is_serial_ready(klines_1hour):
                data = klines_1hour.drop(klines_1hour[klines_1hour['id'] < 0].index)  # 删除空行
                data1 = data.reset_index(drop=True)  # 重建索引
                self.ioModule.judge_file_exist(path=path)
                self.ioModule.write_datas_to_csv_file(data1, path=path)
    async def download_2hour_klines(self, symbol, path):
        if not os.path.exists(path):
            klines_2hour = self.api.get_kline_serial(symbol, duration_seconds=60*60*2, data_length=8000)
            await asyncio.sleep(3)
            if self.api.is_serial_ready(klines_2hour):
                data = klines_2hour.drop(klines_2hour[klines_2hour['id'] < 0].index)  # 删除空行
                data1 = data.reset_index(drop=True)  # 重建索引
                self.ioModule.judge_file_exist(path=path)
                self.ioModule.write_datas_to_csv_file(data1, path=path)
    async def download_4hour_klines(self, symbol, path):
        if not os.path.exists(path):
            klines_4hour = self.api.get_kline_serial(symbol, duration_seconds=60*60*4, data_length=8000)
            await asyncio.sleep(3)
            if self.api.is_serial_ready(klines_4hour):
                data = klines_4hour.drop(klines_4hour[klines_4hour['id'] < 0].index)  # 删除空行
                data1 = data.reset_index(drop=True)  # 重建索引
                self.ioModule.judge_file_exist(path=path)
                self.ioModule.write_datas_to_csv_file(data1, path=path)
    async def download_1day_klines(self, symbol, path):
        if not os.path.exists(path):
            klines_1day = self.api.get_kline_serial(symbol, duration_seconds=60*60*24, data_length=8000)
            await asyncio.sleep(3)
            if self.api.is_serial_ready(klines_1day):
                data = klines_1day.drop(klines_1day[klines_1day['id'] < 0].index)  # 删除空行
                data1 = data.reset_index(drop=True)  # 重建索引
                self.ioModule.judge_file_exist(path=path)
                self.ioModule.write_datas_to_csv_file(data1, path=path)




if __name__ == '__main__':

    self_selection_list = Manager().list()
    quote_dict = Manager().dict()
    current_Kline = Manager().list()
    current_Kline.append('INE.sc2211')
    main_tq_account = 'a哆啦a梦'
    main_tq_pwd = 'c168899'
    ioModule = ReadWriteCsv()
    data = ioModule.read_csv_file(path='./data/self_selection.csv')
    for index,row in data.iterrows():
        self_selection_list.append(row['quote'])
    t = TQServices(args=(self_selection_list, quote_dict, current_Kline, main_tq_account, main_tq_pwd))
    t.start()
    t.join()
