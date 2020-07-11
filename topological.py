import typing


class CyclicDependencyError(ValueError):
    """Raised whe a circular dependency is found"""


def sort(dag: typing.Dict[typing.Any, typing.Set[typing.Any]]) \
        -> typing.List[typing.Any]:
    """Perform a topological sort on provided graph"""
    data = dag.copy()
    data.update({dep: set() for node in dag for dep in dag[node]
                 if dep not in dag})

    for node, deps in data.items():
        data[node].discard(node)
        for dep in deps:
            if node in data[dep]:
                raise CyclicDependencyError(
                    'Circular dependency between {} and {}'.format(node, dep))

    result = []
    while data:
        for node in sorted(k for k in data.keys() if not data[k]):
            del data[node]
            result.append(node)
            for other in data:
                data[other].discard(node)

    return result
