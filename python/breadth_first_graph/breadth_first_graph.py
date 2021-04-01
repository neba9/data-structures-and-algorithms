from graph.graph import Graph, Vertex

def breadth_first_graph(self, start_vertex):
  
  out_put = []
  queue = [start_vertex]

  # keep looping until there are nodes still to be checked
  while queue:
      vertex = queue.pop(0)
      if vertex not in out_put:
          # add vertex to list of checked vertexs
          out_put.append(vertex)
          neighbours = self.self._adjacency_list[vertex]

          # add neighbours of node to queue
          for neighbour in neighbours:
              queue.append(neighbour)
              
  return out_put

