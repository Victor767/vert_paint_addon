# Verticies Color paint addon

It is often needed to paint verticies of the objects in different colors before exporting to engine as engines shaders require it to be painted in one way or another to function properly. This addon allows to paint verticies in any color on the fly right from Object or Edit Mode in Blender without switching to Vertex Paint Mode. The two most used colors - Black and White - are applied with a single press of a button. Any other color could be picked up from color wheel by also pressing a single button.

Unlike painting verticies in different colors in Vertex Paint Mode this plugin allows you to paint any number of vertices on any number of objects in a single instance.

This addon adds buttons to the separate panel in Object Data Properties tab of Blender with the following functions:

1. Paint Object Verticies Black - paints all the verticies of selected object(s) in black color. This means literally all verticies of selected object(s) shall be painted white despite what color thay had earlier. If you need to paint only certain verticies of your object select them in Edit Mode and use buttons 4-6.
2. Paint Object Verticies White - paints all the verticies of selected object(s) in white color. This means literally all verticies of selected object(s) shall be painted white despite what color thay had earlier. If you need to paint only certain verticies of your object select them in Edit Mode and use buttons 4-6.
3. Color Picker for selected Objects - Shows the Color Picker dialog window to choose color by either picking it on a color wheel, sliding RGB/HSV values, entering exact RGB value or entering exact HSV value and applies it to all verticies on all selected objects. If you need to paint only certain verticies of your object select them in Edit Mode and use buttons 4-6.
4. Paint Selected Verticies Black - when in Edit Mode paints all selected verticies in black color leaving all non-selected verticies intact. If you press this button in Object Mode it will paint black all verticies that were left selected in Edit Mode.
5. Paint Selected Verticies White - when in Edit Mode paints all selected verticies in white color leaving all non-selected verticies intact. If you press this button in Object Mode it will paint white all verticies that were left selected in Edit Mode.
6. Color Picker for selected Verticies - shows the Color Picker dialog window to choose color by either picking it on a color wheel, sliding RGB/HSV values, entering exact RGB value or entering exact HSV value and applies it to all selected verticies of all the selected objects.
7. Remove any Verticies Color from Object - removes any Color Attribute data from geometry. It is Color Attribute data which holds any kind of information on the verticies color so by removing it we make sure that the geometry is clean of information about vertex color if we don't need it.

It is handy to use it as when any button is pressed it not only paints the verticies but also changes the Viewport Shading Mode to Solid and Color Type to Attribute even before painting so the result of verticies painting is visible without necessity to change anything in 3D Viewport. When finished painting verticies you can then change the Shading mode and Color type (if in Solid mode) to whatever you got used to.

Addon is always informs you on the Status bar if the operations is performed successfully.

When addon is installed it adds panel to Object Data Properties tab on the bottom of the stack. It makes sense to keep this panel right beneath Color Attributes panel so you can drag it to the place by dragging the grip located to the right of the panel name. It will stay there until you close the project so to leave it there forever I would advise to move it right after you create a new scene and then save its position by saving Startup File (File -> Defaults -> Save Startup File).
