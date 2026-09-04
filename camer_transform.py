import math

points = [
    [2.0, 0.0, -0.2],
    [3.5, 1.0, -0.3],
    [1.5, -0.8, -0.1]
]

tx, ty, tz = 0.5, 0.0, 0.2
theta_deg = -15
theta_rad = math.radians(theta_deg)

transformed_points = []

for point in points:
    xc, yc, zc = point
    
    xb = xc * math.cos(theta_rad) + zc * math.sin(theta_rad) + tx
    yb = yc + ty
    zb = -xc * math.sin(theta_rad) + zc * math.cos(theta_rad) + tz
    
    transformed_points.append([round(xb, 2), round(yb, 2), round(zb, 2)])

print("--- Transformed Obstacles (Base Frame) ---")
for i, pt in enumerate(transformed_points, 1):
    print(f"Obstacle {i}: {pt}")