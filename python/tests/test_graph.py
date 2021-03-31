import pytest
from graph.graph import Graph, Vertex, Edge

def test_add_vertex_pass():
  vertex = Vertex('a')
  actual = vertex.value
  expected = 'a'
  assert actual == expected

def test_add_vertex_fail():
  vertex = Vertex('a')
  actual = vertex.value
  expected = 'b'
  assert actual != expected

def test_add_node():
  graph = Graph()
  expected = 'a'
  actual = graph.add_node('a').value
  assert expected == actual

def test_add_edge_true():
  graph = Graph()
  a = graph.add_node('a')
  b = graph.add_node('b')
  graph.add_edge(a, b)
  assert True

def test_size():
  graph = Graph()
  graph.add_node('a')
  graph.add_node('b')
  expected = 2
  actual = graph.size()
  assert actual == expected

def test_size_fail():
  graph = Graph()
  graph.add_node('a')
  graph.add_node('b')
  expected = 3
  actual = graph.size()
  assert actual != expected

def test_get_node():
  graph = Graph()
  graph.add_node('a')
  graph.add_node('b')
  graph.add_node('c')
  graph.add_node('d')
  expected = 4
  actual = len(graph.get_node())
  assert actual == expected

def test_get_node_fail():
  graph = Graph()
  graph.add_node('a')
  graph.add_node('b')
  graph.add_node('c')
  graph.add_node('d')
  expected = 7
  actual = len(graph.get_node())
  assert actual != expected

def test_get_neighbor():
  graph = Graph()
  a = graph.add_node('a')
  b = graph.add_node('b')
  graph.add_edge(a, b, 1)
  



