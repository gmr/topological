topological
===========
Python3 library of topological sorting algorithms

![Testing](https://github.com/gmr/topological/workflows/Testing/badge.svg)

Examples
--------

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
