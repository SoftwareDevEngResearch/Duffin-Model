from Functions import StaggeredSpatialMesh, InitialE, InitialH, InitialDerivP
import numpy as np

def test_StaggeredSpatialMeshInternal():
    #Here we will test that the meshing function can divide the interval [-1,1] 
    #into five pieces. 
    N = 5
    xplus, xminus, dx = StaggeredSpatialMesh(N)    
    txplus = np.array([-1, -0.6, -0.2, 0.2, 0.6, 1])
    txminus = np.array([-0.8, -0.4, 0, 0.4, 0.8])
    assert np.linalg.norm(txplus-xplus) < 1e-3
    assert np.linalg.norm(txminus-xminus) < 1e-3
test_StaggeredSpatialMeshInternal()

def test_StaggeredSpatialMeshBoundary():
    #Here we make sure that if the input to the spatial mesh is not an integer 
    #the output should be an error message.
    N = 2.5
    x = StaggeredSpatialMesh(N)
    assert x == "The input was not an integer"
test_StaggeredSpatialMeshBoundary()

def test_InitialEInternal():
    #The initial conditions on the electric field are two periods of a sine wave
    #Here we check that it correctly computes some well known internal points
    #namely, sin( -pi/2) sin(0) sin(pi/2)
    N = 4
    xplus, xminus, dx = StaggeredSpatialMesh(N)
    EInit = InitialE(xplus)
    assert abs(EInit[1]+1) < 1e-3
    assert abs(EInit[2]) < 1e-3
    assert abs(EInit[3]-1) <1e-3
test_InitialEInternal()

def test_InitialEBoundary():
    #The initial conditions on the electric field are two periods of a sine wave
    #Here we check that it correctly computes some well known boundary points
    #namely, sin(-pi) sin(pi) 
    N = 4
    xplus, xminus, dx = StaggeredSpatialMesh(N)
    EInit = InitialE(xplus)
    assert abs(EInit[0]) < 1e-3
    assert abs(EInit[4]) < 1e-3
test_InitialEBoundary()


