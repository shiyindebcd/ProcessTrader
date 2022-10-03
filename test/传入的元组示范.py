p = (0,     # 元组第一个元素index，为进程的索引，为config.csv中的行号，从0开始，主要用于策略进程往config文件中回写数据时寻找对应的行

{       # 元组第二个元素dict，为一个字典，config.csv中的每一行数据读出来都是一个字典，回写到config文件中的时候，也是一个同样的字典

        'process_name': '回测{2022-08-01 20:01:51}pingTest/DCE.i2209/15min',    # 进程的名称，主要用于区分进程，还有日志文件的命名
        'client_name': ' ',                                                            # 客户名称
        'whether_self_start': 'Ture',   # 是否自启动，此项只有为ture时，才会自启动，在config文件中将对应行的此项改为False，该进程就不会自启动
        'tq_account': 'hujefeg',                                                # 天勤账号
        'tq_psd': 'hsdhjksfsd',                                                 # 天勤密码
        'futures_company': 'Z中信期货',                                           # 期货公司
        'futures_account': 'sdlkfgsdg',                                         # 实盘期货资金账号
        'futures_psd': '4545655',                                               # 实盘期货资金密码
        'symbol': 'DCE.i2209',                                                  # 合约代码
        'symbol_period': '15',                                                  # 合约周期
        'strategy': 'pingTest',                                                 # 策略名称
        'whether_live_trading': 'Flase',                                        # 是否是实盘交易
        'whether_backtest': 'Ture',                                             # 是否是回测
        'whether_open_web_services': 'True',                                    # 是否开启web服务
        'web_port': '9797',                                           # web服务端口

        'trading_status' : True,          # 交易状态标志位，默认True为正常交易，Flase为停止交易,可在策略中通过开关此位来停止或开启交易
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

        'whether_open_line' : False,                      # 是否定义了开仓直线
        'open_line_Coordinates' : '0,0',                  # 开仓线坐标
        'whether_close_line' : False,                     # 是否定义了平仓直线
        'close_line_Coordinates' : '0,0',                 # 平仓线坐标

        'CP1': '11',                                        # 自定义参数1    Customized_parameters 为了方便使用,缩写为CP
        'CP2': '22',                                        # 自定义参数2
        'CP3': '33',                                        # 自定义参数3
        'CP4': '44',                                        # 自定义参数4
        'CP5': '55',                                        # 自定义参数5
        'CP6': '66',                                        # 自定义参数6
        'CP7': '77',                                        # 自定义参数7
        'CP8': '88'                                         # 自定义参数8

},

'2022-02-15', '2022-08-01'                                              # 元组第三和第四个元素，为回测开始日期和结束日期
                                # 正常运行的策略，传入的元组只需要第一第二个元素，第三和第四个元素直接不要即可，只有在回测时才需要
)
#传入回测的元组为：
