# TDP015 Programming Assignment 1
# Logic
# Skeleton Code

import itertools
from pprint import pprint


class Exp(object):
    """A Boolean expression.

    A Boolean expression is represented in terms of a *reserved symbol* (a
    string) and a list of *subexpressions* (instances of the class `Exp`).
    The reserved symbol is a unique name for the specific type of
    expression that an instance of the class represents. For example, the
    constant `True` uses the reserved symbol `1`, and logical and uses `∧`
    (the Unicode symbol for conjunction). The reserved symbol for a
    variable is its name, such as `x` or `y`.

    Attributes:
        sym: The reserved symbol of the expression (a string).
        sexps: The list of subexpressions (instances of the class `Exp`).
    """

    def __init__(self, sym, *sexps):
        """Constructs a new expression.

        Args:
            sym: The reserved symbol for this expression.
            sexps: The list of subexpressions.
        """
        self.sym = sym
        self.sexps = sexps

    def value(self, assignment):
        """Returns the value of this expression under the specified truth
        assignment.

        Args:
            assignment: A truth assignment, represented as a dictionary
            that maps variable names to truth values.

        Returns:
            The value of this expression under the specified truth
            assignment: either `True` or `False`.
        """
        raise ValueError()

    def variables(self):
        """Returns the (names of the) variables in this expression.

        Returns:
           The names of the variables in this expression, as a set.
        """
        variables = set()
        for sexp in self.sexps:
            variables |= sexp.variables()
        return variables


class Var(Exp):
    """A variable."""

    def __init__(self, sym):
        super().__init__(sym)

    def value(self, assignment):
        assert len(self.sexps) == 0
        return assignment[self.sym]

    def variables(self):
        assert len(self.sexps) == 0
        return {self.sym}


class Nega(Exp):
    """Logical not."""

    # TODO: Complete this class
    def __init__(self, sexp1):
        super().__init__('-', sexp1)

    def value(self, assignment):
        assert len(self.sexps) == 1
        return not self.sexps[0].value(assignment)


class Conj(Exp):
    """Logical and."""

    def __init__(self, sexp1, sexp2):
        super().__init__('∧', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2
        return \
            self.sexps[0].value(assignment) and \
            self.sexps[1].value(assignment)


class Disj(Exp):
    """Logical or."""

    # TODO: Complete this class
    def __init__(self, sexp1, sexp2):
        super().__init__('or', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2
        return \
            self.sexps[0].value(assignment) or \
            self.sexps[1].value(assignment)
    # END TODO


class Impl(Exp):
    """Logical implication."""

    # TODO: Complete this class
    def __init__(self, sexp1, sexp2):
        super().__init__('→', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2
        return \
            not(self.sexps[0].value(assignment) and not \
                self.sexps[1].value(assignment))
        # Alternative (de morgans)
        # return \ 
        #   not self.sexps[0].value(assignment) or \
        #   self.sexps[1].value(assignment)
    # END TODO


class Equi(Exp):
    """Logical equivalence."""

    # TODO: Complete this class
    def __init__(self, sexp1, sexp2):
        super().__init__('↔', sexp1, sexp2)
    def value(self, assignment):
        assert len(self.sexps) == 2
        a = self.sexps[0].value(assignment)
        b = self.sexps[1].value(assignment)
        #return not(not(not a and not b) and not(a and b))
        # Alternative
        return a == b

def assignments(variables):
    """Yields all truth assignments to the specified variables.

    Args:
        variables: A set of variable names.

    Yields:
        All truth assignments to the specified variables. A truth
        assignment is represented as a dictionary mapping variable names to
        truth values. Example:

        {'x': True, 'y': False}
    """
    # TODO: Complete this function. Use the itertools module!
    logic = {True, False}
    AssignmentsList = list()
    for assignment in itertools.product(logic, repeat=len(variables)):
        assignment = dict(zip(variables, assignment))
        AssignmentsList.append(assignment)
    return AssignmentsList


def satisfiable(exp):
    """Tests whether the specified expression is satisfiable.

    An expression is satisfiable if there is a truth assignment to its
    variables that makes the expression evaluate to true.

    Args:
        exp: A Boolean expression.

    Returns:
        A truth assignment that makes the specified expression evaluate to
        true, or False in case there does not exist such an assignment.
        A truth assignment is represented as a dictionary mapping variable
        names to truth values.
    """
    # TODO: Complete this function
    a = assignments(exp.variables())
    for item in a:
        if(VerboseMode): print('   Verbose: ' + str(item) + ' ' + str(exp.value(item)))
        if(exp.value(item)):
            return item
    return False

def tautology(exp):
    """Tests whether the specified expression is a tautology.

    An expression is a tautology if it evaluates to true under all
    truth assignments to its variables.

    Args:
        exp: A Boolean expression.

    Returns:
        True if the specified expression is a tautology, False otherwise.
    """
    # TODO: Complete this function
    a = assignments(exp.variables())
    for item in a:
        if(VerboseMode): print('   Verbose: ' + str(item) + ' ' + str(exp.value(item)))
        if (not exp.value(item)):
            return False
    return True


def equivalent(exp1, exp2):
    """Tests whether the specified expressions are equivalent.

    Two expressions are equivalent if they have the same truth value under
    each truth assignment.

    Args:
        exp1: A Boolean expression.
        exp2: A Boolean expression.

    Returns:
        True if the specified expressions are equivalent, False otherwise.
    """
    # TODO: Complete this function
    v = exp1.variables()
    v2 = exp2.variables()
    if(v2!=v): 
        return False
    a = assignments(v)
    for item in a:
        if(VerboseMode): print('   Verbose: ' + str(item) + ' ' + str(exp1.value(item)) + ' ' + str(exp2.value(item)))
        if( exp1.value(item) != exp2.value(item)):
            return False
    return True
    # END TODO


def test1():
    a = Var('a')
    b = Var('b')
    c = Var('c')
    exp1 = Impl(Impl(a, b), c)
    exp2 = Conj(Disj(a, c), Disj(Nega(b), c))
    return equivalent(exp1, exp2)


def testNega():
    a = Var('a')
    exp1 = Nega(a)
    s = 'Exp1: - True = ' + str(exp1.value({'a': True})) + '\n'
    s += 'Exp1: - False = ' + str(exp1.value({'a': False})) + '\n'

    return s

def testConj():
    a = Var('a')
    b = Var('b')
    exp1 = Conj(a, b)
    s = 'Exp1: False and False = ' + str(exp1.value({'a': False, 'b': False})) + '\n'
    s += 'Exp1: True and True = ' + str(exp1.value({'a': True, 'b': True})) + '\n' 
    s += 'Exp1: True and False = ' + str(exp1.value({'a': True, 'b': False})) + '\n' 
    return s

def testDisj():
    a = Var('a')
    b = Var('b')
    exp1 = Disj(a, b)
    s = 'Exp1: False or False = ' + str(exp1.value({'a': False, 'b': False})) + '\n'
    s += 'Exp1: True or True = ' + str(exp1.value({'a': True, 'b': True})) + '\n' 
    s += 'Exp1: True or False = ' + str(exp1.value({'a': True, 'b': False})) + '\n' 
    return s

def testImpl():
    a = Var('a')
    b = Var('b')
    exp1 = Impl(a, b)
    s = 'Exp1: False , False -> ' + str(exp1.value({'a': False, 'b': False})) + '\n'
    s += 'Exp1: False , True -> ' + str(exp1.value({'a': False, 'b': True})) + '\n' 
    s += 'Exp1: True , False -> ' + str(exp1.value({'a': True, 'b': False})) + '\n' 
    s += 'Exp1: True , True -> ' + str(exp1.value({'a': True, 'b': True})) + '\n' 
    return s

def testEqui():
    a = Var('a')
    b = Var('b')
    exp1 = Equi(a, b)
    s = 'Exp1: False , False -> ' + str(exp1.value({'a': False, 'b': False})) + '\n'
    s += 'Exp1: False , True -> ' + str(exp1.value({'a': False, 'b': True})) + '\n' 
    s += 'Exp1: True , False -> ' + str(exp1.value({'a': True, 'b': False})) + '\n' 
    s += 'Exp1: True , True -> ' + str(exp1.value({'a': True, 'b': True})) + '\n' 
    return s

def testAssi():
    a = Var('a')
    b = Var('b')
    c = Var('c')
    exp1 = Conj(Disj(a,b), c)
    s = assignments(exp1.variables())
    return s

def testSati():
    a = Var('a')
    b = Var('b')
    exp1 = Disj(a,b)
    sat = satisfiable(exp1)
    s = 'Exp1 (a v -a): ' + str(sat) + ' -> '
    if(sat != False):
        s += str(exp1.value(sat)) + '\n'
    else:
        s += 'FALSE' + '\n'

    exp2 = Conj(a,Nega(a))
    sat = satisfiable(exp2)

    s += 'Exp1 (a v -a): ' + str(sat) + ' -> '
    if(sat != False):
        s += str(exp2.value(sat)) + '\n'
    else:
        s += 'FALSE' + '\n'
    return s

def testTaut():
    a = Var('a')
    exp1 = a
    tau = tautology(exp1)
    s = 'Exp1 (a) : ' + str(tau) + '\n' 

    b = Var('b')
    exp2 = Disj(b, Nega(b))
    tau = tautology(exp2)
    s += 'Exp2 (b v -b) : ' + str(tau) + '\n' 

    p = Var('p')
    q = Var('q')
    exp3 = Impl(Conj(p, Impl(p,q)),q)
    tau = tautology(exp3)
    s += 'Exp3 ( (p ∧ (p -> q)) -> q ) : ' + str(tau) + '\n'
    return s

def testEquivalent():
    a = Var('a')
    exp1 = a
    equ = equivalent(exp1, exp1)
    s = 'Exp1 (a), Exp2 (a): ' + str(equ) + '\n'
     
    b = Var('b')
    exp2 = b
    equ = equivalent(exp1, exp2)
    s+= 'Exp1 (a), Exp2 (b): ' + str(equ) + '\n'

    exp3 = Conj(a, b)
    exp4 = Nega (Disj(Nega(a), Nega(b))) # deMorgan
    equ = equivalent(exp3, exp4)
    s+= 'Exp1 (a ∧ b), Exp2 (-(-a v -b)): ' + str(equ) + '\n'
    exp5 = Disj(a,b)
    equ = equivalent(exp3, exp5)
    s+= 'Exp1 (a ∧ b), Exp2 (a v b): ' + str(equ) + '\n'
    return s


if __name__ == "__main__":
    VerboseMode = True
    print("Test 1")
    print(test1())
    # TODO: Add some more test cases

    print("Test Nega:")
    print(testNega())
    print("Test Conj:")
    print(testConj())
    print("Test Disj:")
    print(testDisj())
    print("Test Impl:")
    print(testImpl())
    print("Test Equi:")
    print(testEqui())
    print("Test Assignment:")
    pprint(testAssi())    # Using prettyprint
    print('')
    print("Test Sati:")
    print(testSati())
    print("Test Tautology:")
    print(testTaut())  
    print("Test Equivalent:")
    print(testEquivalent())   
