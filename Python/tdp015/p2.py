# TDP015 Programming Assignment 2
# Recursion
# Skeleton Code

# Do not use any imports!

# In this assignment you are asked to implement functions on *nested
# pairs*. The set of nested pairs is defined recursively:
#
# 1. The empty tuple () forms a nested pair.
#
# 2. If a and b are nested pairs, then the tuple (a, b) forms a nested
#    pair.
#
# Here are some examples of nested pairs sorted by their *degree*. The
# degree of a nested pair is the number of empty tuples contained in it.
#
# degree 1 (1 pair):
#
# ()
#
# degree 2 (1 pair):
#
# ((), ())
#
# degree 3 (2 pairs):
#
# ((), ((), ()))
# (((), ()), ())
#
# degree 4 (5 pairs):
#
# ((), ((), ((), ())))
# ((), (((), ()), ()))
# (((), ()), ((), ()))
# (((), ((), ())), ())
# ((((), ()), ()), ())
#
# The following sequence gives the number of nested pairs with degrees
# 1, 2, 3, ...:
#
# 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900,
# 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, ...

# ## Problem 1
#
# Implement a function nested_pairs() that yields all nested pairs
# with a specified degree. Each nested pair should be yielded exactly
# once. For example, nested_pairs(4) should yield the 5 nested pairs
# listed above. Use recursion. Test your function by counting the
# number of nested pairs yielded by it and comparing against the
# sequence of numbers given above.

    # NoteToSelf:  View as a bTree with () as a leaf
    #
    #         a full node is  *  (a node with two leafs) => ((), ())
    #                        /\
    #                       () ()
    #
    #         a half nnode is  *  (a node with a node and a leaf) => (*, ())
    #                         /\
    #                        *  ()
    #
    # The order is the number of leafs
    # Order 1 is just a leaf
    # To find all combinations we need to distribute theese nodes between
    # each branch 
    #  
    # For order n > 2
    # Here we need to create all trees that fit into (*,*)
    # where the number of leafs are n
    # For n = 4 => (1,3), (2,2), (3,1) => (1, (1,2)),   => (1, (1, (1, 1)))
    #                                     (1, (2,1)),   => (1, ((1, 1), 1))
    #                                     (1,1),(1,1)), => the same
    #                                     ((1,2),1),    => ((1, (1, 1)), 1)
    #                                     ((2,1),1)     => (((1,1), 1), 1)

def nested_pairs(n):
    """Yield all nested pairs with degree *n*."""

    if n == 1: yield "()" 
    if n > 1:
        for i in range(1,n):                 
            for nextvalue_left in nested_pairs(i): # new gen. of lesser order
                for nextvalue_right in nested_pairs(n-i): # new gen. 
                    yield "({}, {})".format(nextvalue_left, nextvalue_right)


# ## Problem 2
#
# Implement a function count_nested_pairs() that counts the number of
# nested pairs with a specified degree. A naive implementation of this
# function would call the nested_pairs() function from Problem 1. This
# is not what you are supposed to do! Instead, try to come up with a
# solution that counts the number of nested pairs without generating
# them. There is a way to solve this problem using a formula; but your
# solution should use recursion. Test your implementation by comparing
# your numbers to the numbers that you got above. What is the maximal
# degree for which you can compute the number of nested pairs in under
# one minute?

# NOTE the n == 2, 3 cuts some of the leafs and get more performance

def count_nested_pairs(n):
    """Count the number of nested pairs with degree *n*."""
    if n == 1: return 1   # Get order 18 in 51 seconds
    #if n == 2: return 1  # extra speed => get order 18 in 24 seconds
    #if n == 3: return 2  # more speed => get order 19 in 33 seconds
    if n > 1:
        c = 0
        for i in range(1,n):
            c = c + count_nested_pairs(i) * count_nested_pairs(n-i)       
        return c


# ## Problem 3
#
# Because it uses recursion, the function that you implemented in
# Problem 2 will call itself many times, and many times with the same
# argument. One way to speed things up is to cache the results of
# these calls. This strategy is called *memoization*.
#
# The idea is the following: All recursive calls of the function get
# access to a common cache in the form of a dictionary. Before a
# recursive call computes the number of nested pairs of a given degree
# *n*, it first checks whether that number is already stored in the
# cache. If yes, then the recursive call simply returns that
# value. Only if the value has not already been cached, the recursive
# call starts a computation on its own; but then it stores the result
# of that computation in the common cache, under the key *n*, so that
# subsequent calls will not have to recompute it.
#
# Write a function count_nested_pairs_memoized() that implements this
# idea. Test your implementation as above. How long does it take you to
# compute the number of nested pairs for the maximal degree that you
# could do in under one minute in Problem 2?

# NOTE Hm, I got this idea in task2 so....

memory = {1:1} 
def count_nested_pairs_memoized(n):
    """Count the number of nested pairs with degree *n*."""
    if not n in memory:
        c = 0
        for i in range(1,n):
            c = c + count_nested_pairs_memoized(i) * count_nested_pairs_memoized(n-i)       
        memory[n] = c
    return memory[n]


if __name__ == "__main__":
    import time
    from pprint import pprint
    tests = [1, 2, 3]  #Choose tests to run

    if 1 in tests:
        print("*** Test part 1 ***\n")
        print("Nested pairs:")
        order = 12
        for n in range(1, order+1):
            print("Trying order {}: ".format(n), end='')
            t0 = time.time()
            l = list()  
            for p in nested_pairs(n):
                if p in l: print("Duplicate!!")  #remove to increase performance
                l.append(p)
                if n<6 : print("\nRecieved: {}".format(p), end='') 
            t1 = time.time()
            total = t1 - t0
            #if n >= 6 : print("Suppressed output... (to many lines)")
            print(" Generated {} lines in {:6.3f} seconds.".format(len(l), total))
    if 2 in tests:
        print("\n*** Test part 2 ***\n")
        print("Count Nested pairs:")
        order = 18
        for n in range(10, order+1):
            print("Trying order {}:".format(n), end='')
            t0 = time.time()
            p = count_nested_pairs(n)           
            print("Counted: {}".format(p), end='') 
            t1 = time.time()
            total = t1 - t0
            print(" in {:6.3f} seconds.".format(total))
    if 3 in tests:
        print("\n*** Test part 3 ***\n")
        print("Memoized Count of Nested pairs:")
        order = 30
        for n in range(18, order+1):
            print("Trying order {}: ".format(n), end='')
            t0 = time.time()
            p = count_nested_pairs_memoized(n)           
            print("Counted: {}".format(p), end='')  
            t1 = time.time()
            total = t1 - t0
            print(" in {:10.8f} seconds.".format(total))
            #pprint(memory)
        
            