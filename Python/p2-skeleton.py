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
## (((),()), ((),()))  <= More than 3 empty tuples, ergo wrong
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


def nested_pairs(n):
    dbg = False
    """Yield all nested pairs with degree *n*."""

    # NoteToSelf:  View as a bTree with () as a leaf
    #
    #               a full node is  *  (a node with two leafs) => ((), ())
    #                              /\
    #                            () ()
    #
    #               a half nnode is  *  (a node with a node and a leaf) => (*, ())
    #                               /\
    #                              *  ()
    #
    # The order is the number of leafs
    # Order 1 is just a leaf
    # To find all combinations we need to distribute theese nodes between each branch 
    #  
    if dbg: print("Starting to run a np generator. n={}\n".format(n))
    if n > 2:
      
        for i in range(1,n):     # NoteToSelf: n not included in range 
            #print("i = {}".format(i))
            np_left = nested_pairs(i) # create new generator
            np_right = nested_pairs(n-i) # create new generator
            print("doing {} / {}".format(i, n-i))
            for nextvalue_left in np_left:
                if dbg: print("Left hand {}".format(nextvalue_left))
                for nextvalue_right in np_right:
                    if dbg: print("Right hand {}".format(nextvalue_right))
                    s = "({}, {})".format(nextvalue_left, nextvalue_right)
                    if dbg: print("TOTAL: {}\n".format(s))
                    try:
                        yield s
                    except GeneratorExit:
                        print("Exiting")
                        return
                if dbg: print("No more right values...(left={}".format(nextvalue_left))
            if dbg: print("No more left values...")
            
    if n == 2:
        try:
            s = "((), ())"
            if dbg: print("From np (n={}) returning: {}\n".format(n,s))
            yield s
        except GeneratorExit:
            if dbg: print("Exiting n==2")
            return
    if n == 1:
        try:
            s = "()" 
            print("From np (n={}): {}\n".format(n, s))
            yield s
        except GeneratorExit:
            print("Exiting n==1")
            return


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


def count_nested_pairs(n):
    """Count the number of nested pairs with degree *n*."""
    # TODO: Replace the following line with your own code.
    return 0


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


def count_nested_pairs_memoized(n):
    # TODO: Replace the following line with your own code.
    return 0

if __name__ == "__main__":
    n = 1
    print("Nested pairs:")
    while n<5:
        print("*********************************************Trying order {}:\n".format(n))
        for p in nested_pairs(n):
            print("======================Recieving: {}".format(p))
        n += 1
