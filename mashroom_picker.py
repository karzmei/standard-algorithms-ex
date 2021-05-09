# mushroom picker on a line:

def mushroom_strategy(mushrooms, start, steps):
    """ given an array mushrooms of non-negatives which tells us how many mushrooms are in each spot
    and a starting position start, need to find best strategy to collect as many as possible given a limited number of steps.
    Cannot collect twice from the same spot (ie after one time the mushrooms there are zero but can still pass this spot). 
    Each step is one step left or right. 
    Returns the total max sum of collected mushrooms under the constrains and the amount of effective steps to the right."""

    # create prefix sums array:
    length = len(mushrooms)
    prefix_sums = []
    for i in range(length):
        if i == 0:
            prefix_sums.append(mushrooms[i])
        else:
            prefix_sums.append(prefix_sums[i-1] + mushrooms[i])

    # find the best route:
    max_sum = 0
    steps_to_right = 0
    for to_right in range(0, min(steps, length-1 - start) +1):
        right = start + to_right
        left = start - (steps - 2*to_right)
        if left <= 0:
            result_sum = prefix_sums[right]
        else:
            result_sum = prefix_sums[right] - prefix_sums[left-1]
        if result_sum > max_sum:
            max_sum = result_sum
            steps_to_right = to_right

    return max_sum, steps_to_right




if __name__ == '__main__':
    mushrooms = [2,3,7,5,1,3,9]
    print("The mushrooms field looks like:", mushrooms)
    starting = 4
    steps_limit = 6
    print("starting at", starting, "and having energy for", steps_limit, "steps.")
    
    max_sum, steps_right = mushroom_strategy(mushrooms, starting, steps_limit)
    print("The best way is first go right for", steps_right, "steps, then go left:\nthis way you get", max_sum, "mushrooms, pal.")

