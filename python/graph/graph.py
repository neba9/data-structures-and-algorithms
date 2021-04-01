
class Vertex:

  def __init__(self, value):
    self.value = value 

class Edge:

  def __init__(self, vertex, weight=1):
    self.vertex = vertex
    self.weight = weight


class Graph:

  def __init__(self):
    self._adjacency_list = {}


  def add_node(self, value):
    vertex = Vertex(value)
    self._adjacency_list[vertex] = []

    return vertex

  def add_edge(self, start_vertex, end_vertex, weight=1):

    if start_vertex not in self._adjacency_list:
      raise KeyError('start vertex not in graph')

    if end_vertex not in self._adjacency_list:
      raise KeyError('End Vertex is not i graph')

    edge = Edge(end_vertex, weight)
    adjacencies = self._adjacency_list[start_vertex]
    
    return adjacencies.append(edge)

  def get_node(self):
    return self._adjacency_list.keys()

  def get_neighbor(self, vertex):
    return self._adjacency_list[vertex]

  def size(self):
    return len(self._adjacency_list)



