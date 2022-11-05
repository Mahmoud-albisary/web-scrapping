from bokeh.plotting import  figure
from bokeh.io import output_file, show
from bokeh.models import NumeralTickFormatter,  HoverTool
import pandas

df = pandas.read_csv(r"C:\Users\Muh\web scrapping\final.csv")
count = []
ad = df["address"]
ad  = list(ad)
counts = df["price"]
counts = list(counts)
for items in counts:
    for item in items:
        try:
            int(item)
        except:
            items = items.replace(item, "")
    count.append(int(items))
print(count)

output_file("line.html")

f = figure(x_range=ad, plot_height=1000, plot_width = 2000, title="Fruit Counts", y_range=[0,1000000])
f.vbar(x = ad, top=count, width=0.85)
f.xgrid.grid_line_color = None
f.y_range.start = 0
f.yaxis.formatter=NumeralTickFormatter(format="0")

show(f)
