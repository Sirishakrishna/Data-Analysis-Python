# read csv file and convert to html file

import pandas as py

data1= py.read_csv('/home/sirisha/Videos/vastdata.csv',index_col=0)
data1.to_html('data2.html')