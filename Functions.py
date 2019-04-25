import numpy as np
import math
##These functions relate to the initiation of the code and mesh
##building.

def StaggeredSpatialMesh(N):
    #This function creates a pair of staggered mesh of [-1,1]
    #It takes the number of subpartitions and returns the 
    #two grids alongside with the mesh size dx.
    if N == int(N):
        dx = 2/N
        xplus = [-1+dx*i for i in range(N+1)]
        xminus = [-1+dx/2+dx*i for i in range(N)]
        return xplus,xminus,dx
    else:
        return "The input was not an integer"

def InitialE(xplus):
    #Provided a mesh this function returns the initial conditions
    #of the simulation as a numpy array
    return np.array([math.sin(math.pi*x) for x in xplus])
    
def InitialH(xminus):
    #Provided a mesh this function returns the initial conditions
    #of the simulation as a numpy array
    return np.array([math.cos(math.pi*x) for x in xminus])
    
def InitialP(xplus):
    #These are the initial conditions of the polarization of the
    #material
    return np.array([0 for x in xplus])

def InitialDerivP(xplus):
    #These are the initial conditions of the polarization of the
    #material
    return np.array([math.exp(x) for x in xplus])

def PCBC(x):
    #These are the boundary conditions of the electric field and     #polarization field
    return 0


