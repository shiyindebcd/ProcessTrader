from functools import partial
from random import randrange

from PySide6.QtCore import QPoint, Qt, QTimer
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCharts import *
from PySide6.QtWidgets import QGridLayout


class ChartWidget:
    def __init__(self, widget):
        super().__init__()
        self.widget = widget                        
        self.chart = QChart()       
        self._chart_view = QChartView(self.chart)
        self.chart.ChartTheme(QChart.ChartThemeDark)
        self._axis_y = QValueAxis()     
        self._axis_x = QBarCategoryAxis()
        self.categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        self._line_series = QLineSeries()
        self._bar_series = QBarSeries()
        self.set4 = QBarSet("Smartphones")
        self.set3 = QBarSet("iPhones")
        self.set2 = QBarSet("AirPods")
        self.set1 = QBarSet("Tablets")
        self.set0 = QBarSet("iMac")

    def add_chart(self):
        self.set0.append([1, 2, 3, 4, 5, 6])
        self.set1.append([5, 0, 0, 4, 0, 7])
        self.set2.append([3, 5, 8, 13, 8, 5])
        self.set3.append([5, 6, 7, 3, 4, 5])
        self.set4.append([9, 7, 5, 3, 1, 2])

        self._bar_series.append(self.set0)
        self._bar_series.append(self.set1)
        self._bar_series.append(self.set2)
        self._bar_series.append(self.set3)
        self._bar_series.append(self.set4)

        self._line_series.setName("Treds")
        self._line_series.append(QPoint(0, 4))
        self._line_series.append(QPoint(1, 15))
        self._line_series.append(QPoint(2, 20))
        self._line_series.append(QPoint(3, 4))
        self._line_series.append(QPoint(4, 12))
        self._line_series.append(QPoint(5, 17))

        self.chart.addSeries(self._bar_series)
        self.chart.addSeries(self._line_series)
        self.chart.setTitle("Line and barchart example")

        self._axis_x.append(self.categories)
        self.chart.setAxisX(self._axis_x, self._line_series)
        self.chart.setAxisX(self._axis_x, self._bar_series)
        self._axis_x.setRange("Jan", "Jun")

        self.chart.setAxisY(self._axis_y, self._line_series)
        self.chart.setAxisY(self._axis_y, self._bar_series)
        self._axis_y.setRange(0, 20)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self._chart_view.setRenderHint(QPainter.Antialiasing)

        self.widget.addWidget(self._chart_view)


class DonutWidget:
    def __init__(self, pie):
        self.pie = pie                                                  # 初始化饼图
        self.donuts = []                                                # 初始化饼图列表
        self.chart_view = QChartView()                                  # 初始化图表视图
        self.chart_view.setRenderHint(QPainter.Antialiasing)            # 设置抗锯齿
        self.chart = self.chart_view.chart()                            # 获取图表
        self.chart.legend().setVisible(False)                           # 隐藏图例
        # self.chart.setTitle("用户统计")                                # 设置图表标题
        self.chart.setTheme(QChart.ChartThemeDark)                      # 设置图表主题
        # 设置图表的背景颜色
        self.chart.setBackgroundBrush(QColor(0, 0, 0, 0))                # 设置图表的背景颜色
        self.chart.setAnimationOptions(QChart.AllAnimations)            # 设置动画效果

        self.min_size = 0.1                                             # 最小占比
        self.max_size = 1                                               # 最大占比
        self.donut_count = 5        # donut 圈数    

        self.add_donut()                                                # 添加饼图

        # create main layout                                            # 创建主布局
        self.main_layout = self.pie                                     # 主布局为饼图
        self.main_layout.addWidget(self.chart_view, 1)                  # 添加图表视图
        # self.setLayout(self.main_layout)                              # 设置主布局

        self.update_timer = QTimer()                                    # 初始化定时器
        self.update_timer.timeout.connect(self.update_rotation)         # 设置定时器超时信号
        self.update_timer.start(1000)                                   # 启动定时器

    def add_donut(self):
        for i in range(self.donut_count):                              # 循环添加饼图
            donut = QPieSeries()                                                # 创建一个饼图
            slccount = randrange(3, 6)                                          # slice 圈数
            for j in range(slccount):
                value = randrange(100, 200)                                     # slice 值

                slc = QPieSlice(str(value), value)                              # 创建一个 slice
                slc.setLabelVisible(True)                                       # 显示 slice 标签
                slc.setLabelColor(Qt.white)                                     # slice 标签颜色
                slc.setLabelPosition(QPieSlice.LabelInsideTangential)           # slice 标签位置

                # Connection using an extra parameter for the slot
                slc.hovered[bool].connect(partial(self.explode_slice, slc=slc))     # slice 鼠标悬浮事件

                donut.append(slc)                                                   # 添加 slice 到饼图
                size = (self.max_size - self.min_size) / self.donut_count       # slice 大小
                donut.setHoleSize(self.min_size + i * size)                     # 设置饼图的孔大小
                donut.setPieSize(self.min_size + (i + 1) * size)                # 设置饼图的大小

            self.donuts.append(donut)                                           # 添加饼图到列表
            self.chart_view.chart().addSeries(donut)                            # 添加饼图到图表

    def update_rotation(self):                                                  # 更新饼图旋转角度
        for donut in self.donuts:                                               # 遍历所有饼图
            phase_shift = randrange(-50, 100)                                   # 饼图旋转角度
            donut.setPieStartAngle(donut.pieStartAngle() + phase_shift)         # 更新饼图旋转角度
            donut.setPieEndAngle(donut.pieEndAngle() + phase_shift)             # 更新饼图旋转角度

    def explode_slice(self, exploded, slc):                                     # slice 是否被挤压
        if exploded:                                                            # slice 被挤压
            self.update_timer.stop()                                            # 停止更新饼图旋转角度
            slice_startangle = slc.startAngle()                                 # slice 开始角度
            slice_endangle = slc.startAngle() + slc.angleSpan()                 # slice 结束角度

            donut = slc.series()                                                # 获取 slice 对应的饼图
            idx = self.donuts.index(donut)                                      # 获取饼图在列表中的索引
            for i in range(idx + 1, len(self.donuts)):                          # 遍历所有饼图
                self.donuts[i].setPieStartAngle(slice_endangle)                 # 更新饼图开始角度
                self.donuts[i].setPieEndAngle(360 + slice_startangle)           # 更新饼图结束角度
        else:
            for donut in self.donuts:                                           # 遍历所有饼图
                donut.setPieStartAngle(0)                                       # 更新饼图开始角度
                donut.setPieEndAngle(360)                                       # 更新饼图结束角度

            self.update_timer.start()   

        slc.setExploded(exploded)                                               # 更新 slice 是否被挤压
