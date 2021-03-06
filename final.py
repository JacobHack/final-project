import pandas as pd 
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('Players.csv', index_col=0)
corr = df.corr()
blues = sns.color_palette("light:b", as_cmap=True)





plt.rcParams['figure.figsize'] = [10, 10]
plt.rcParams['figure.dpi'] = 200
plt.style.use("dark_background")
sns.set_style('whitegrid')
p = sns.heatmap(corr, cmap=sns.color_palette("mako", as_cmap=True))
for tick_label in p.get_yticklabels():
    tick_label.set_color("white")
for tick_label in p.get_xticklabels():
    tick_label.set_color("white")
p.get_figure().savefig("medals.png",bbox_inches='tight',transparent=False)