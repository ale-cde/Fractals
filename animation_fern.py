#%%
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
# colors and stuff
fig=plt.figure(figsize=(1.5*5.5,1.5*6),facecolor='black')
ax=plt.axes()
ax.spines['bottom'].set_color('white')
ax.spines['top'].set_color('white') 
ax.spines['right'].set_color('white')
ax.spines['left'].set_color('white')
ax.set_facecolor('black')
plt.axis([-2.1820,2.6558,0,9.9983])
# getting the data
x_data=[0]
y_data=[0]
for i in range(50000):
    p=np.random.rand()
    x=x_data[-1]
    y=y_data[-1]
    if p<0.01:
        next_x=0
        next_y=0.16*y
    elif p<0.86:
        next_x= 0.85*x + 0.04*y
        next_y=-0.04*x + 0.85*y + 1.6
    elif p<0.93:
        next_x= 0.20*x - 0.26*y
        next_y= 0.23*x + 0.22*y + 1.6
    else:
        next_x=-0.15*x + 0.28*y
        next_y= 0.26*x + 0.24*y + 0.44
    x_data.append(next_x)
    y_data.append(next_y)
#animating the data
def ani(i):
    p=100
    n=i*p
    m=i*p+(p-1)
    if m>50000:
        a.event_source.stop()
    thisx=x_data[n:m]
    thisy=y_data[n:m]
    plt.plot(thisx,thisy,'.',color='#00cf18',markersize=1.5)
a=animation.FuncAnimation(fig,ani,fargs=(),interval=1,save_count=500)
writervideo = animation.FFMpegWriter(fps=60)
a.save('fern.mp4',writer=writervideo)
#plt.show()
# %%
