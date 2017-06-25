from abc import ABCMeta, abstractmethod
from numpy.core.records import ndarray
from graphtiny.domain import Chart, DataStreamWindow


class IChart(metaclass=ABCMeta):

    @abstractmethod
    def set_data_stream(self, chart: Chart, x: ndarray, y: ndarray) -> None:
        """
        Introduces data stream in the chart
        :param chart: A Chart object
        :param x: A numpy array representing data stream of the x-axis
        :param y: A numpy array representing data stream of the y-axis
        """


class IDataStreamWindow(metaclass=ABCMeta):

    @abstractmethod
    def launch_window(self, window: DataStreamWindow) -> None:
        """
        Displays the window with its graphic content
        :param window: A DataStreamWindow object
        """

    @abstractmethod
    def __raise_thread_with_window(self, window: DataStreamWindow) -> None:
        """
        Run parallel thread to keep the window alive
        :param window: A DataStreamWindow object
        :return:
        """