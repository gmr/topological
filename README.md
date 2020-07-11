topological
===========
Python3 library of topological sorting algorithms

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
