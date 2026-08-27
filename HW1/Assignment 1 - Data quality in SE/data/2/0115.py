import math
import backtrader as bt
from datetime import datetime
from bots.TelegramBot import TelegramBot
import logging
class Volume(bt.Strategy):
    params = (('avg_volume_period', 10), ('ticker', 'hpg'), ('ratio', 1.25))

    def __init__(self):
        self.mysignal  = (self.data.volume / bt.ind.Average(self.data.volume, period=self.params.avg_volume_period)) >= self.params.ratio
    def next(self):
        self.step_date = self.data.datetime.date().strftime("%Y-%m-%d")
        self.today = datetime.now().strftime("%Y-%m-%d")
        if self.mysignal and self.step_date == self.today:
            TelegramBot.send("{} - KLGD lớn hơn KLGD trung bình {} ngày gần nhất.".format(self.params.ticker, self.params.avg_volume_period))
            