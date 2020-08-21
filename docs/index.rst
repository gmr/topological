topological
==================
The library provides two distinct functions, ``sort`` and ``weighted_sort``
    * ``sort`` function is an implementation of topological sorting of a given Directed Acyclic Graph (DAG)
    * ``weighted_sort`` is a customized verison of topological sort. This function takes two arguments, 
      one is ``dag`` and the other argument is ``weights`` for the nodes in the graph.
      The weights help to control the order of evaluating the nodes in the graph.
      The node with lowest weight is evaluated first among the siblings.
    * Generates CyclicDependencyError exception when cycles are detected in the input graph

The function takes two arugemnts one is bins configuration which is a ``py:typing.dict[py:typing.any, py:typing.list]`` and another parameter is bin to be adjusted ``py:typing.any``.

Python versions supported: 3.7+

Installation
------------
``topological`` is available on the Python package index and is installable via pip:

.. code:: bash

    pip3 install topological

Examples
--------

Topological sort

.. code-block:: python

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


Weighted topological sort

.. code-block:: python

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


Documentation
-------------

.. toctree::
   :maxdepth: 4

   sort
   weighted_sort
