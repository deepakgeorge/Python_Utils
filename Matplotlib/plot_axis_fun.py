
import matplotlib.pyplot as plt
def plot_axis(x,y,ax,ylab,xlab):  
    #ax.set_title('visualization')
    ax.plot(x,y, linestyle= '-', lw=1)
    ax.set_ylabel(ylab)
    ax.set_xlabel(xlab)
    
fig = plt.subplots(nrows=2, ncols=1,sharex=True)
fig[1][0].set_title('Fts Vs Age')
plot_axis(x=basic_ft_base['age'],y=basic_ft_base['rms'],ax=fig[1][0],ylab='rms',xlab='age')
plot_axis(x=basic_ft_base['age'],y=basic_ft_base['kurt'],ax=fig[1][1],ylab='kurt',xlab='age')
