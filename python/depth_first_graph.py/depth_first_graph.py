from graph.graph import Graph, Vertex

def depth_first_graph(self, start_vertex):
  
  out_put = []
  queue = [start_vertex]

  if start_vertex not in self._adjacency_list:
      raise KeyError('start Vertex is not i graph')

  # keep looping until there are nodes still to be checked
  while queue:
      vertex = queue.pop(0)
      if vertex not in out_put:
          # add vertex to list of checked vertexs
          out_put.append(vertex)
          neighbours = self.self._adjacency_list[vertex]

          # add neighbours of node to queue
          for neighbour in neighbours:
              queue.append(neighbour[vertex] - out_put)
              
  return out_put