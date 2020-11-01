from mpl_toolkits.mplot3d import axes3d
import mpl_toolkits.mplot3d as mpl3d
import matplotlib.pyplot as plt

class LorenzPlotter:

    def __init__(self):
            
       
        plt.style.use(['dark_background']) 
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.xaxis.pane.fill = False
        self.ax.yaxis.pane.fill = False
        self.ax.zaxis.pane.fill = False
        self.ax.xaxis.pane.set_edgecolor('black')
        self.ax.yaxis.pane.set_edgecolor('black')
        self.ax.zaxis.pane.set_edgecolor('black')
        self.ax.grid(False)
        self.ax.set_title('Lorenz Attractor')
               



    def plt(self, p, savePath):

        self.ax.plot(p[0], p[1], p[2], 
                color='w', 
                alpha=0.5,
                linewidth=0.3)
        # self.ax.set_xlim((-30,30))
        # self.ax.set_ylim((-30,30))
        # self.ax.set_zlim((0,50))
        
        
        plt.savefig(savePath, dpi=100)
        # plt.show()
        plt.close()
