# -*- coding: utf-8 -*-
__author__ = 'MoroJoJo'


from stl_utils import stl_logger as slog

import tushare
import pandas as pd
import os


'''
获取宏观经济数据
'''


RETRY_COUNT = 5               # 调用tushare接口失败重试次数
RETRY_PAUSE = 0.1             # 调用tushare接口失败重试间隔时间

DEFAULT_DIR_PATH = '../../../Data/origin/tushare/security_macro_economy_data'


def get_deposit_rate_data():
    '''
    获取存款利率数据

        date :变动日期
        deposit_type :存款种类
        rate:利率（%）

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/deposit_rate.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_deposit_rate()')
        tmp_data = tushare.get_deposit_rate()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_deposit_rate() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_deposit_rate() return none')
    else:
        tmp_data.to_csv(file_path)


def get_loan_rate_data():
    '''
    获取贷款利率数据

        date :执行日期
        loan_type :贷款种类
        rate:利率（%）

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/loan_rate.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_loan_rate()')
        tmp_data = tushare.get_loan_rate()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_loan_rate() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_loan_rate() return none')
    else:
        tmp_data.to_csv(file_path)


def get_rrr_data():
    '''
    获取存款准备金率数据

        date :变动日期
        before :调整前存款准备金率(%)
        now:调整后存款准备金率(%)
        changed:调整幅度(%)

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/rrr.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_rrr()')
        tmp_data = tushare.get_rrr()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_rrr() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_rrr() return none')
    else:
        tmp_data.to_csv(file_path)


def get_money_supply_data():
    '''
    获取货币供应数据

        month :统计时间
        m2 :货币和准货币（广义货币M2）(亿元)
        m2_yoy:货币和准货币（广义货币M2）同比增长(%)
        m1:货币(狭义货币M1)(亿元)
        m1_yoy:货币(狭义货币M1)同比增长(%)
        m0:流通中现金(M0)(亿元)
        m0_yoy:流通中现金(M0)同比增长(%)
        cd:活期存款(亿元)
        cd_yoy:活期存款同比增长(%)
        qm:准货币(亿元)
        qm_yoy:准货币同比增长(%)
        ftd:定期存款(亿元)
        ftd_yoy:定期存款同比增长(%)
        sd:储蓄存款(亿元)
        sd_yoy:储蓄存款同比增长(%)
        rests:其他存款(亿元)
        rests_yoy:其他存款同比增长(%)

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/money_supply.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_money_supply()')
        tmp_data = tushare.get_money_supply()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_money_supply() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_money_supply() return none')
    else:
        tmp_data.to_csv(file_path)


def get_money_supply_bal_data():
    '''
    获取货币供应数据(年底余额)

        year :统计年度
        m2 :货币和准货币(亿元)
        m1:货币(亿元)
        m0:流通中现金(亿元)
        cd:活期存款(亿元)
        qm:准货币(亿元)
        ftd:定期存款(亿元)
        sd:储蓄存款(亿元)
        rests:其他存款(亿元)

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/money_supply_bal.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_money_supply_bal()')
        tmp_data = tushare.get_money_supply_bal()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_money_supply_bal() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_money_supply_bal() return none')
    else:
        tmp_data.to_csv(file_path)


def get_gdp_year_data():
    '''
    获取年度国内生产总值

        year :统计年度
        gdp :国内生产总值(亿元)
        pc_gdp :人均国内生产总值(元)
        gnp :国民生产总值(亿元)
        pi :第一产业(亿元)
        si :第二产业(亿元)
        industry :工业(亿元)
        cons_industry :建筑业(亿元)
        ti :第三产业(亿元)
        trans_industry :交通运输仓储邮电通信业(亿元)
        lbdy :批发零售贸易及餐饮业(亿元)

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/gdp(Y).csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_gdp_year()')
        tmp_data = tushare.get_gdp_year()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_gdp_year() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_gdp_year() return none')
    else:
        tmp_data.to_csv(file_path)


def get_gdp_quarter_data():
    '''
    获取季度国内生产总值

        quarter :季度
        gdp :国内生产总值(亿元)
        gdp_yoy :国内生产总值同比增长(%)
        pi :第一产业增加值(亿元)
        pi_yoy:第一产业增加值同比增长(%)
        si :第二产业增加值(亿元)
        si_yoy :第二产业增加值同比增长(%)
        ti :第三产业增加值(亿元)
        ti_yoy :第三产业增加值同比增长(%)

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/gdp(Q).csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_gdp_quarter()')
        tmp_data = tushare.get_gdp_quarter()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_gdp_quarter() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_gdp_quarter() return none')
    else:
        tmp_data.to_csv(file_path)


def get_gdp_for_data():
    '''
    获取三大需求对GDP的贡献度数据

        year :统计年度
        end_for :最终消费支出贡献率(%)
        for_rate :最终消费支出拉动(百分点)
        asset_for :资本形成总额贡献率(%)
        asset_rate:资本形成总额拉动(百分点)
        goods_for :货物和服务净出口贡献率(%)
        goods_rate :货物和服务净出口拉动(百分点)

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/gdp_for.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_gdp_for()')
        tmp_data = tushare.get_gdp_for()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_gdp_for() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_gdp_for() return none')
    else:
        tmp_data.to_csv(file_path)


def get_gdp_pull_data():
    '''
    获取三大产业对GDP拉动数据

        year :统计年度
        gdp_yoy :国内生产总值同比增长(%)
        pi :第一产业拉动率(%)
        si :第二产业拉动率(%)
        industry:其中工业拉动(%)
        ti :第三产业拉动率(%)

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/gdp_pull.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_gdp_pull()')
        tmp_data = tushare.get_gdp_pull()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_gdp_pull() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_gdp_pull() return none')
    else:
        tmp_data.to_csv(file_path)


def get_gdp_contribution_data():
    '''
    获取三大产业贡献率数据

        year :统计年度
        gdp_yoy :国内生产总值
        pi :第一产业献率(%)
        si :第二产业献率(%)
        industry:其中工业献率(%)
        ti :第三产业献率(%)

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/gdp_contribution.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_gdp_contrib()')
        tmp_data = tushare.get_gdp_contrib()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_gdp_contrib() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_gdp_contrib() return none')
    else:
        tmp_data.to_csv(file_path)


def get_gdp_cpi_data():
    '''
    获取居民消费价格指数CPI数据

        month :统计月份
        cpi :价格指数

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/cpi.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_cpi()')
        tmp_data = tushare.get_cpi()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_cpi() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_cpi() return none')
    else:
        tmp_data.to_csv(file_path)


def get_gdp_ppi_data():
    '''
    获取居民消费价格指数CPI数据

        month :统计月份
        ppiip :工业品出厂价格指数
        ppi :生产资料价格指数
        qm:采掘工业价格指数
        rmi:原材料工业价格指数
        pi:加工工业价格指数
        cg:生活资料价格指数
        food:食品类价格指数
        clothing:衣着类价格指数
        roeu:一般日用品价格指数
        dcg:耐用消费品价格指数

    Parameters
    ------
        无
    return
    -------
        无
    '''
    dir_path = DEFAULT_DIR_PATH
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    file_path = '%s/ppi.csv' % dir_path

    tmp_data = pd.DataFrame()
    try:
        slog.StlDmLogger().debug('tushare.get_ppi()')
        tmp_data = tushare.get_ppi()
    except Exception as exception:
        slog.StlDmLogger().error('tushare.get_ppi() excpetion, args: %s' % exception.args.__str__())

    if tmp_data is None:
        slog.StlDmLogger().warning('tushare.get_ppi() return none')
    else:
        tmp_data.to_csv(file_path)


if __name__ == '__main__':
    get_deposit_rate_data()
    get_loan_rate_data()
    get_rrr_data()
    get_money_supply_data()
    get_money_supply_bal_data()
    get_gdp_year_data()
    get_gdp_quarter_data()
    get_gdp_for_data()
    get_gdp_pull_data()
    get_gdp_contribution_data()
    get_gdp_cpi_data()
    get_gdp_ppi_data()