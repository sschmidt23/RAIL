"""
A superclass for creators of mock data for redshift estimation experiments
"""

from __future__ import absolute_import
__all__ = ['Creator']

import rail
from rail.formats import Private
from rail.formats import Public
from rail.formats import Prior
from rail.formats import Joint
from rail.formats import Data
import pickle
import pomegranate as pm
import pandas as pd

class Creator(object):

    def __init__(self, file, TF = None, sel_fcn = None, params=None):
        """
        An object that supplies mock data for redshift estimation experiments from a smooth space

        Parameters
        ----------
        file   : smoothly interpolated space written to pickle file to be sampled for photometry
        TF     : transfer function
        sel_fcn: selection function as written to a pickle file
        params : additional parameters desired to be stored with the instance as a dictionary
        
        Notes
        -----
        Currently the Creator class does not generate the smoothly interpolated space from the DC2 data, but reads it in.

        """
        print('Loading {}'.format(paramfile))
        self.file = file #store which smooth space is used
        self.dataspace = pickle.load(open(paramfile,'rb')) #read in file and store space
        self.params = params
        self.TF = TF
        if TF = None:
            print('Setting transfer function to be None.')
        self.sel_fcn = sel_fcn
        
        #apply selection function if it exists
        if sel_fcn = None:
            print('Setting selection function to be None.')
        else:
            selection = pickle.load(open(sel_fcn,'rb'))
            self.dataspace = selection * self.dataspace #associated with creator instance, formalism may need to change
            print('Selection applied to data space.')
        
        print('File read in and object created.')
        pass
    
    def make_TF(self,fcn):
        """
        A simple function that initiates the transfer function and stores it on the object.
        
        Parameters
        ----------
        fcn : the desired transfer function taking deep information into noisier wide data
        
        Notes
        -----
        May want to read from file, or do in initialization stage.
        """
        self.TF = fcn
        pass
        
    
    def make_Pjoint(inputs = samples, paramfile):
        """
        A function that generates the joint probabilities for the input samples drawn from the DC2 space and returns a pomegranate mixing model.
        
        Parameters
        ----------
        inputs     : a pandas dataframe with galaxy samples, with true redshifts, photometry and photometric errors stored
        paramfile  : a pickle file with the parameterization required to make the joint probability
        """
        self.Pzparam = pickle.load(open(paramfile,'rb'))

        return pjoint
    

    def make_sel_fcn(self, sel_fcn, fileloc, tag = None):
        """
        Define the selection function applied to the color space and associate it with the creator instance
        
        Parameters
        ----------
        sel_fcn  : the selection function (format up for debate)
        fileloc  : the written out file location for the selection function, stored as a pkl
        tag      : specific suffix added to selection function
        
        Notes
        -----
        The formatting of this function could be as simple as a dictionary of cuts, though if more complex spaces 
        are desired we may want to grid the self.dataspace and supply a boolean at each point.
        """
        
        outfile = fileloc + 'sel_func_params_file' + tag +'.pkl'
        with open(outfile, 'wb') as handle:
            pickle.dump(fileloc,handle)
        
        print('Wrote {} to file.'.format(outfile))
        
        self.dataspace = sel_fcn * self.dataspace #associated with creator instance, formalism may need to change
        print('Selection applied to data space.')
        
        self.sel_fcn = outfile #store outfile function location
        pass
    
    
    def sample_pspace(self, n_gals=1e9, output_dims=('zTrue', 'g', 'r', 'i', 'z', 'y', 'gErr', 'rErr', 'iErr', 'zErr', 'yErr')):
        """
        
        Parameters
        ----------
        n_gals      : the number of galaxies in the desired sample
        output_dims : the desired fields for the sample
        
        Output
        ------
        A RAILinfo object with the prescribed fields drawn from the smooth space described by the file read in at initiation of the instance
        and stored in self.dataspace.
        
        Notes
        -----
        formulism may change after RAILinfo gets more developed
        """
        #get the sample from file
        print('Drawing {0} samples from {1}.'.format(n_gals,self.file))
        
        #store sample in rail.RAILinfo object, identifying the data frame as photometry and the metadata as other relevant parameters
        #sample = rail.RAILinfo(...)
        #sample.metadata = 
        #sample.data = 
        
        return sample

    
    def print_status(self):
        """
        Print a status of Creator to see what relevant files/functions are applied in this instance.
        """
        
        print('Smooth space         : {}'.format(self.file))
        print('Selection Function   : {}'.format(self.sel_fcn))
        print('Transfer Function    : {}'.format(self.TF))
        print('P(z) parametrization : {}'.format(self.Pzparam))
        #other parameters of interest .....
        pass


    def write(self, fileloc, scope=None):
        """
        Saves the Creator's data

        Parameters
        ----------
        fileloc: string
            where to save the file
        scope: string, optional
            "public" or "private"; None is equivalent to all
        """
        pass
