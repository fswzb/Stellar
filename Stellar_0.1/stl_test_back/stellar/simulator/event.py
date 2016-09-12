# -*- coding: utf-8 -*-
__author__ = 'MoroJoJo'


from ..const import EVENT_TYPE


'''
事件循环
'''


class TradeSimulationEventSource(object):
    def __init__(self, trading_param):
        self.trading_param = trading_param
        self.timezone = trading_param.timezone
        self.generator = self.create_generator()

    def create_generator(self):
        for date in self.trading_param.trading_calendar:
            yield date.replace(hour=9, minute=0), EVENT_TYPE.DAY_START
            yield date.replace(hour=15, minute=0), EVENT_TYPE.HANDLE_BAR
            yield date.replace(hour=16, minute=0), EVENT_TYPE.DAY_END

    def __iter__(self):
        return self

    def __next__(self):
        for date, event in self.generator:
            return date, event
        raise StopIteration