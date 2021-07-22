# implementing a binary search tree:

class binary_search_tree (object) :
	def __init__(self, val = None):
		self.val = val
		self.left_ch = None
		self.right_ch = None

	def isEmpty(self):
		return self.val == self.left_ch == self.right_ch == None


	def insert(self, val):
		if (not self.val) :
			self.val = val
		else:
			cur_val = self.val
			if (cur_val > val) :
				if not self.left_ch:
					self.left_ch = binary_search_tree(val)
				else:
					self.left_ch.insert(val)
			else:
				if not self.right_ch:
					self.right_ch = binary_search_tree(val)
				else:
					self.right_ch.insert(val)

	def display_ascend(self):
		# displaying left-center-right bottom-up
		if (not self.val):
			print('[empty]')
		else:
			if self.left_ch :
				self.left_ch.display_ascend()
			print(self.val)
			if self.right_ch :
				self.right_ch.display_ascend()

	def sorted_list(self):
		# going left-center(root)-right, bottom-up
		if not self.val:
			return []
		else:
			sorted_l = []
			if self.left_ch :
				sorted_l = self.left_ch.sorted_list()
			sorted_l.append(self.val)
			if self.right_ch :
				sorted_l = sorted_l + self.right_ch.sorted_list()
			return sorted_l

	def smallest(self):
		if not self.left_ch:
			return self.val
		else:
			return self.left_ch.smallest()


	def largest(self):
		if not self.right_ch:
			return self.val
		else:
			return self.right_ch.largest()

	def contains_value(self, q_val):
		if self.val :
			if (self.val == q_val):
				return True
			elif (q_val < self.val) :
				if self.left_ch : 
					return (self.left_ch).contains_value(q_val)
			else:
				if self.right_ch :
					return self.right_ch.contains_value(q_val)
		return False
	def print_tree(self):
		# go root-[left-right]
		if self.val :
			print(self.val)
			if self.left_ch :
				print("/")
				self.left_ch.print_tree()
			if self.right_ch :
				print("\\")
				self.right_ch.print_tree()

	def depth(self):
		if self.val:
			dep = 1
			l_depth = 0
			r_depth = 0
			if self.left_ch:
				l_depth = self.left_ch.depth()
			if self.right_ch:
				r_depth = self.right_ch.depth()
			return dep + max(l_depth, r_depth)
		return 0


if __name__ == '__main__':
	my_tree = binary_search_tree(5)
	numbers = [2,7,3,0,5, 5, 1, -1, 9, 4]
	for num in numbers:
		my_tree.insert(num)

	print("displaying in ascending order:")
	print(my_tree.sorted_list())
	print("tree depth is", my_tree.depth())
