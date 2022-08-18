# # coding:utf-8

import sys
import os
import time
import datetime

import pandas as pd

class ReadWriteCsv(object): # csv文件读写类
    
    def add_dict_to_csv(self, my_df, path):
        data = self.read_csv_file(path)
        data = pd.concat([data, my_df], ignore_index=True)
        
        self.write_config_file(data, path)
        print('数据已存入config文件')

    def read_csv_file(self, path):
        df = pd.read_csv(path, engine='python', index_col=0)
               
        return df

    def write_config_file(self, df_tmp, path, encoding='utf_8_sig',index=False):
        df = pd.DataFrame(df_tmp)
        df.to_csv(path, encoding=encoding)

    def judge_config_exist(self, path):
        dirs = './data/'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
            print('文件目录' + dirs + '不存在，已创建')
        else:
            pass
        
        if not os.path.exists(path):
            df_tmp = pd.DataFrame()
            self.write_config_file(df_tmp, path)
            print('文件' + path + '不存在，已创建空白文件')
        else:
            print('文件' + path + '已存在')

    def delete_file(self, path):
        os.remove(path)
        


class ReadWriteExcel(object):   # excel文件读写类
    
    def add_dict_to_excel(self, my_df, path):
        data = self.read_excel_file(path)
        data = pd.concat([data, my_df], ignore_index=True)
        
        self.write_config_file(data, path)
        print('数据已存入config文件')

    def read_excel_file(self, path):
        df = pd.read_excel(path,index_col=0)
        return df

    def write_config_file(self, df_tmp, path, encoding='utf-8',index=False):
        df = pd.DataFrame(df_tmp)
        df.to_excel(path)

    def judge_config_exist(self, path):
        dirs = './data/'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
            print('文件目录' + dirs + '不存在，已创建')
        else:
            pass
        
        if not os.path.exists(path):
            df_tmp = pd.DataFrame()
            self.write_config_file(df_tmp, path)
            print('文件' + path + '不存在，已创建空白文件')
        else:
            print('文件' + path + '存在')


class Logger(object):   # 日志记录类
        def __init__(self, process_name):
            
            self.path = "./log/" + process_name + '/'   # 在log目录下创建以 process_name 命名的文件夹
            self.log_filename = datetime.datetime.now().strftime('%Y_%m_%d') + '.log'    # 日志文件名，以当前日期为名
            self.terminal = sys.stdout

            # 检查self.path是否存在，不存在则创建
            if not os.path.exists(self.path):
                os.makedirs(self.path)
            # 检查self.path下是否存在self.log_filename文件，不存在则创建空白文件
            if not os.path.exists(self.path + self.log_filename):
                with open(self.path + self.log_filename, 'w') as f:
                    f.write('')

                print('空白日志文件已创建，路径为：' + self.path + self.log_filename)
            
            # 打开self.path下的self.log_filename文件，并写入日志 
            self.log = open(os.path.join(self.path, self.log_filename), "a", buffering = 1, encoding='utf8',)

 
            # open(file, ‘w’, buffering = a) 中，buffering设置缓冲行为        
            # 全缓冲： a 是正整数，当缓冲区文件大小达到a大小时候，写入磁盘        
            # 行缓冲： buffering = 1, 缓冲区碰到 \n 换行符的时候就写入磁盘        
            # 无缓冲：buffering = 0 ，写多少，存多少


            print('*' * 40,' ', self.log_filename, ' ', '*' * 40)
            print('\n')
            print('开始记录 ', process_name, ' 的运行日志 。。。。。。\n')
            print('开始时间为： ', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '\n\n')

        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)
 
        def flush(self):
            pass
        
        
