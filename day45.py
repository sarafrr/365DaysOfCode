# pandas - plotting

import pandas as pd
import matplotlib.pyplot as plt

# using only a list we would not have
# a name for the plot and we have to use a
# dictionary
y = {'x':[1,2,3,4], 'f(x)':[2,4,6,8], 'g(x)':[12,14,16,18]}

graph = pd.DataFrame(y,y['x'])
# print the whole data frame of pandas
print(graph)
# print a column of a data frame of pandas
print('graph[\'f(x)\']:', graph['f(x)'], sep='\n')

graph.plot(kind='line', grid=True, title="title of the graph0",
           ylabel='y0', xlabel = 'x0', xlim=(1,4))
plt.show()

# to make a scatter plot we have to specify both x and y
# and both has to be part of the dataframe
# we can pass both the index of the column and the name in the dataframe
graph.plot(kind='scatter', x = 0, y = 1, grid=True, title="title of the graph1",
           ylabel='y1', xlabel = 'x1', xlim=(1,4))
plt.show()


