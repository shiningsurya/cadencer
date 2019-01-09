# Edit this file to your liking!
# don't take the function signature tho
import matplotlib.pyplot as plt
def Plotter(mj,obs='gmrt',fname='cadence.png'):
        inpta = mj.keys()
        plt.figure()
        leg = []
        for i,pul in enumerate(inpta):
                ty = [i+1] * len(mj[pul])
                plt.scatter(mj[pul],ty,label=pul + ": " +str(len(mj[pul])))
                leg.append(pul + "[" + str(len(mj[pul])) + "]")
        plt.xlabel('MJD')
        plt.title('Cadence sheet | '+ obs.upper() )
        plt.ylabel('Pulsar[Number of Obs]')
        plt.yticks(range(1, 1+len(inpta)),leg,rotation=20)
        plt.gca().xaxis.grid(b=None)
        plt.tight_layout()
        plt.savefig(fname)
