# `rail` overview

There are three aspects to the RAIL approach, plus infrastructure to support them, each defined by a minimal version that can be developed further as necessary.
The purpose of each major module is outlined below and described in a README in its own directory, where relevant code will ultimately live.

### creation

Code to forward-model mock data for testing redshift estimation codes, including physical systematics whose impact we wish to test

### estimation

Code to automatically execute arbitrary redshift estimation codes

### evaluation

Code to assess the performance of redshift estimation codes

### formats

Supporting code and custom data types

## Proposed Flow

These three parts to the RAIL will be nested into a class structure that should streamline creation of training sets, photo-z methods, and eventual evaluation of each.
This structure is proposed as follows:

- **RedshiftFramework class**: This contains the *creation* segment of the code to pass photometry to the estimation codes. This can have derived classes with hidden and variable true P(z,f)s and selection functions on the spectroscopic samples. The main benefit to this class is the avoidance of requiring fixed and specialized catalogs for each photo-z method's training. It will publicly provide
  - Wide field data to estimate P(z),
  - Deep/multi-band data,
  - Samples with spectroscopic redshifts on both,
  - The transfer function that takes deep field data to wide field observations (i.e. error models).

- **RedshiftMethod class**: This is the *estimation* segment that consists of a constructor that is passed an instance of RedshiftFramework, from which this class gets its data for training. Each derived class will be a separate photo-z method and should provide publicly
  - A function that returns p(z) given wide field fluxes and positions
  - Functions to write/read itself from file (instead of retraining each run).

- **Evaluation script/class**: This is the final script or class that will create instances of RedshiftFramework to pass into instances of RedshiftMethod. The inputs to each method can be modified and evaluated on various metrics, where we should take care to also evaluate ensembles of galaxies in a metric in addition to individual galaxy PDFs.
