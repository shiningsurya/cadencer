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
parser.add_argument("-p","--pickle", help='Pickle filename')
parser.add_argument("-o","--obs", choices=['gmrt','ort'], help='Observatory name')
parser.add_argument("--plot", help='Plot filename')
args = parser.parse_args()
#####
p = re.compile('J\d{4}[+-]\d{2,4}[AB]*[_.](\d{5})\S*[prof,tim,fits]*')
def xMJD(x):
        ret = []
        for ix in x:
                six = str(ix)
		if p.match(six) is not None:
			ret.append(int(p.match(six).group(1)))
        return ret
def Pickler(root):
        for pul in inpta: 
                xrt = []
                for _,dl,fl in os.walk(root + '/' + pul + '/'):
                        xrt += xMJD(fl)
                        xrt += xMJD(dl)
                        break
                mjd = np.unique(np.array(xrt,dtype=np.int))
		if len(mjd) == 0:
			print "Pulsar {0} has {1} observations.".format(pul,len(mjd))
		else:	
			print "Pulsar {0} has {1} observations ranging from {2} to {3}".format(pul,len(mjd),min(mjd),max(mjd))
			mj[pul] = mjd 
#####
if args.jlist is not None and args.pickle is not None:
        mj = dict()
        ita  = list(args.jlist.readlines())
        args.jlist.close()
        inpta = [x.strip() for x in ita]
        Pickler(args.dir) # make pickle 
	with open(args.pickle,'wb+') as f:
		pickle.dump(mj, f) # dump pickle
        # plot
elif args.jlist is None and args.pickle is not None:
	with open(args.pickle,'rb') as f:
		mj = pickle.load(f) # load pickle
        # plot from pickle
elif args.jlist is not None and args.pickle is None:
        mj = dict()
        ita  = list(args.jlist.readlines())
        args.jlist.close()
        inpta = [x.strip() for x in ita]
        Pickler(args.dir) # make pickle 

if args.plot is not None:
        from plotter import Plotter
        Plotter(mj, obs=args.obs, fname=args.plot)
        # plotter
#####
