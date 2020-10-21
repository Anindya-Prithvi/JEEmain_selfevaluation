import matplotlib.pyplot as pl
import numpy as np
def analyzergraph(nam,timeq):
    X=np.array(range(1,76))
    pl.xticks(X,np.array(range(1,76)))
    Y=np.array(timeq)
    pl.ylabel("Time taken in Minutes")
    pl.xlabel("Question number")
    pl.bar(X,Y)
    pl.show()
    pl.title(nam)
