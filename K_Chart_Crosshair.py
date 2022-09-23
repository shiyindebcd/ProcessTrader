# -*- coding: utf-8 -*-
import datetime as dt

import pyqtgraph as pg
from pyqtgraph.Point import Point
from PySide6 import QtCore
from tqsdk import tafunc


########################################################################
# 十字光标类
########################################################################
class Crosshair(QtCore.QObject):
    """
    此类给pg.PlotWidget()添加crossHair功能,PlotWidget实例需要初始化时传入
    """
    signal = QtCore.Signal(float, float)
    signalInfo = QtCore.Signal(float, float)


    # ----------------------------------------------------------------------
    def __init__(self, parent, master):
        """Constructor"""
        self.__view = parent
        self.master = master
        super(Crosshair, self).__init__()
        self.datas = None
        self.xAxis = 0
        self.yAxis = 0
        self.yAxises = [0 for i in range(3)]
        self.leftX = [0 for i in range(3)]
        self.showHLine = [False for i in range(3)]
        self.text_Y_volume = [pg.TextItem('', anchor=(1, 1)) for i in range(3)]
        self.views = [parent.centralWidget.getItem(i + 1, 0) for i in range(3)]
        self.rects = [self.views[i].sceneBoundingRect() for i in range(3)]
        self.vLines = [pg.InfiniteLine(angle=90, movable=False) for i in range(3)]
        self.hLines = [pg.InfiniteLine(angle=0, movable=False) for i in range(3)]

        # mid 在y轴动态跟随最新价显示最新价和最新时间
        self.__text_X_date = pg.TextItem('X_date', anchor=(1, 1))
        self.__text_label_Info = pg.TextItem('lastBarInfo', anchor=(0, 1))
        self.__text_Ind_Info = pg.TextItem('lastIndInfo')
        self.__text_Volume_Info = pg.TextItem('lastBarVolume')
        self.__text_MACD_Info = pg.TextItem('lastMACDInfo')

        self.__text_X_date.setZValue(20)
        self.__text_label_Info.setZValue(20)
        self.__text_Ind_Info.setZValue(20)
        self.__text_MACD_Info.setZValue(20)
        self.__text_Volume_Info.setZValue(20)
        self.__text_label_Info.border = pg.mkPen(color=(230, 255, 0, 255), width=0)

        for i in range(3):
            self.text_Y_volume[i].setZValue(20)
            self.vLines[i].setPos(20)
            self.hLines[i].setPos(20)
            self.vLines[i].setZValue(20)
            self.hLines[i].setZValue(20)
            self.views[i].setZValue(20)
            self.views[i].addItem(self.vLines[i])
            self.views[i].addItem(self.hLines[i])
            self.views[i].addItem(self.text_Y_volume[i])

        self.views[0].addItem(self.__text_label_Info, ignoreBounds=True)
        self.views[0].addItem(self.__text_Ind_Info, ignoreBounds=True)
        self.views[1].addItem(self.__text_Volume_Info, ignoreBounds=True)
        self.views[2].addItem(self.__text_MACD_Info, ignoreBounds=True)
        self.views[2].addItem(self.__text_X_date, ignoreBounds=True)
        self.proxy = pg.SignalProxy(self.__view.scene().sigMouseMoved, rateLimit=360, slot=self.__mouseMoved)
        # 跨线程刷新界面支持
        self.signal.connect(self.update)
        self.signalInfo.connect(self.plotInfo)

    def update(self, x, y):
        """刷新界面显示"""
        xAxis = x
        yAxis = y
        if xAxis is None:
            xAxis, yAxis = (self.xAxis, self.yAxis)
        else:
            xAxis, yAxis = (x, y)
        self.moveTo(xAxis, yAxis)

    def __mouseMoved(self, evt):
        """鼠标移动回调"""
        pos = evt[0]
        self.rects = [self.views[i].sceneBoundingRect() for i in range(3)]
        for i in range(3):
            self.showHLine[i] = False
            if self.rects[i].contains(pos):
                mousePoint = self.views[i].vb.mapSceneToView(pos)
                xAxis = mousePoint.x()
                yAxis = mousePoint.y()
                self.yAxises[i] = yAxis
                self.showHLine[i] = True
                self.moveTo(xAxis, yAxis)

    def moveTo(self, xAxis, yAxis):
        if xAxis is None:
            xAxis, yAxis = (self.xAxis, self.yAxis)
        else:
            xAxis, yAxis = (int(xAxis), yAxis)
        self.rects = [self.views[i].sceneBoundingRect() for i in range(3)]

        if not xAxis or not yAxis:
            return
        self.xAxis = xAxis
        self.yAxis = yAxis
        self.vhLinesSetXY(xAxis, yAxis)
        self.plotInfo(xAxis, yAxis)
        self.master.candle.update()

    def vhLinesSetXY(self, xAxis, yAxis):
        """水平和竖线位置设置"""
        for i in range(3):
            self.vLines[i].setPos(xAxis)
            if self.showHLine[i]:
                self.hLines[i].setPos(yAxis if i == 0 else self.yAxises[i])
                self.hLines[i].show()
            else:
                self.hLines[i].hide()

    def plotInfo(self, xAxis, yAxis):
        """
        被嵌入的plotWidget在需要的时候通过调用此方法显示K线信息
        """
        if self.datas is None:
            return
        try:
            # 获取K线数据
            data = self.datas.loc[xAxis]
            lastdata = self.datas.loc[xAxis - 1]

            # 用天勤自带的时间转换函数将时间截转换成datetime格式
            tickDatetime = tafunc.time_to_datetime(data['datetime'])
            openPrice = data['open']
            closePrice = data['close']
            lowPrice = data['low']
            highPrice = data['high']
            volume = int(data['volume'])
            preClosePrice = lastdata['close']
            diff = data['diff']
            dea = data['dea']
            bar = data['bar']
            mv1 = data['mv1']
            mv2 = data['mv2']
            pb1 = data['pb1']
            pb2 = data['pb2']
            pb3 = data['pb3']
            pb4 = data['pb4']
            pb5 = data['pb5']
            pb6 = data['pb6']

        except Exception as e:
            return

        if (isinstance(tickDatetime, dt.datetime)):
            dateText = dt.datetime.strftime(tickDatetime, '%m-%d')
            timeText = dt.datetime.strftime(tickDatetime, '%H:%M')
            if tickDatetime.hour:   # 日内周期
                datetimeText = dt.datetime.strftime(tickDatetime, '%m-%d %H:%M')
            else:                   # 日线及以上周期
                datetimeText = dt.datetime.strftime(tickDatetime, '%Y-%m-%d')
        else:
            datetimeText = ""
            dateText = ""
            timeText = ""

        # 显示高开低收及日期
        # 和上一个收盘价比较，决定K线信息的字符颜色
        cOpen = 'rgb(255,0,0)' if openPrice > preClosePrice else 'rgb(0,255,0)'
        cClose = 'rgb(255,0,0)' if closePrice > preClosePrice else 'rgb(0,255,0)'
        cHigh = 'rgb(255,0,0)' if highPrice > preClosePrice else 'rgb(0,255,0)'
        cLow = 'rgb(255,0,0)' if lowPrice > preClosePrice else 'rgb(0,255,0)'

        self.__text_label_Info.setHtml(u'<div style="text-align: center; background-color:rgb(13,9,27)">\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">日期:</span><br>\
                                <span style="color: rgb(0,255,255); font-size: 14px;">%s</span><br><br>\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">时间:</span><br>\
                                <span style="color: rgb(0,255,255); font-size: 14px;">%s</span><br><br>\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">开盘:</span><br>\
                                <span style="color: %s;     font-size: 14px;">%.1f</span><br>\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">最高:</span><br>\
                                <span style="color: %s;     font-size: 14px;">%.1f</span><br>\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">最低:</span><br>\
                                <span style="color: %s;     font-size: 14px;">%.1f</span><br>\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">收盘:</span><br>\
                                <span style="color: %s;     font-size: 14px;">%.1f</span><br><br>\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">成交量:</span><br>\
                                <span style="color: rgb(0,255,255); font-size: 14px;">%d</span><br>\
                            </div>' % (dateText, timeText, cOpen, openPrice, cHigh, highPrice, cLow, lowPrice, cClose, closePrice, volume))
        # 显示纵轴时间
        # 显示所有的主图技术指标,六条瀑布线
        self.__text_Ind_Info.setHtml(u'<div style="text-align: center; background-color:rgb(13,9,27)">\
                                <span style="color: rgb(255,255,0);  font-size: 14px;">  瀑布线指标(3,4,9,13,18,24)-->  </span>\
                                <span style="color: rgb(255,255,255);  font-size: 14px;">  PB1: %.1f   </span>\
                                <span style="color: rgb(255,85,0);  font-size: 14px;">  PB2: %.1f   </span>\
                                <span style="color: rgb(255,0,127);  font-size: 14px;">  PB3: %.1f   </span>\
                                <span style="color: rgb(0,255,0);  font-size: 14px;">  PB4: %.1f   </span>\
                                <span style="color: rgb(255,0,0);  font-size: 14px;">  PB5: %.1f   </span>\
                                <span style="color: rgb(60,60,255);  font-size: 14px;">  PB6: %.1f   </span>'
                                     '</div>' % (pb1, pb2, pb3, pb4, pb5, pb6))

        # 显示成交量及均量
        self.__text_Volume_Info.setHtml(u'<div style="text-align: center; ">\
                                <span style="color: rgb(255,255,0);  font-size: 14px;">  成交量(5,20)-->    </span>\
                                <span style="color: rgb(255,0,255);  font-size: 14px;">  Vol: %.1f   </span>\
                                <span style="color: rgb(60,60,255);  font-size: 14px;">  ma5: %.1f   </span>\
                                <span style="color: rgb(255,0,127);  font-size: 14px;">  ma20: %.1f   </span>'
                                        '</div>' % (volume, mv1, mv2))

        # 显示macd技术指标
        self.__text_MACD_Info.setHtml(u'<div style="text-align: center; ">\
                                <span style="color: rgb(255,255,0);  font-size: 14px;">  MACD(12,6,9)-->   </span>\
                                <span style="color: rgb(255,0,255);  font-size: 14px;">  diff: %.1f   </span>\
                                <span style="color: rgb(60,60,255);  font-size: 14px;">  dea: %.1f   </span>\
                                <span style="color: rgb(255,0,127);  font-size: 14px;">  bar: %.1f   </span>'
                                      '</div>' % (diff, dea, bar))

        # 坐标轴宽度
        rightAxisWidth = self.views[0].getAxis('right').width()
        bottomAxisHeight = self.views[2].getAxis('bottom').height()
        offset = QtCore.QPointF(rightAxisWidth, bottomAxisHeight)

        # 各个顶点
        tl = [self.views[i].vb.mapSceneToView(self.rects[i].topLeft()) for i in range(3)]
        # 调试中获得的tl值为:
        # [PySide6.QtCore.QPointF(3493.702783, 727.623408),
        # PySide6.QtCore.QPointF(3493.702783, 110144.265625),
        # PySide6.QtCore.QPointF(3493.702783, 7.519954)]

        br = [self.views[i].vb.mapSceneToView(self.rects[i].bottomRight() - offset) for i in range(3)]
        # 调试中获得的br值为:
        # [PySide6.QtCore.QPointF(3602.111762, 667.376592),
        # PySide6.QtCore.QPointF(3602.111762, 2612.734375),
        # PySide6.QtCore.QPointF(3602.111762, -3.606918)]

        # 设置s标签信息坐标
        self.__text_label_Info.setPos(tl[0].x(), br[0].y())
        self.__text_Ind_Info.setPos(tl[0].x(), tl[0].y())
        self.__text_Volume_Info.setPos(tl[0].x(), tl[1].y())
        self.__text_MACD_Info.setPos(tl[0].x(), tl[2].y())

        # 修改对称方式防止遮挡
        if xAxis > self.master.index:
            self.__text_X_date.setPos(xAxis, br[2].y())
            self.__text_X_date.anchor = Point((1, 1))
            self.__text_label_Info.setPos(tl[0].x(), br[0].y())
            self.__text_label_Info.anchor = Point((0, 1))
            self.text_Y_volume[0].setPos(br[0].x(), yAxis)
            self.text_Y_volume[0].anchor = Point(1, 1)
        else:
            self.__text_X_date.setPos(xAxis, br[2].y())
            self.__text_X_date.anchor = Point((0, 1))
            self.__text_label_Info.setPos(br[0].x(), br[0].y())
            self.__text_label_Info.anchor = Point((1, 1))
            self.text_Y_volume[0].setPos(tl[0].x(), yAxis)
            self.text_Y_volume[0].anchor = Point(0, 1)

        # 显示Y轴价格

        self.text_Y_volume[0].setHtml('<div style="text-align: right">\
                     <span style="color: yellow; font-size: 16px;">%0.1f</span>\
                        </div>' % (yAxis))

        # 显示X轴时间
        self.__text_X_date.setHtml('<div style="text-align: center">\
                                <span style="color: yellow; font-size: 16px;">%s</span>\
                                </div>' % (datetimeText))
