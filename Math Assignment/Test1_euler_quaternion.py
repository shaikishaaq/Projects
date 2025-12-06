import numpy as np

def euler_to_quaternion(roll, pitch, yaw):
    """
    Convert Euler angles (radians: roll=X, pitch=Y, yaw=Z) to quaternion [w, x, y, z].
    Uses intrinsic XYZ convention (aerospace standard). Robust for all angles.
    """
    cr, sr = np.cos(roll/2), np.sin(roll/2)
    cp, sp = np.cos(pitch/2), np.sin(pitch/2)
    cy, sy = np.cos(yaw/2), np.sin(yaw/2)
    
    w = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy
    
    return np.array([w, x, y, z])

def quaternion_to_euler(q):
    """
    Convert quaternion [w, x, y, z] to Euler angles (radians: roll, pitch, yaw).
    Handles gimbal lock (pitch=±π/2) explicitly using arcsin clamping.
    """
    w, x, y, z = q
    
    # Roll (X-axis)
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x**2 + y**2)
    roll = np.arctan2(sinr_cosp, cosr_cosp)
    
    # Pitch (Y-axis) - gimbal lock handling
    sinp = 2 * (w * y - z * x)
    if abs(sinp) >= 1.0:
        pitch = np.sign(sinp) * np.pi / 2
    else:
        pitch = np.arcsin(sinp)
    
    # Yaw (Z-axis)
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y**2 + z**2)
    yaw = np.arctan2(siny_cosp, cosy_cosp)
    
    return np.array([roll, pitch, yaw])

# Test suite with edge cases (gimbal lock included)
if __name__ == "__main__":
    tests = [
        (0, 0, 0),                           # Zero angles
        (np.pi/2, 0, 0),                     # Roll 90°
        (0, np.pi/2, 0),                     # Pitch 90° (gimbal lock)
        (0, 0, np.pi/2),                     # Yaw 90°
        (np.pi/4, np.pi/3, -np.pi/6)         # Arbitrary angles
    ]
    
    print("Euler ↔ Quaternion Conversion Tests")
    print("-" * 50)
    for i, (roll, pitch, yaw) in enumerate(tests, 1):
        quat = euler_to_quaternion(roll, pitch, yaw)
        euler_recovered = quaternion_to_euler(quat)
        error = np.linalg.norm(euler_recovered - np.array([roll, pitch, yaw]))
        print(f"Test {i}: Euler=[{roll:.3f},{pitch:.3f},{yaw:.3f}] → Quat={quat[:.3f]}")
        print(f"  Recovered: {euler_recovered[:.3f]}, Error: {error:.2e}")

