# GraphTiny

A Python library that lets you display graphs in streaming, simply and easily. Especially suitable for scientific use.
<br>
<br>
It is an abstraction layer for the [PyQtGraph](https://github.com/pyqtgraph/pyqtgraph) library.
<br>
<br>

---

## Requirements
* Python 3.5+


## Install
```console
pip install graphtiny
```

## Examples

**Display graph in streaming with random values:**
```python
import random
from time import sleep
from graphtiny.service import ChartService, DataStreamWindowService
from graphtiny.domain import Chart, DataStreamWindow

window = DataStreamWindow()
chart1 = Chart()
window.charts_list.append(chart1)
DataStreamWindowService().launch_window(window)
chart_service = ChartService()
for i in range(5, 200):
    sleep(0.1)
    chart_service.set_data_stream(chart1, i, random.randrange(0, i))
```

<p align="center"><img src="https://camo.githubusercontent.com/b0bb052ea60d05e5401072cd5f557aaaaab43703/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f78543339446d6b3136726a724934757544362f67697068792e676966" /></p>


<br>
<br>

**You can display multiple graphs per window:**
```python
window = DataStreamWindow()
window.columns_display = 2
chart1, chart2, chart3, chart4 = Chart(), Chart(), Chart(), Chart()
window.charts_list.append(chart1)
window.charts_list.append(chart2)
window.charts_list.append(chart3)
window.charts_list.append(chart4)
DataStreamWindowService().launch_window(window)
chart_service = ChartService()
for i in range(5, 200):
    sleep(0.1)
    chart_service.set_data_stream(chart1, i, random.randrange(0, i))
    chart_service.set_data_stream(chart2, i, random.randrange(0, i))
    chart_service.set_data_stream(chart3, i, random.randrange(0, i))
    chart_service.set_data_stream(chart4, i, random.randrange(0, i))
```

<p align="center"><img src="https://camo.githubusercontent.com/483aa8b5f10db347b54cd20bc815d0857c2fb511/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f785433394354556d49395638324b4c78664f2f67697068792e676966" /></p>

<br>
<br>

**You can change the colors:**
```python
from graphtiny.util import Colors

window = DataStreamWindow()
window.background_color = Colors.BLACK  # black
window.coordinate_system_color = Colors.WHITE  # white
chart1 = Chart()
chart1.line_color = '#01DF01'  # green
```

<p align="center"><img src="https://camo.githubusercontent.com/84b491d4ead6734818b6205b8e99b21be35c43d5/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f7854333943597431493562544843486c62712f67697068792e676966" /></p>

<br>

## License
[MIT](LICENSE) (Massachusetts Institute of Technology)
