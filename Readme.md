# Python Optimization Template

This template is a generic framework to develop software solutions that 
make decisions based on a given set of input parameters that are used to build
an optimization model.

# Properties

The solution method of the optimization model is abstracted out and the framework
supports the coexistence of multiple algorithms of any type to coexist within the same codebase. 

The framework is built with the idea of building a solution pool using multiple algorithms and afterwards evaluating
their quality based on a separate evaluation tool. This generalization allows the code to accomodate using more 
simplified models to find solutions and a model with higher fidelity and more complexities such as stochasticity, elasticity,
non-linearities to evaluate each solution. 


The main interface for the entry points in the InstanceManager found in `src/instance_manager.py` class which contains the links to all the relevant 
information of a given solve. An example of how this can be called can be found in the `scripts/main.py` file.