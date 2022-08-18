#传入回测的元组为：
(0,     # 元组第一个元素index，为进程的索引，为config.csv中的行号，从0开始，主要用于策略进程往config文件中回写数据时寻找对应的行

{       # 元组第二个元素dict，为一个字典，config.csv中的每一行数据读出来都是一个字典，回写到config文件中的时候，也是一个同样的字典

        'process_name': '回测{2022-08-01 20:01:51}pingTest/DCE.i2209/15min',    # 进程的名称，主要用于区分进程，还有日志文件的命名
        'client_name': ' ',                                                            # 客户名称
        'tq_account': 'hujefeg',                                                # 天勤账号
        'tq_psd': 'hsdhjksfsd',                                                 # 天勤密码
        'futures_company': 'Z中信期货',                                           # 期货公司
        'futures_account': 'sdlkfgsdg',                                         # 实盘期货资金账号
        'futures_psd': '4545655',                                               # 实盘期货资金密码
        'symbol': 'DCE.i2209',                                                  # 合约代码
        'symbol_period': '15',                                                  # 合约周期
        'strategy': 'pingTest',                                                 # 策略名称
        'whether_self_start': 'Ture',   # 是否自启动，此项只有为ture时，才会自启动，在config文件中将对应行的此项改为False，该进程就不会自启动
        'whether_live_trading': 'Flase',                                        # 是否是实盘交易
        'whether_backtest': 'Ture',                                             # 是否是回测
        'whether_open_web_services': 'True',                                    # 是否开启web服务
        'web_port': '9797',                                           # web服务端口

        'stop_trading': 0,                                                      # 停止交易标记位，此项为0时正常交易，为1时停止交易
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

        'Customized_parameters_1': '11',                                        # 自定义参数1
        'Customized_parameters_2': '22',                                        # 自定义参数2
        'Customized_parameters_3': '33',                                        # 自定义参数3
        'Customized_parameters_4': '44',                                        # 自定义参数4
        'Customized_parameters_5': '55',                                        # 自定义参数5
        'Customized_parameters_6': '66',                                        # 自定义参数6
        'Customized_parameters_7': '77',                                        # 自定义参数7
        'Customized_parameters_8': '88'                                         # 自定义参数8

}, 

'2022-02-15', '2022-08-01'                                              # 元组第三和第四个元素，为回测开始日期和结束日期
                                # 正常运行的策略，传入的元组只需要第一第二个元素，第三和第四个元素直接不要即可，只有在回测时才需要
)