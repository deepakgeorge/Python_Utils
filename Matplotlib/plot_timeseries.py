import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

rng = pd.date_range('1/1/2017', periods=72, freq='H')

ts = pd.concat([pd.DataFrame(rng),
                pd.DataFrame(np.random.uniform(low=1000, high=10000, size=(len(rng),))),
                pd.DataFrame(np.random.uniform(low=1000, high=10000, size=(len(rng),))),
                pd.DataFrame(np.random.uniform(low=1000, high=10000, size=(len(rng),))),
                pd.DataFrame(np.random.uniform(low=1000, high=10000, size=(len(rng),))),
                pd.DataFrame(np.random.randint(low=0, high=2, size=(len(rng),)))
                ],1)

ts.columns = ['DateTime', 'Revenue1','Revenue2','Sales1','Sales2','Score']


def plot_ts(df, varlist,var_name, var2, score, dt):
    fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1,sharex=True)
    plt.subplots_adjust(left=None, bottom=None, right=None,top=None, wspace=None,hspace=0.2)#hspace adjust gap between the 2 subplodf

    ax1.set_title(var_name + ' Profile')
    for i in varlist:
        ax1.plot(df[dt],df[i], linestyle= '-', lw=1.5)
        ax1.set_ylabel(var_name)
    #bbox_to_anchor=(0.2,-0.15) sepecify starting position with reference 0,0 of the plot. -0.15 implies below the plot
    ax1.legend(bbox_to_anchor=(0.4,-0.10), loc=3,ncol=10,borderaxespad=0, edgecolor='k').draggable() #ncol makes legend horizontal. give high value like 10 when not sure of number of legends
    ax1.tight_layout() #to prevent legend overlapping on the line series.
    #for creating seconfay axis
    sec = ax1.twinx()
    sec.plot(df[dt],df[score], color='k',linestyle= '-.', lw=3)

    ax2.plot(df[dt],df[var2], color='b',linestyle= '-', lw=1)
    ax2.set_xlabel(dt)
    ax2.set_ylabel(var2)


plt.close('all')

plot_ts(ts,
var_name = 'Revenue',
dt = 'DateTime',
varlist = ['Revenue1','Revenue2'],
score = 'Score',
var2 = 'Sales1')
