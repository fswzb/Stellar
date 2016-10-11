# -*- coding: utf-8 -*-
__author__ = 'MoroJoJo'


import os
import datetime
from concurrent.futures import ThreadPoolExecutor

import tushare

from utils.logger import *
from utils.common import get_stellar_root
from utils.data import is_market_closed
from utils.data import need_data_file_refresh
from data_manager.tushare import fundamental as sfund


'''
获取证券股票的指定交易日的大单交易数据
'''


# Global Consts
USING_CSV = 1
USING_MY_SQL = 2
USING_MONGO_DB = 3
STORAGE_MODE = USING_CSV

# TuShare Data Storage Path
DEFAULT_CSV_PATH_TS = ('%s/Data/csv/tushare' % get_stellar_root())
DEFAULT_MY_SQL_PATH_TS = ('%s/Data/mysql/tushare' % get_stellar_root())
DEFAULT_MONGO_DB_PATH_TS = ('%s/Data/mongodb/tushare' % get_stellar_root())

THREAD_COUNT = 50    # 查询交易数据的并行线程数
RETRY_COUNT = 5      # 调用tushare接口失败重试次数
RETRY_PAUSE = 0.1    # 调用tushare接口失败重试间隔时间
VOL = 400            # 定义为大单的手数

DEAL_FORWARD = 0
DEAL_BACKWARD = 1


def get_directory_path(vol):
    dir_path = ''
    if STORAGE_MODE == USING_CSV:
        dir_path = '%s/security_trade_data/big_deal/current_day/vol_%s' % (DEFAULT_CSV_PATH_TS, vol)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    return dir_path


def get_all_security_current_day_big_deal_no_multi_thread(vol=VOL):
    '''
    获取所有股票在今天的大单交易信息, 非多线程版本

    Parameters
    ------
        vol: 大单手数
    return
    -------
        无
    '''
    dm_log.debug('get_all_security_current_day_big_deal_no_multi_thread Begin...')

    today = datetime.date.today()
    today_str = datetime.date.strftime(today, '%Y-%m-%d')
    code_list = sfund.get_all_security_basic_info()              # 获取所有股票的基本信息
    for code in code_list:
        dm_log.debug('get_big_deal_data, code: %s, deal_date: %s' % (code, today_str))
        get_big_deal_data((code, today_str, vol))

    dm_log.debug('get_all_security_current_day_big_deal_no_multi_thread Finish...')


def get_all_security_current_day_big_deal_multi_thread(vol=VOL):
    '''
    获取所有股票今天的大单交易数据, 多线程版本

    Parameters
    ------
        vol: 大单手数
    return
    -------
        无
    '''
    today = datetime.date.today()
    today_str = datetime.date.strftime(today, '%Y-%m-%d')

    if tushare.is_holiday(today_str):
        dm_log.debug('get_all_security_current_day_big_deal_multi_thread() deal_date: %s skipped, cause this day is a holiday' % today_str)
        return

    code_list = sfund.get_all_security_basic_info()              # 获取所有股票的基本信息
    para_list = []
    for code in code_list:
        para_list.append((code, today_str, vol))
    pool = ThreadPoolExecutor(max_workers=THREAD_COUNT)
    pool.map(get_big_deal_data, para_list)


def print_result(request, result):
    print("---Result from request %s : %r" % (request.requestID, result))


def get_big_deal_data(para):
    '''
    获取code对应股票在指定时间长度内的大单交易数据

        code：代码
        name：名称
        time：时间
        price：当前价格
        volume：成交手
        preprice ：上一笔价格
        type：买卖类型【买盘、卖盘、中性盘】

    Parameters
    ------
        code: 股票代码
        tick_date: 查询日期
        vol: 大单手数
    return
    -------
        无
    '''
    code = para[0]
    deal_date = para[1]
    vol = para[2]
    if not is_market_closed():
        # now is too early for refresh, current day data is not ready.
        dm_log.debug('Now is too early for refresh, current day data is not ready.')
        return

    if STORAGE_MODE == USING_CSV:
        file_path = '%s/%s.csv' % (get_directory_path(vol), code)

        if not need_data_file_refresh(file_path):
            # the file is already refreshed some time current day after valid date, no need to refresh
            dm_log.debug('%s is already up-to-date, no need to refresh.' % file_path)
            return

        try:
            dm_log.debug('tushare.get_sina_dd: %s, tick_date=%s called' % (code, deal_date))
            df = tushare.get_sina_dd(code, date=deal_date, vol=vol, retry_count=RETRY_COUNT, pause=RETRY_PAUSE)
        except Exception as exception:
            dm_log.error('tushare.get_sina_dd(%s) excpetion, args: %s' % (code, exception.args.__str__()))
        else:
            if df is None:
                dm_log.warning('tushare.get_sina_dd: %s, tick_date=%s return none' % (code, deal_date))
            else:
                dm_log.debug('tushare.get_sina_dd: %s, tick_date=%s done, got %d rows' % (code, deal_date, len(df)))
                df.to_csv(file_path)


if __name__ == "__main__":
    # get_all_security_current_day_big_deal_no_multi_thread(vol=120)
    get_all_security_current_day_big_deal_multi_thread(vol=200)
    # get_big_deal_data('002612', '2016-07-26', vol=150)

