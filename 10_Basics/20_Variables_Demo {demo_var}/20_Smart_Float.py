info = {
    "name": "Smart Float",
    "type": "input_custom",
    "prop_id": "demo_var",  # Этот ID должен быть в названии папки {demo_var}
    "default": 4.0,
    "min": 0.0,
    "max": 10.0,
    "icon": "SETTINGS",
    "description": "Меняет масштаб выделенных объектов. Округляется если > 1.0"
}

import bpy

# Доступ к значению через props (автоматически проброшено аддоном)
prop_item = context.scene.my_addon_vars.get(info['prop_id'])

def run():
    # Пример использования переменной: меняем масштаб объектов
    for obj in context.selected_objects:
        obj.scale = (val, val, val)
    
    # Выводим текущее значение в консоль для проверки
    print(f"Lazy Scripts Demo: Текущий масштаб установлен в {val:.2f}")

# Вызываем функцию при каждом изменении ползунка
run()
