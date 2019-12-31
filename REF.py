# -*- coding: utf-8 -*-
import numpy as np
from scipy import sparse

def main():
    size_M = int(input("# of rows"))
                   
    size_N = int(input("# of columns"))
                  
    mat = np.eye(size_M, M=size_N)
    print(mat)
    
if __name__ == '__main__':
    main()