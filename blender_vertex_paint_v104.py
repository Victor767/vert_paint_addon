# #########################################################
# Buttons in Object Data Properties Tab
#
# Description:
# Adds buttons to Object Data Properties Tab
# 
#
# Author: Viktor Andryeyenkov
# 
# #########################################################

bl_info = {
    "name" : "Verticies Color Manipulation Buttons",
    "author" : "Viktor Andryeyenkov",
    "description" : "Adds buttons",
    "blender" : (3, 00, 0),
    "version" : (1, 0, 4),
    "location" : "Object Data Properties > Vertex Color Manipulation",
    "warning" : "",
    "category" : "Vertex Color",
    "wiki_url": ""
}

import bpy

class SimpleOperator1(bpy.types.Operator):    
    """Paint all verticies of all selected objects in black color"""
    bl_idname = "object.paint_vert_black"
    bl_label = "Paint Object Verticies Black"

    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'SOLID'
                        space.shading.color_type = 'VERTEX'

        for obj in context.selected_objects:
            if obj.type == 'MESH':
                bpy.ops.object.mode_set(mode='OBJECT')
                
                mesh = obj.data
                
                if not mesh.vertex_colors:
                    mesh.vertex_colors.new()
                
                vertex_colors = mesh.vertex_colors.active
                
                for poly in mesh.polygons:
                    for loop_index in poly.loop_indices:
                        vertex_colors.data[loop_index].color = (0, 0, 0, 1)  # Set color to black

                mesh.update()
                
        self.report({'INFO'}, "Object(s) verticies painted black.")

        return {'FINISHED'}



class SimpleOperator2(bpy.types.Operator):    
    """Paint all verticies of all selected objects in white color"""
    bl_idname = "object.paint_vert_white"
    bl_label = "Paint Object Verticies White"

    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'SOLID'
                        space.shading.color_type = 'VERTEX'

        for obj in context.selected_objects:
            if obj.type == 'MESH':
                bpy.ops.object.mode_set(mode='OBJECT')
                
                mesh = obj.data
                
                if not mesh.vertex_colors:
                    mesh.vertex_colors.new()
                
                vertex_colors = mesh.vertex_colors.active
                
                for poly in mesh.polygons:
                    for loop_index in poly.loop_indices:
                        vertex_colors.data[loop_index].color = (255, 255, 255, 1)  # Set color to white

                mesh.update()
                
        self.report({'INFO'}, "Object(s) verticies painted white.")

        return {'FINISHED'}



class SimpleOperator3(bpy.types.Operator):    
    """Paint all verticies of all selected objects in red color"""
    bl_idname = "object.paint_vert_red"
    bl_label = "Paint Object Verticies Red"

    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'SOLID'
                        space.shading.color_type = 'VERTEX'

        for obj in context.selected_objects:
            if obj.type == 'MESH':
                bpy.ops.object.mode_set(mode='OBJECT')
                
                mesh = obj.data
                
                if not mesh.vertex_colors:
                    mesh.vertex_colors.new()
                
                vertex_colors = mesh.vertex_colors.active
                
                for poly in mesh.polygons:
                    for loop_index in poly.loop_indices:
                        vertex_colors.data[loop_index].color = (255, 0, 0, 1)  # Set color to red

                mesh.update()
                
        self.report({'INFO'}, "Object(s) verticies painted red.")

        return {'FINISHED'}






class SimpleOperator4(bpy.types.Operator):    
    """Paint all selected verticies of all selected objects in black color"""
    bl_idname = "object.paint_vert_black_2"
    bl_label = "Paint Selected Verticies Black"

    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'SOLID'
                        space.shading.color_type = 'VERTEX'
                        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                mesh = obj.data
                
                if not mesh.vertex_colors:
                    mesh.vertex_colors.new()
                vertex_colors = mesh.vertex_colors.active

                if vertex_colors:
                    for vert in mesh.vertices:
                        if vert.select:
                            vert_index = vert.index
                
                            for poly in mesh.polygons:
                                if vert_index in poly.vertices:
                                    for loop_index in poly.loop_indices:
                                        loop = mesh.loops[loop_index]
                                        if loop.vertex_index == vert_index:
                                            vertex_colors.data[loop_index].color = (0, 0, 0, 1)
        selected_objects = bpy.context.selected_objects

        bpy.context.view_layer.update()
        
        bpy.ops.object.mode_set(mode='EDIT')
        
        self.report({'INFO'}, "Selected verticies painted black.")
        
        return {'FINISHED'}




class SimpleOperator5(bpy.types.Operator):    
    """Paint all selected verticies of all selected objects in white color"""
    bl_idname = "object.paint_vert_white_2"
    bl_label = "Paint Selected Verticies White"

    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'SOLID'
                        space.shading.color_type = 'VERTEX'
                        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                mesh = obj.data
                
                if not mesh.vertex_colors:
                    mesh.vertex_colors.new()
                vertex_colors = mesh.vertex_colors.active

                if vertex_colors:
                    for vert in mesh.vertices:
                        if vert.select:
                            vert_index = vert.index
                
                            for poly in mesh.polygons:
                                if vert_index in poly.vertices:
                                    for loop_index in poly.loop_indices:
                                        loop = mesh.loops[loop_index]
                                        if loop.vertex_index == vert_index:
                                            vertex_colors.data[loop_index].color = (255, 255, 255, 1)
        selected_objects = bpy.context.selected_objects

        bpy.context.view_layer.update()
        
        bpy.ops.object.mode_set(mode='EDIT')
        
        self.report({'INFO'}, "Selected verticies painted white.")
        
        return {'FINISHED'}



class SimpleOperator6(bpy.types.Operator):    
    """Paint all selected verticies of all selected objects in red color"""
    bl_idname = "object.paint_vert_red_2"
    bl_label = "Paint Selected Verticies Red"

    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'SOLID'
                        space.shading.color_type = 'VERTEX'
                        
        bpy.ops.object.mode_set(mode='OBJECT')
        
        for obj in bpy.context.selected_objects:
            if obj.type == 'MESH':
                mesh = obj.data
                
                if not mesh.vertex_colors:
                    mesh.vertex_colors.new()
                vertex_colors = mesh.vertex_colors.active

                if vertex_colors:
                    for vert in mesh.vertices:
                        if vert.select:
                            vert_index = vert.index
                
                            for poly in mesh.polygons:
                                if vert_index in poly.vertices:
                                    for loop_index in poly.loop_indices:
                                        loop = mesh.loops[loop_index]
                                        if loop.vertex_index == vert_index:
                                            vertex_colors.data[loop_index].color = (255, 0, 0, 1)
        selected_objects = bpy.context.selected_objects

        bpy.context.view_layer.update()
        
        bpy.ops.object.mode_set(mode='EDIT')
        
        self.report({'INFO'}, "Selected verticies painted red.")
        
        return {'FINISHED'}




class SimpleOperator7(bpy.types.Operator):
    """Remove any Color Attributes available in selected objects"""
    bl_idname = "object.del_vrt_color"
    bl_label = "Remove any Verticies Color from Object"

    def execute(self, context):
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.shading.type = 'SOLID'
                        space.shading.color_type = 'VERTEX'

        for obj in context.selected_objects:
            if obj.type == 'MESH' and obj.data.color_attributes:
                for attr in reversed(obj.data.color_attributes):
                    obj.data.color_attributes.remove(attr)
        self.report({'INFO'}, "Color attributes removed from selected objects.")
        
        return {'FINISHED'}



class SimplePanel(bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_label = "Vertex Color Manipulation"
    bl_idname = "VERT_COLOR"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    def draw(self, context):
        layout = self.layout
        layout.operator(SimpleOperator1.bl_idname)
        layout.operator(SimpleOperator2.bl_idname)
        layout.operator(SimpleOperator3.bl_idname)
        layout.operator(SimpleOperator4.bl_idname)
        layout.operator(SimpleOperator5.bl_idname)
        layout.operator(SimpleOperator6.bl_idname)
        layout.operator(SimpleOperator7.bl_idname)

def register():
    bpy.utils.register_class(SimpleOperator1)
    bpy.utils.register_class(SimpleOperator2)
    bpy.utils.register_class(SimpleOperator3)
    bpy.utils.register_class(SimpleOperator4)
    bpy.utils.register_class(SimpleOperator5)
    bpy.utils.register_class(SimpleOperator6)
    bpy.utils.register_class(SimpleOperator7)
    bpy.utils.register_class(SimplePanel)

def unregister():
    bpy.utils.unregister_class(SimpleOperator1)
    bpy.utils.unregister_class(SimpleOperator2)
    bpy.utils.unregister_class(SimpleOperator3)
    bpy.utils.unregister_class(SimpleOperator4)
    bpy.utils.unregister_class(SimpleOperator5)
    bpy.utils.unregister_class(SimpleOperator6)
    bpy.utils.unregister_class(SimpleOperator7)
    bpy.utils.unregister_class(SimplePanel)

if __name__ == "__main__":
    register()