# RAIL formats modules

The code here is for RAIL-specific data formats.

## Philosophy

We need generic containers for information passed between `rail.creation.Creator` objects, `rail.estimation.Estimator objects`, and `rail.evaluation.Evaluator` objects.
This information will likely be a mix of (serializable?) structures with some notion of provenance, providing a route to mutually blind `Creator`s, `Estimator`s, and `Evaluator`s from one another.
Even information that only passes between methods of one of these classes may be better off shunted to a specialized data type to minimize passing state around, as it expands the flexibility of the experimental design.

## Minimal requirements

## Eventual goals
