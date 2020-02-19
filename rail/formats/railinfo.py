"""
A superclass for RAIL data types
"""

from __future__ import absolute_import
__all__ = ['RAILInfo']

import rail

Info_ = namedtuple('Info', ['origin', 'scope', 'content'])
# Any Info_ object is just a little wrapper for some content.
# `scope` would represent something like "public" or "private", so we could ensure that `Creator`s, `Estimator`s, and `Evaluator`s can only use information that they're supposed to, like a backup system to blinding the experiment.
# I'm still not sure what "origin" would look like, but all information should come with some indicator of how it was made, even if that information does not get passed to the `Creator`s, `Estimator`s, and `Evaluator`s.
# On the other hand, it may be better to keep the provenance away from railinfo.Info_ to maintain blinding, instead having `Public`, `Private`, etc. be the subclasses of the RAILInfo object.

class RAILInfo(object):

    def __init__(self):
        """
        An object that constrains information for RAIL functionality

        Parameters
        ----------

        Notes
        -----
        I'm writing this like it's basically a dict, but it could be structured in a variety of ways.
        The important things at this stage are what its methods and attributes are and how we want to interact with them, and we can revise the underlying framework later.
        """
        self.contents = {}

    def add(self, key, value):
        """
        Adds a piece of information to the RAILInfo object

        Parameters
        ----------
        key: string
            what the RAILInfo object calls this information
        value: Info namedtuple
            a named tuple of information to include in the RAILInfo ensemble

        Notes
        -----
        This could be adapted to use the `+` syntax.
        More importantly, we can specify an acceptable set of `key`s to standardize the way the `Creator`s, `Estimator`s, and `Evaluator`s interact with it.
        """
        self.contents[key] = value
        return

    def write(self, fileloc):
        """
        Saves the RAILInfo object

        Parameters
        ----------
        fileloc: string
            where to save the file
        """
        pass
