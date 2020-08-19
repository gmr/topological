topological
===========
Python3 library of topological sorting algorithms. 

The library provides two distinct functions, sort and weighted_sort.    
* sort function is a pure topological sorting of a Directed acyclic graph
* weighted_sort provides ability to define weights to nodes, to control the order of evaluating the dependencies of the nodes in the graph.


![Testing](https://github.com/gmr/topological/workflows/Testing/badge.svg)

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