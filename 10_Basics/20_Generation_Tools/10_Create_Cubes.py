info = {"name": "Generate Cubes", "type": "button", "icon": "MESH_CUBE"}
import bpy
import random
for i in range(5):
    bpy.ops.mesh.primitive_cube_add(location=(random.uniform(-5, 5), random.uniform(-5, 5), 0))
