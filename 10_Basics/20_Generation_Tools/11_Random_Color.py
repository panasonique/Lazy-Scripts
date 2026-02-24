info = {
    "name": "Random Colors",
    "type": "button",
    "icon": "COLOR",
    "description": "Назначает случайный цвет всем выделенным объектам"
}

import bpy
import random

def run():
    # Проходим по всем выделенным объектам
    for obj in context.selected_objects:
        if obj.type == 'MESH':
            # Создаем или берем существующий материал
            mat = bpy.data.materials.new(name="RandomMat")
            mat.use_nodes = True
            
            # Находим ноду Principled BSDF
            nodes = mat.node_tree.nodes
            bsdf = nodes.get("Principled BSDF")
            
            if bsdf:
                # Генерируем случайный цвет (RGBA)
                color = (random.random(), random.random(), random.random(), 1.0)
                bsdf.inputs[0].default_value = color
                
            # Назначаем материал объекту
            if obj.data.materials:
                obj.data.materials[0] = mat
            else:
                obj.data.materials.append(mat)

    report({'INFO'}, f"Цвета обновлены для {len(context.selected_objects)} объектов")

run()
