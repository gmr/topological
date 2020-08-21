topological
===========
Python3 library of topological sorting algorithms. 

![Testing](https://github.com/gmr/topological/workflows/Testing/badge.svg)

* ``sort`` function is an implementation of topological sorting of a given Directed Acyclic Graph (DAG)
* ``weighted_sort`` is a customized verison of topological sort. This function takes two arguments, 
      one is ``dag`` and the other argument is ``weights`` for the nodes in the graph.
      The weights help to control the order of evaluating the nodes in the graph.
      The node with lowest weight is evaluated first among the siblings.
* Generates CyclicDependencyError exception when cycles are detected in the input graph
Examples
--------
sort
```python
import topological

dag = {
    'b': {'a'},
    'c': {'b'},
    'd': {'b', 'c'},
    'e': {'d'},
    'f': {'a', 'b', 'd'}
}
expectation = ['a', 'b', 'c', 'd', 'e', 'f']
assert topological.sort(dag) == expectation

```
Weighted sort
```python
import topological

dag = {
    'b': {'a'},
    'c': {'b'},
    'd': {'b', 'c'},
    'e': {'d'},
    'f': {'a', 'b', 'd'}
}
weights = {'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 10, 'f': 1}
expectation = ['a', 'b', 'c', 'd', 'f', 'e']
assert topological.weighted_sort(dag) == expectation

```