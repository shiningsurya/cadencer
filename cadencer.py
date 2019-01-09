#! /usr/bin/python
import argparse
import numpy as np
import pickle
import fnmatch as fn
import os
import re
#####
parser = argparse.ArgumentParser(description='Create cadence plots.')
parser.add_argument("-d","--dir", default='.', help='Directory where all the J-dirs are')
parser.add_argument("-l","--jlist", type=argparse.FileType('r'),help='List of pulsars of which to make cadence sheet')
parser.add_argument("-p","--pickle", type=argparse.FileType('rwb'), help='Pickle filename')
parser.add_argument("-o","--obs", choices=['gmrt','ort'], help='Observatory name')
parser.add_argument("--plot", help='Plot filename')
parser.print_help()
args = parser.parse_args()
#####
if args.jlist is not None and args.pickle is not None:
        mj = dict()
        ita  = list(jlist.readlines())
        args.jlist.close()
        inpta = [x.strip() for x in ita]
        Pickler(args.dir) # make pickle 
        pickle.dump(mj, args.pickle) # dump pickle
        # plot
elif args.jlist is None and args.pickle is not None:
        mj = pickle.load(args.pickle) # load pickle
        # plot from pickle
if args.plot is not None:
        import matplotlib.pyplot as plt 
        Plotter(mj, obs=args.obs, fname=args.plot)
        # plotter
#####
p = re.compile('J\d{4}[+-]\d{2,4}[AB]*[_.](\d{5})\S*[prof,tim]*')
def xMJD(x):
        ret = []
        for ix in x:
                six = str(ix)
                ret.append(int(p.match(six).group(1)))
        return ret
def Pickler(root):
        for pul in inpta: 
                xrt = []
                for _,dl,fl in os.walk(root + '/' + pul + '/'):
                        xrt.append(xMJD(fl))
                        xrt.append(xMJD(dl))
                        break
                mjd = np.unique(np.array(xrt,dype=np.int))
                print "Pulsar {0} has {1} observations ranging from {2} to {3}".format(pul,len(mjd),min(mjd),max(mjd))
                mj[pul] = mjd 

def Plotter(mj,obs='gmrt',fname='cadence.png'):
        inpta = mj.keys()
        plt.figure()
        leg = []
        for i,pul in enumerate(inpta):
                ty = [i+1] * len(mj[pul])
                arried = np.array(mj[pul], dtype=np.int)
                plt.scatter(arried,ty,label=pul + ": " +str(len(mj[pul])))
                leg.append(pul + "[" + str(len(mj[pul])) + "]")
        plt.xlabel('MJD')
        plt.title('Cadence sheet | '+ obs.upper() )
        plt.ylabel('Pulsar[Number of Obs]')
        plt.yticks(np.arange(len(inpta))+1,leg,rotation=20)
        plt.gca().xaxis.grid(b=None)
        plt.tight_layout()
        plt.savefig(fname)
