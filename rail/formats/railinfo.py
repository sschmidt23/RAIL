"""
A superclass for RAIL data types
"""

from __future__ import absolute_import
__all__ = ['RAILInfo']

import rail

Event_ = namedtuple('Event', ['origin', 'detail'])
# Info_ = namedtuple('Info', ['origin', 'scope', 'content'])
# Any Info_ object is just a little wrapper for some content.
# `scope` would represent something like "public" or "private", so we could ensure that `Creator`s, `Estimator`s, and `Evaluator`s can only use information that they're supposed to, like a backup system to blinding the experiment.
# I'm still not sure what "origin" would look like, but all information should come with some indicator of how it was made, even if that information does not get passed to the `Creator`s, `Estimator`s, and `Evaluator`s.
# On the other hand, it may be better to keep the provenance away from railinfo.Info_ to maintain blinding, instead having `Public`, `Private`, etc. be the subclasses of the RAILInfo object.

class RAILInfo(object):

    def __init__(self, data, metadata, scope='private', provenance=[]):
        """
        An object that constrains information for RAIL functionality

        Parameters
        ----------
        data: pandas.DataFrame
            tabular data, with rows for each galaxy
        metadata: dictionary
            non-tabular data, not specific to each galaxy
        scope: string; optional
            designation as 'private' or 'public' relative to `estimator` objects
            Note: This is logically equivalent to a boolean but might be less ambiguous to the user as string keyword.
        provenance: list, rail.Event; optional
            a list of rail.Event objects detailing the processes/configuration parameters that produced the RAILInfo object and any modifications made since its creation, if applicable
            Note: Perhaps this should also accommodate a string for the path to a file containing the provenance information?

        Notes
        -----
        I'm writing this like it's basically a dict, but it could be structured in a variety of ways.
        The important things at this stage are what its methods and attributes are and how we want to interact with them, and we can revise the underlying framework later.
        """
        self.data = data
        self.metadata = metadata

        self.scope = scope
        if scope == 'private':
            self.provenance = provenance

        self.contents = {'data': self.data, 'metadata': self.metadata}
        self.identity = {'scope': self.scope, 'data': self.data.keys, 'metadata': self.metadata.keys}

    def export(self, fn='railinfo.pkl', scope='private', data_keys=None, metadata_keys=None):
        """
        Creates a RAILInfo object from subset of current RAILInfo object

        Parameters
        ----------
        fn: string; optional
            path to which exported RAILInfo object should be saved
        scope: string; optional
            is the saved RAILInfo object 'public' or 'private'?
            Defaults to private to avoid accidental unblinding to `estimator` objects
        data_keys: tuple, string; optional
            column names of self.data to export
        metadata_keys: tuple, string; optional
            dictionary keys
        """
        if scope == 'private':
            outprovenance = self.provenance
            outprovenance.append(rail.Event('RAILInfo.export', self.identity))
        else:
            outprovenance = []

        outinfo = rail.RAILInfo(self.data[data_keys], self.metadata[metadata_keys], scope=scope, provenance=outprovenance)

        with open(fn, 'wb') as outfile:
            pickle.dump(outinfo, outfile)

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

    def read(self, fileloc, scope="public"):
        """
        Read a RAILInfo object from a file

        Parameters
        ----------
        fileloc: string
            where to find the file
        scope: string, optional
            "public" or "private"; None is equivalent to all
        """
        pass

    def write(self, fileloc, scope=None):
        """
        Saves the RAILInfo object

        Parameters
        ----------
        fileloc: string
            where to save the file
        scope: string, optional
            "public" or "private"; None is equivalent to all
        """
        pass
