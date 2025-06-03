# binary min-heap
# we're representing the heap using a list

class binary_min_heap (object):
	def __init__(self):
		self.heap_list = []
		self.length = 0

	def __swap(self, i, j):
		# swaps two elements in the heap
		temp = self.heap_list[i]
		self.heap_list[i] = self.heap_list[j]
		self.heap_list[j] = temp

	def insert(self, val):
		if self.length < len(self.heap_list):
            		self.heap_list[self.length] = val
        	else:
            		self.heap_list.append(val)
		self.length += 1
		
		j = self.length - 1 # current index of the inserted value
		finished = False
		while (j > 0) and (not finished):
			if (j % 2 == 0):
				par_i = (j-2) // 2	# the parent index
			else:	# j is odd
				par_i = (j-1) // 2	# the parent index
			if self.heap_list[par_i] > self.heap_list[j]:
				# swap them!
				self.__swap(j, par_i)
				j = par_i
			else:
				finished = True

	def __slide_down(self, i):
		# sliding down an element at place i, if needed, to maintain (min) heap-property
		leng = self.length
		s = i 	# index of current element to be slided
		while (s < leng):
			if (2*s + 1 <= leng):	# if there exists left child
				left_child = self.heap_list[2*s + 1]	
				if (2*s + 1 <= leng):	# if there's also right child: (if no left, than also no right)
					right_child = self.heap_list[2*s + 2]
					# check who's smaller, if even one of then is smaller than the parent
					if left_child < right_child:
						swap_i = 2*s + 1
					else:
						swap_i = 2*s + 2
				else:	# there's only left child
					swap_i = 2*s + 1
			# in case we need to swap:
			if (self.heap_list[s] > self.heap_list[swap_i]):
				self.__swap(s, swap_i)
				s = swap_i
			else: #no need to swap: stop!
				break

	def erase_by_index(self, i):
		# erase element situated in place i
		# method: swap it with the last one, delete, and slide the previously last one to a correct position.
		last_i = self.length - 1
		last = self.heap_list[last_i]	# last element
		self.__swap(i, last_i)
		
		# erase new-last element and decrease length:
		del self.heap_list[last_i]
		self.length -= 1
		# slide down the new i-th element, if needed:
		self.__slide_down(i)

	def min_val(self):
		return (self.heap_list)[0]

	def display_list(self):
		return self.heap_list


if __name__ == '__main__':
	heap = binary_min_heap()
	values = [5, 10, 7, 13, 20, 8, 16, 17, 14]
	for val in values:
		heap.insert(val)
	print(heap.display_list())
	heap.erase_by_index(0)
	print(heap.display_list())
