# -*- coding: utf-8 -*-

import numpy as np
import pyqtgraph as pg
import PySide6
from PySide6 import QtCore, QtGui
from PySide6.QtGui import *


########################################################################
# K线图形对象
########################################################################
class CandlestickItem(pg.GraphicsObject):
    """K线图形对象"""


    def __init__(self, data: list):  # 初始化
        pg.GraphicsObject.__init__(self)
        # 只重画部分图形，大大提高界面更新速度
        self.rect = None
        self.picture = None
        self.setFlag(PySide6.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemUsesExtendedStyleOption)

        self.offset = 0
        self.low = 0
        self.high = 1
        self.picture = QtGui.QPicture()
        self.pictures = []
        self.generatePicture(data)  # 刷新K线


    def generatePicture(self, data=None, redraw=False):  # 画K线
        """重新生成图形对象"""
        if redraw:  # 重画或者只更新最后一个K线
            self.pictures = []
        elif self.pictures:
            self.pictures.pop()
        w = 0.4  # k线一半的宽度

        if len(data) > 0:
            self.low = np.min(data['low'])
            self.high = np.max(data['high'])
        else:
            self.low, self.high = (0, 1)

        npic = len(self.pictures)
        for (i, open_i, high_i, low_i, close_i, volume_i) in data:
            if i >= npic:
                picture = QtGui.QPicture()
                p = QtGui.QPainter(picture)
                # 画蜡烛图,下跌绿色（实心）, 上涨红色（空心）
                if close_i < open_i:  # 阴线情况
                    p.setPen(pg.mkPen(QtGui.QColor(0, 255, 0), width=2))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush(QtGui.QColor(0, 255, 0)))
                    p.drawLine(QtCore.QPointF(i, low_i), QtCore.QPointF(i, high_i))  # 画上下影线
                    p.drawRect(QtCore.QRectF(i - w, open_i, w * 2, close_i - open_i))  # 画矩形，实心K线

                elif close_i > open_i:  # 阳线情况
                    p.setPen(pg.mkPen(QtGui.QColor(255, 0, 0), width=2))  # red
                    p.setBrush(pg.mkBrush(QtGui.QColor(255, 0, 0)))  # red
                    if (high_i != close_i):  # 如果最高点不等于收盘价，画上影线
                        p.drawLine(QtCore.QPointF(i, high_i), QtCore.QPointF(i, close_i))
                    if (low_i != open_i):  # 如果最低点不等于开盘价，画下影线
                        p.drawLine(QtCore.QPointF(i, open_i), QtCore.QPointF(i, low_i))

                    # p.drawRect(QtCore.QRectF(i - w, open, w * 2, close - open)) # 如果画实心阳线，只需画个实心矩形即可
                    # 画空心阳线的时候，需要画四条线

                    p.drawLine(QtCore.QPointF(i - w, open_i), QtCore.QPointF(i - w, close_i))  # 画单根K线的左边线
                    p.drawLine(QtCore.QPointF(i + w, open_i), QtCore.QPointF(i + w, close_i))  # 画单根K线的右边线
                    p.drawLine(QtCore.QPointF(i - w, close_i), QtCore.QPointF(i + w, close_i))  # 画单根K线的上边线
                    p.drawLine(QtCore.QPointF(i - w, open_i), QtCore.QPointF(i + w, open_i))  # 画单根K线的下边线

                else:  # 平盘情况
                    if high_i == low_i:
                        p.setPen(pg.mkPen(QtGui.QColor(255, 255, 255), width=3))  # 一字线时设为白色
                        p.setBrush(pg.mkBrush(QtGui.QColor(255, 255, 255)))
                        p.drawLine(QtCore.QPointF(i - w, close_i), QtCore.QPointF(i + w, close_i))  # 光画一条横线即可
                    else:
                        p.setPen(pg.mkPen(QtGui.QColor(0, 0, 255), width=3))  # 十字线时设为蓝色
                        p.setBrush(pg.mkBrush(QtGui.QColor(0, 0, 255)))
                        p.drawLine(QtCore.QPointF(i, high_i), QtCore.QPointF(i, low_i))  # 画上下影线
                        p.drawLine(QtCore.QPointF(i - w, close_i), QtCore.QPointF(i + w, close_i))  # 画一条横线

                p.end()
                self.pictures.append(picture)


    def update(self):  # 手动重画
        if not self.scene() is None:
            self.scene().update()


    def paint(self, painter, opt, w):  # 自动重画
        rect = opt.exposedRect
        xmin, xmax = (max(0, int(rect.left())), min(int(len(self.pictures)), int(rect.right())))
        if not self.rect == (rect.left(), rect.right()) or self.picture is None:
            self.rect = (rect.left(), rect.right())
            self.picture = self.createPic(xmin, xmax)
            self.picture.play(painter)
        elif not self.picture is None:
            self.picture.play(painter)


    def createPic(self, xmin, xmax):  # 缓存图片
        picture = QPicture()
        p = QPainter(picture)
        [pic.play(p) for pic in self.pictures[xmin:xmax]]
        p.end()
        return picture


    def boundingRect(self):  # 定义边界
        return QtCore.QRectF(0, self.low, len(self.pictures), (self.high - self.low))


########################################################################
# 成交量图形对象
########################################################################
class VolumeItem(pg.GraphicsObject):
    """K线图形对象"""


    def __init__(self, data: list):  # 初始化
        """初始化"""
        pg.GraphicsObject.__init__(self)
        self.rect = None
        self.picture = None
        self.setFlag(PySide6.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemUsesExtendedStyleOption)  # 只重画部分图形，大大提高界面更新速度

        self.offset = 0
        self.low = 0
        self.high = 1
        self.picture = QtGui.QPicture()
        self.pictures = []
        self.generatePicture(data)  # 刷新柱线


    def generatePicture(self, data=None, redraw=False):  # 画柱线
        """重新生成图形对象"""
        # 重画或者只更新最后一个K线
        if redraw:
            self.pictures = []
        elif self.pictures:
            self.pictures.pop()
        w = 0.4  # k线一半的宽度
        self.low = 0
        if len(data) > 0:
            self.high = np.max(data['volume'])
        else:
            self.high = 1
        npic = len(self.pictures)
        for (i, open_i, high_i, low_i, close_i, volume_i) in data:
            if i >= npic:
                picture = QtGui.QPicture()
                p = QtGui.QPainter(picture)
                # 下跌绿色（实心）, 上涨红色（空心）
                if close_i < open_i:  # 阴线情况
                    p.setPen(pg.mkPen(QtGui.QColor(0, 255, 0), width=2))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush(QtGui.QColor(0, 255, 0)))
                    p.drawRect(QtCore.QRectF(i - w, 0, w * 2, volume_i))  # 画矩形，实心成交量柱线

                elif close_i > open_i:  # 阳线情况
                    p.setPen(pg.mkPen(QtGui.QColor(255, 0, 0), width=2))  # red
                    p.setBrush(pg.mkBrush(QtGui.QColor(255, 0, 0)))  # red

                    # p.drawRect(QtCore.QRectF(i - w, open_i, w * 2, close_i - open_i)) # 如果画实心阳线，只需画个实心矩形即可
                    # 画空心阳线的时候，需要画四条线

                    p.drawLine(QtCore.QPointF(i - w, 0), QtCore.QPointF(i - w, volume_i))  # 画单根成交量柱线的左边线
                    p.drawLine(QtCore.QPointF(i + w, 0), QtCore.QPointF(i + w, volume_i))  # 画单根成交量柱线的右边线
                    p.drawLine(QtCore.QPointF(i - w, volume_i), QtCore.QPointF(i + w, volume_i))  # 画单根成交量柱线的下边线
                    p.drawLine(QtCore.QPointF(i - w, 0), QtCore.QPointF(i + w, 0))  # 画单根成交量柱线的上边线

                else:  # 平盘情况
                    p.setPen(pg.mkPen(QtGui.QColor(0, 0, 255), width=2))  # 十字线设为蓝色
                    p.setBrush(pg.mkBrush(QtGui.QColor(0, 0, 255)))  # 十字线设为蓝色

                    p.drawRect(QtCore.QRectF(i - w, 0, w * 2, volume_i))  # 画矩形，实心成交量柱线

                p.end()
                self.pictures.append(picture)


    def update(self):  # 手动重画
        if not self.scene() is None:
            self.scene().update()


    def paint(self, painter, opt, w):  # 自动重画
        rect = opt.exposedRect
        xmin, xmax = (max(0, int(rect.left())), min(int(len(self.pictures)), int(rect.right())))
        if not self.rect == (rect.left(), rect.right()) or self.picture is None:
            self.rect = (rect.left(), rect.right())
            self.picture = self.createPic(xmin, xmax)
            self.picture.play(painter)
        elif not self.picture is None:
            self.picture.play(painter)


    def createPic(self, xmin, xmax):  # 缓存图片
        picture = QPicture()
        p = QPainter(picture)
        [pic.play(p) for pic in self.pictures[xmin:xmax]]
        p.end()
        return picture


    def boundingRect(self):  # 定义边界
        return QtCore.QRectF(0, self.low, len(self.pictures), (self.high - self.low))


########################################################################
# MACD图形对象
########################################################################
class MACDItem(pg.GraphicsObject):
    """K线图形对象"""


    def __init__(self, data: list):  # 初始化
        """初始化"""
        pg.GraphicsObject.__init__(self)
        self.rect = None
        self.picture = None
        self.setFlag(PySide6.QtWidgets.QGraphicsItem.GraphicsItemFlag.ItemUsesExtendedStyleOption)  # 只重画部分图形，大大提高界面更新速度

        self.offset = 0
        self.low = 0
        self.high = 1
        self.picture = QtGui.QPicture()
        self.pictures = []

        self.generatePicture(data)


    def generatePicture(self, data=None, redraw=False):  # 画柱线
        """重新生成图形对象"""
        if redraw:  # 重画或者只更新最后一个周期的线
            self.pictures = []
        elif self.pictures:
            self.pictures.pop()
        w = 0.1  # 柱线半宽
        if len(data) > 0:
            self.low = np.min(data['bar'])
            self.high = np.max(data['bar'])
        else:
            self.low, self.high = (0, 1)

        npic = len(self.pictures)

        for i, bar_i in data:
            if i >= npic:
                picture = QtGui.QPicture()
                p = QtGui.QPainter(picture)

                if bar_i > 0:  # macd 红柱
                    p.setPen(pg.mkPen(QtGui.QColor(255, 0, 0), width=2))  # 设置画笔颜色，宽度
                    p.setBrush(pg.mkBrush(QtGui.QColor(255, 0, 0)))
                    p.drawRect(QtCore.QRectF(i - w, 0, w * 2, bar_i))  # 画矩形

                else:  # macd 绿柱
                    p.setPen(pg.mkPen(QtGui.QColor(0, 255, 0), width=2))
                    p.setBrush(pg.mkBrush(QtGui.QColor(0, 255, 0)))
                    p.drawRect(QtCore.QRectF(i - w, 0, w * 2, bar_i))  # 画矩形

                p.end()
                self.pictures.append(picture)


    def update(self):  # 手动重画
        if not self.scene() is None:
            self.scene().update()


    def paint(self, painter, opt, w):  # 自动重画
        rect = opt.exposedRect
        xmin, xmax = (max(0, int(rect.left())), min(int(len(self.pictures)), int(rect.right())))
        if not self.rect == (rect.left(), rect.right()) or self.picture is None:
            self.rect = (rect.left(), rect.right())
            self.picture = self.createPic(xmin, xmax)
            self.picture.play(painter)
        elif not self.picture is None:
            self.picture.play(painter)


    def createPic(self, xmin, xmax):  # 缓存图片
        picture = QPicture()
        p = QPainter(picture)
        [pic.play(p) for pic in self.pictures[xmin:xmax]]
        p.end()
        return picture


    # 定义边界
    def boundingRect(self):
        return QtCore.QRectF(0, self.low, len(self.pictures), (self.high - self.low))
