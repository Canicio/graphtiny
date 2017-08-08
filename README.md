# GraphTiny

A Python library that lets you display graphics in streaming, simply and easily. Especially suitable for scientific use.
<br>
<br>
It is an abstraction layer for the [PyQtGraph](https://github.com/pyqtgraph/pyqtgraph) library.
<br>
<br>

---

## Requirements
* Python 3.5+
* PyQt 4.8+ or PySide
* PyQtGraph

## Install
```console
pip install graphtiny
```

## Examples

Display graphic in streaming with random values:
```python
import random
from time import sleep
from graphtiny.bs import ChartBS, DataStreamWindowBS
from graphtiny.domain import Chart, DataStreamWindow

window = DataStreamWindow()
chart1 = Chart()
window.charts_list.append(chart1)
DataStreamWindowBS().launch_window(window)
chart_bs = ChartBS()
for i in range(5, 200):
    sleep(0.1)
    chart_bs.set_data_stream(chart1, i, random.randrange(0, i))
```

![demo1](resources/graph_simple.mp4)
![demo11](resources/graph_simple.gif)


You can display multiple charts per window:
```python
window = DataStreamWindow()
window.columns_display = 2
chart1, chart2, chart3, chart4 = Chart(), Chart(), Chart(), Chart()
window.charts_list.append(chart1)
window.charts_list.append(chart2)
window.charts_list.append(chart3)
window.charts_list.append(chart4)
DataStreamWindowBS().launch_window(window)
chart_bs = ChartBS()
for i in range(5, 200):
    sleep(0.1)
    chart_bs.set_data_stream(chart1, i, random.randrange(0, i))
    chart_bs.set_data_stream(chart2, i, random.randrange(0, i))
    chart_bs.set_data_stream(chart3, i, random.randrange(0, i))
    chart_bs.set_data_stream(chart4, i, random.randrange(0, i))
```


![demo2](resources/graph_multi.mp4)

You can change the colors:
```python
window = DataStreamWindow()
window.background_color = 'k'  # black
window.coordinate_system_color = 'w'  # white
chart1 = Chart()
chart1.line_color = 'g'  # green
```

![demo3](resources/graph_colors.mp4)


## License
[MIT](LICENSE) (Massachusetts Institute of Technology)
