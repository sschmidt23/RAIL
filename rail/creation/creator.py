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

class Creator(object):

    def __init__(self, params=None):
        """
        An object that makes mock data for redshift estimation experiments

        Parameters
        ----------

        Notes
        -----

        """
        self.params = params
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
