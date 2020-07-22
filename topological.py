import heapq
import typing


class CyclicDependencyError(ValueError):
    """Raised whe a circular dependency is found"""


def sort(dag: typing.Dict[typing.Any, typing.Set[typing.Any]],
         weights: typing.Dict[typing.Any, int] = {}) \
             -> typing.List[typing.Any]:
    """Perform a topological sort on provided graph

    :raises: CyclicDependencyError

    """
    data = dag.copy()
    data.update({dep: set()
                 for node in dag for dep in dag[node]
                 if dep not in dag})

    for node, deps in data.items():
        data[node].discard(node)
        for dep in deps:
            if node in data[dep]:
                raise CyclicDependencyError(
                    'Circular dependency between {} and {}'.format(node, dep))

    result = []
    while data:
        leaves = [(weights.get(k2, 1), k2) for k2 in
                  [k1 for k1 in data.keys() if not data[k1]]]
        heapq.heapify(leaves)
        for _, node in leaves:
            del data[node]
            result.append(node) if node else None
            for other in data:
                data[other].discard(node)
    return result
