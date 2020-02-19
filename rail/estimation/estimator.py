"""
A superclass for estimators of redshift posterior PDFs
"""

from __future__ import absolute_import
__all__ = ['Estimator']

import rail
from rail.formats import Public
from rail.formats import Prior
from rail.formats import Data
from rail.formats import PDFs


class Estimator(object):

    def __init__(self, name=None):
        """
        An object that constrains redshifts of a sample of galaxies

        Parameters
        ----------
        name: string
            the name of the estimation routine

        Notes
        -----
        This is not the wrapper for redshift estimation codes!
        The wrapped codes, however, should be subclasses of the rail.estimator.Estimator class.
        """
        self.name = name

    def prepare(self, public_info, **kwargs):
        """
        Trains and/or tunes prior information based on available external information

        Parameters
        ----------
        public_info: rail.formats.Public object
            all external information available to the rail.estimator.Estimator object

        Returns
        -------
        prior_info: rail.formats.Prior object
            information necessary for Estimator.estimate(), derived from external_info

        Notes
        -----
        Since the format of prior_info is presumably unique to each estimator, it contains whatever information the estimator expects.
        The rail-specific format would just provide some bookkeeping functionality for us as experimenters.
        It is intentional that the rail.estimator.Estimator class does not carry around training inputs/outputs, to keep it lightweight and prevent spillover between experiments.
        """
        prior_info = rail.formats.Prior()
        return(prior_info)

    def estimate(self, data, prior_info, **kwargs):
        """
        Estimates redshift posterior PDFs of a galaxy sample with given data and requisite prior information

        Parameters
        ----------
        data: rail.formats.Data object
            all available data for a set of galaxies with unknown redshifts
        prior_info: rail.formats.Prior object
            prior information required for redshift posterior PDF estimation as processed from available external information by

        Returns
        -------
        estimates: rail.formats.PDFs object
            redshift posterior PDFs for the input data set

        Notes
        -----
        It might make sense for rail.formats.PDFs to actually be a qp.ensemble.Ensemble object (or an improved future version thereof) so the estimated redshift posteriors can remain in their native format and be easily convertible without reinventing the wheel on the metrics I/O.
        """
        estimates = rail.formats.PDFs()
        return(estimates)
