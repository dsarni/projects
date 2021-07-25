#------------------------------------------------------------------------------
# Vector.py
#------------------------------------------------------------------------------
# Daniel Sarni
# dsarni@ucsc.edu
# Programming Assignment 8
"""
    This module provides functions to perform standard vector operations.  Vectors
    are represented as tuples of numbers (floats or ints).  Functions that take two 
    vector arguments will raise a ValueError() exception if the two vectors are of
    different dimensions.  
"""
#------------------------------------------------------------------------------
# import library modules
#------------------------------------------------------------------------------
import random
import math
#------------------------------------------------------------------------------
# function definitions
#------------------------------------------------------------------------------

# add() -----------------------------------------------------------------------
def add(u, v):
    """Return the vector sum u+v."""
    result = []
    if len(u) == len(v):
        for i in range (0, len(u)):
            result.append((u[i] + v[i]))
        return tuple(result)
    else:
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
# end add() -------------------------------------------------------------------


# negate() --------------------------------------------------------------------
def negate(u):
    """Return the negative of the vector u."""
    result = []
    for i in range(0, len(u)):
        result.append(u[i] * -1)
    return tuple(result)
    
# end negate() ----------------------------------------------------------------   


# sub() -----------------------------------------------------------------------
def sub(u, v):
    """Return the vector difference u-v."""
    result = []
    if len(u) == len(v):
        for i in range(0, len(u)):
            result.append((u[i] - v[i]))
        return tuple(result)
    else:
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))

# end sub() -------------------------------------------------------------------


# scalarMult() ----------------------------------------------------------------
def scalarMult(c, u):
    """Return the scalar product cu of the number c by the vector u."""
    result = []
    for i in range (0, len(u)):
        result.append(c*(u[i]))
    return tuple(result)

# end scalarMult() ------------------------------------------------------------


# hadamard() ------------------------------------------------------------------
def hadamard(u, v):
    """ Return the Hadamard product of u with v."""
    result = []
    if len(u) == len(v):
        for i in range(0, len(u)):
            result.append(u[i] * v[i])
        return tuple(result)
    else:
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
# end hadamard() --------------------------------------------------------------


# dot() -----------------------------------------------------------------------
def dot(u, v):
    """Return the dot product of u with v."""
    result = []
    result2 = []
    if len(u) == len(v):
        for i in range(0, len(u)):
            result.append(u[i] * v[i])
        result2.append(sum(result))
        for i in range(0, len(u)):
            return (result2[i])
    else:
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
# end dot() -------------------------------------------------------------------


# length() --------------------------------------------------------------------
def length(u):
    """Returns the (geometric) length of a vector"""
    for i in range(0, len(u)):
        gLength = dot(u, u)**(1/2)
    return gLength
# end length() ----------------------------------------------------------------


# dim() -----------------------------------------------------------------------
def dim(u):
    """Return the dimension of the vector u."""
    for i in range(0, len(u)):
        len(u)
    return len(u)
# end dim() -------------------------------------------------------------------


# unit() ----------------------------------------------------------------------
def unit(v):  
    """Return a unit (geometric length 1) vector in the direction of v."""  
    result2 = []
    for i in range(0, len(v)):
        gLength = dot(v, v)**(1/2)
    for i in range(0, len(v)):
        if gLength > 1:
            result2.append((1/gLength) * v[i])
        elif gLength <= 1:
            result2.append((gLength/1) * v[i])
    return tuple(result2)
# end unit() ------------------------------------------------------------------

#angle() ----------------------------------------------------------------------
def angle(u, v):
    """Return the angle (in radians) between vectors u and v."""
    if len(u) != len(v):
        raise ValueError('incompatible vectors: '+str(u)+', '+str(v))
    Angle = math.acos(dot(unit(u), unit(v)))
    return Angle
        
# end angle() -----------------------------------------------------------------


# randVector() ----------------------------------------------------------------
def randVector(n, a, b):
    """Return a vector of dimension n whose components are random floats in
 the range [a, b). """
    rand = random.uniform(a, b)
    rand2 = random.uniform(a, b)
    return (rand,rand2)
# end randomVector() ----------------------------------------------------------


