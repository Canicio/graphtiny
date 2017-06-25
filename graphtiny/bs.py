from time import sleep
import pyqtgraph as pg
import threading
from graphtiny.api import IChart, IDataStreamWindow
from graphtiny.domain import DataStreamWindow, Chart


class FuncThread(threading.Thread):

    def __init__(self, t, *a) -> None:
        self._t = t
        self._a = a
        threading.Thread.__init__(self)

    def run(self) -> None:
        self._t(*self._a)


class ChartBS(IChart):

    def set_data_stream(self, chart: Chart, x, y) -> None:
        chart.x[chart.ptr] = x
        chart.y[chart.ptr] = y
        chart.ptr += 1


class DataStreamWindowBS(IDataStreamWindow):

    def launch_window(self, window: DataStreamWindow) -> None:
        calculating_thread = FuncThread(self.__raise_thread_with_window, window)
        calculating_thread.start()
        sleep(1)

    def __raise_thread_with_window(self, window: DataStreamWindow) -> None:
        window.qapp = pg.mkQApp()
        window.win = pg.GraphicsWindow()  # raise window!

        if window.background_color:
            window.win.setBackground(window.background_color)
        if window.coordinate_system_color:
            pg.setConfigOption('foreground', window.coordinate_system_color)

        i = 0
        for chart in window.charts_list:
            if i % window.columns_display == 0 and i >= window.columns_display:
                window.win.nextRow()
            chart.plot = window.win.addPlot()
            if chart.downsampling:
                chart.plot.setDownsampling(mode=chart.downsampling)
            if chart.clipToView:
                chart.plot.setClipToView(True)
            chart.curve = chart.plot.plot()
            if chart.line_color:
                chart.curve.setPen(chart.line_color)
            i += 1

        while window.win.isVisible():
            # refresh data
            for chart in window.charts_list:
                chart.curve.setData(chart.x[:chart.ptr], chart.y[:chart.ptr])
                window.qapp.processEvents()

