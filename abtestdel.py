import database
from dashboard import draw_barplot
from dashboard import draw_pie
from dashboard import draw_simple_barplot
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import time
from IPython.display import IFrame


fig, ax = plt.subplots(figsize=(20, 10))
data3 = pd.read_csv("./database.csv", encoding='utf-8', thousands=',')
draw_pie(data=data3, column='sculpture', ax=ax, title='A/B 테스트')
fig.savefig("static/img/ab_test.jpeg")