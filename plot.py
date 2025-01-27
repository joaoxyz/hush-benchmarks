import json
import re

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

progs = ['binary-trees', 'fannkuch-redux', 'fasta', 'regex-redux', 'spectral-norm']
results = []
for p in progs:
    with open(f"benchmarks/json/{p}.json") as res:
        results += json.load(res)["results"]

results = [{key: i[key] for key in i.keys() & {'command', 'mean'}} for i in results]

df = pd.json_normalize(results)
df['mean'] *= 100
df = df.round(1)
df['lang'] = df.apply(lambda row: row.command.split(' ', 1)[0].capitalize(), axis=1)
df['program'] = df.apply(lambda row: re.sub(r"([\s\S]*\/|\.[\s\S]*)", "", row.command), axis=1)
df = df.drop('command', axis=1)

g = sns.barplot(data=df, x="program", y="mean", hue="lang", edgecolor=".2")
#g.set(ylim=(0, 55))
g.set(yscale="log", xlabel="", ylabel="Média de tempo de execução dos programas (em ms)", title="")
for i in g.containers:
    g.bar_label(i,)
plt.yticks(ticks=[], labels=[])
handles, labels = g.get_legend_handles_labels()
g.legend(handles=handles, labels=labels)
g.tick_params(left=False, bottom=False)

g.get_figure().savefig("barplot.png")