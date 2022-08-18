# # coding:utf-8
import json
import os
import pandas as pd


def add_param(my_df, path):
    data = read_excel_file(path)
    data = data.append(my_df,ignore_index=True)
    
    write_config_file(data, path)
    print('数据已存入config文件')

def read_excel_file(path):
    df = pd.read_excel(path,index_col=0)
    return df

def write_config_file(df_tmp, path, encoding='utf-8',index=False):
    df = pd.DataFrame(df_tmp)
    df.to_excel(path)

def judge_config_exist(path):
    dirs = './data/'
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    if not os.path.exists(path):
        df_tmp = pd.DataFrame()
        write_config_file(df_tmp, path)