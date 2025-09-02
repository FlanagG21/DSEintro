#Author: Galen Flanagan
#Fun Fact: A photo of mine is a famous internet meme template.
import pytest
from Kronecker import kroneckerProduct

def testKronecker():
    u = [[0,1]]
    v =[[1,0]]
    s = [[1,1],[1,0]]
    t = [[0,1],[1,0]]
    assert kroneckerProduct(u,v) == [[0,0,1,0]]
    assert kroneckerProduct(s,t) == [[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]]