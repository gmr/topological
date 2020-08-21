import unittest

import topological


class TopologicalSort(unittest.TestCase):
    def test_simple_dag(self):
        dag = {
            'b': {'a'},
            'c': {'b'},
            'd': {'b', 'c'},
            'e': {'d'},
            'f': {'a', 'b', 'd'}
        }
        expectation = ['a', 'b', 'c', 'd', 'e', 'f']
        self.assertListEqual(topological.sort(dag), expectation)

    def test_toposort_dag(self):
        dag = {2: {11}, 9: {11, 8, 10}, 10: {11, 3}, 11: {7, 5}, 8: {7, 3}}
        expectation = [3, 5, 7, 8, 11, 2, 10, 9]
        self.assertListEqual(topological.sort(dag), expectation)

    def test_circular_dependency(self):
        dag = {2: {11}, 9: {11, 8, 10}, 10: {11, 3}, 11: {2, 7, 5}, 8: {7, 3}}
        with self.assertRaises(topological.CyclicDependencyError):
            topological.sort(dag)

    def test_str_key_with_weights(self):
        dag = {'A': {'C'},  'B': {''}, 'C': {'B', 'D'}, 'D': {''}, 'E': {'C'}}
        weights = {'A': 10, 'B': 25, 'C': 17, 'D': 1, 'E': 10}
        expectation = ['D', 'B', 'C', 'A', 'E']
        self.assertEqual(topological.weighted_sort(dag, weights), expectation)

        dag = {'A': {'C'},  'B': {''}, 'C': {'B', 'D'}, 'D': {''}, 'E': {'C'}}
        weights = {'A': 10, 'B': 25, 'C': 17, 'D': 1, 'E': 1}
        expectation = ['D', 'B', 'C', 'E', 'A']
        self.assertEqual(topological.weighted_sort(dag, weights), expectation)

    def test_nbr_key_with_weights(self):
        dag = {2: {11}, 9: {11, 8, 10}, 10: {11, 3}, 11: {7, 5}, 8: {7, 3}}
        weights = {7: 1, 5: 1, 11: 1, 2: 1, 3: 1, 8: 1, 10: 1, 9: 1}
        expectation = [3, 5, 7, 8, 11, 2, 10, 9]

        dag = {2: {11}, 9: {11, 8, 10}, 10: {11, 3}, 11: {7, 5}, 8: {7, 3}}
        weights = {7: 1, 5: 2, 11: 1, 2: 1, 3: 10, 8: 1, 10: 1, 9: 1}
        expectation = [7, 5, 3, 8, 11, 2, 10, 9]
        self.assertEqual(topological.weighted_sort(dag, weights), expectation)

    def test_nbr_key_with_fewer_weights(self):
        dag = {2: {11}, 9: {11, 8, 10}, 10: {11, 3}, 11: {7, 5}, 8: {7, 3}}
        weights = {7: 1, 5: 2, 3: 10}
        expectation = [7, 5, 3, 8, 11, 2, 10, 9]
        self.assertEqual(topological.weighted_sort(dag, weights), expectation)
