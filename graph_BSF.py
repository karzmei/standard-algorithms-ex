# directed graph with weighted edges, no double edges, possibly loops and BFS

""" Directed graph, weighted, possibly with loops (edges from vertex to itself), *NO double edges*.
There's a dictionary of vertices, and for each vertex there are two *dictionaries* of neighbors;
one of outgoing nhbrs and one for incoming, that is, if there's an edge from u to v, 
then v appears in the outgoing dictionary of u, 
and u appears in the incoming dictionary of v.
And for each member of the dictionaries we have the edge weight.
"""
import math

class dgraph (object):
	def __init__(self, vertices = None):
		if not vertices:
			vertices = set()
		self.__vertices = vertices
		self.__outgoing = {vertex: {} for vertex in vertices}
		self.__incoming = {vertex: {} for vertex in vertices}


	def add_vertex(self, vertex):
		if vertex in self.__vertices:
			print("Error: this vertex name already exists.")
		else:
			self.__vertices.add(vertex)
			self.__outgoing[vertex] = {}  # empty dict of adjacent vertices
			self.__incoming[vertex] = {}

	def erase_vertex(self, vertex):
		if vertex not in self.__vertices:
			print(vertex, "? No such vertex in the graph so nothing to remove")
			return
		# remove vertex from all nhbrs dictionaries:
		for u in self.__vertices:  
			# go over all the vertices and erase appearances of vertex as a nhbrs
			self.erase_edge(u, vertex)
		self.__vertices.remove(vertex)
		del self.__outgoing[vertex]
		del self.__incoming[vertex]

	def add_edge(self, start_v, end_v, weight = 1):
		if (start_v in self.__vertices) and (end_v in self.__vertices):
			self.__outgoing[start_v][end_v] = weight  # could be double edges
			self.__incoming[end_v][start_v] = weight  # could also put -weight, but ok.
		else:
			print("At least one of the given vertices doesn't exist in the graph.")

	def erase_edge(self, start_v, end_v):
		if (start_v in self.__vertices) and (end_v in self.__outgoing[start_v]):
			del self.__outgoing[start_v][end_v]
			del self.__incoming[end_v][start_v]

	def print_vertices(self):
		print("The vertices are:", self.__vertices)

	def print_out_nbhrs(self, vertex):
		if vertex in self.__vertices:
			print("The out-neighbors of", vertex, "are:", self.__outgoing[vertex])
		else:
			print("Are you sure about", vertex, "? There is no such vertex in the graph.")

	def get_vertices(self):
		return self.__vertices

	def get_out_nhbrs(self, vertex):
		if vertex in self.__vertices:
			return self.__outgoing[vertex].keys()
		else:
			print("No such vertex.")

	def get_in_nhbrs(self, vertex):
		if vertex in self.__vertices:
			return self.__incoming[vertex].keys()
		else:
			print("No such vertex.")

	def get_out_nhbr_w(self, vertex):
		if vertex in self.__vertices:
			return self.__outgoing[vertex]
		else:
			print("No such vertex.")

	def get_in_nhbr_w(self, vertex):
		if vertex in self.__vertices:
			return self.__incoming[vertex]
		else:
			print("No such vertex.")



def dgraph_bfs(G, s):
	""" Performs a breadth-first-search on G starting at the source s.
	Returns:
	- for each vertex u, its distance from s,
	- for each vertex u, its "predecessor" (in the specific scanninng srating at s)
	* colors are 0 (white), 1 (gray), 2 (black)
	"""
	vertices = G.get_vertices()
	# initializing for all vertices
	colors = {vertex: 0 for vertex in vertices}
	preds = {vertex: None for vertex in vertices}
	dists = {vertex: math.inf for vertex in vertices}
	# initializing expecially for the sourse:
	dists[s] = 0
	colors[s] = 1
	# let the scanning begin
	que = [s]	# that's going to be a fifo queue
	while que:  # is not empty
		cur = que.pop(0)	# take out first element
		cur_d = dists[cur]	# distance of cur to source
		
		# look at all th neighbors that are NOT covered yet (could happen if there are some loops)
		all_ws = G.get_out_nhbr_w(cur)
		all_nhbrs = list(all_ws)
		nhbrs = []
		nhbrs_ws = {}
		for u in all_nhbrs:
			if colors[u] == 0 :
				nhbrs.append(u)
				nhbrs_ws[u] = all_ws[u]

		# update queue are the parametes color, distance, predcessor for all new nhbrs
		que.extend(nhbrs) 	# add nhbrs to queue (unless they already there)
		colors.update({u: 1 for u in nhbrs})
		preds.update({u : cur for u in nhbrs})
		# update only new distance is smaller - BUT from what i did every vertex can only be visited once anyway.. that's not good. :q
		for u,w in nhbrs_ws.items():
			if (cur_d + w < dists[u]) :
				dists[u] = cur_d + w
		
		# finished with current element
		colors[cur] = 2
	return preds, dists




if __name__ == '__main__':
	G = dgraph()

	G.add_vertex(1)
	G.add_vertex(2)
	G.add_edge(1,2)
	G.add_vertex(3)
	G.add_edge(1,3)
	G.add_edge(2,3)
	G.add_vertex(4)
	G.add_edge(2,4)
	G.add_vertex(5)
	G.add_edge(4,5)
	G.add_edge(2,2)
	G.add_edge(3,2)
	G.add_edge(3,4)

	G.print_out_nbhrs(1)
	
	preds, dists = dgraph_bfs(G, 2)
	print(preds)
