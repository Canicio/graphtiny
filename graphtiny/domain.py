import numpy as np


class Chart(object):

    def __init__(self) -> None:
        self.plot = None
        self.curve = None
        self.downsampling = 'peak'
        self.clipToView = True
        self.line_color = 'r'
        self.ptr = 0
        self.x = np.zeros(9000)
        self.y = np.zeros(9000)
        self.left_label = ''
        self.left_label_units = ''
        self.bottom_label = ''
        self.bottom_label_units = ''


class DataStreamWindow(object):

    def __init__(self) -> None:
        self.qapp = None
        self.win = None
        self.charts_list = list()
        self.columns_display = 1
        self.background_color = 'w'
        self.coordinate_system_color = 'b'
