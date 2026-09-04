#  Camera-to-Base Frame Transformation

## Overview
This script performs a 3D spatial transformation to convert target marker coordinates detected by a vehicle's front camera (`camera_link`) into coordinates relative to the vehicle's center frame (`base_link`).

## Setup & Parameters
The script applies a rotation around the Y-axis (camera pitch tilt angle) followed by translation offsets:

- **Obstacle Points (Camera Frame):**
  - Point 1: `[2.0, 0.0, -0.2]`
  - Point 2: `[3.5, 1.0, -0.3]`
  - Point 3: `[1.5, -0.8, -0.1]`
- **Translation Offsets:** `tx = 0.5`, `ty = 0.0`, `tz = 0.2` (meters)
- **Pitch Rotation Angle ($\theta$):** `-15°`

## Execution
Run the Python script using:
```bash
python3 camera_transform.py
