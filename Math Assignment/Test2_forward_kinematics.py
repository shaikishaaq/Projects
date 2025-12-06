import numpy as np

def forward_kinematics(j1, j2, j3, j4, L=1.0):
    """
    Computes 3D end-effector position for 4-DOF serial robot arm.
    Assumes standard DH convention: Rz-Tx for joint 1&4, Ry-Tx for joint 2, Rx-Tx for joint 3.
    Joint axes perpendicular as specified. [file:1]
    """
    # Joint 1: Rotation Z, Translate X
    c1, s1 = np.cos(j1), np.sin(j1)
    T1 = np.array([
        [c1, -s1, 0, L*c1],
        [s1,  c1, 0, L*s1],
        [0,    0, 1, 0   ],
        [0,    0, 0, 1   ]
    ])
    
    # Joint 2: Rotation Y, Translate X
    c2, s2 = np.cos(j2), np.sin(j2)
    T2 = np.array([
        [c2, 0, s2, L*c2],
        [0,  1, 0,  0   ],
        [-s2,0, c2, 0   ],
        [0,  0, 0,  1   ]
    ])
    
    # Joint 3: Rotation X, Translate X
    c3, s3 = np.cos(j3), np.sin(j3)
    T3 = np.array([
        [1,  0,   0,  L  ],
        [0,  c3, -s3, 0  ],
        [0,  s3,  c3, 0  ],
        [0,  0,   0,  1  ]
    ])
    
    # Joint 4: Rotation Z, Translate X
    c4, s4 = np.cos(j4), np.sin(j4)
    T4 = np.array([
        [c4, -s4, 0, L*c4],
        [s4,  c4, 0, L*s4],
        [0,    0, 1, 0   ],
        [0,    0, 0, 1   ]
    ])
    
    # Total transformation matrix
    T_total = T1 @ T2 @ T3 @ T4
    return T_total[:3, 3]  # End-effector position [x, y, z]

# Example usage and test (all joints at 0 rad)
if __name__ == "__main__":
    pos = forward_kinematics(0, 0, 0, 0)
    print(f"End-effector at zero angles: {pos}")  # Expected: [4. 0. 0.]

