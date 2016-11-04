import matplotlib.pyplot as plt

x_väärtused_a = [100, 200, 300, 400]
y_väärtused_a = [1, 2, 3, 4]

x_väärtused_b = [500, 600, 700, 800, 900, 1000, 1100, 1200]
y_väärtused_b = [50, 60, 70, 80, 90, 100, 110, 120]

fig = plt.figure()          
ax2 = fig.add_subplot(1,1,1) 

ax = ax2.twinx()

ax2.plot(x_väärtused_a, y_väärtused_a, "o-b")
ax2.set_ylim(0, 13)
ax2.set_yticks([1,2,3,4])

ax.plot(x_väärtused_b, y_väärtused_b, "o-r") 
ax.set_ylim(0, 130)
ax.set_yticks([50,60,70,80,90,100,110,120])

ax.grid()
ax2.grid()
fig.show()                 