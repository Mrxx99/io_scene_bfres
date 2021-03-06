import bpy
import os

# ---- Preferences ----

class BfresAddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    def _get_tex_conv_path(self):
        return self.tex_conv_path

    def _set_tex_conv_path(self, value):
        # Check if the selected path is the executable.
        if os.path.isfile(value):
            self.tex_conv_path = value
        else:
            raise AssertionError("The selected path is not the TexConv2 executable.")

    # General
    tex_conv_path = bpy.props.StringProperty()
    tex_conv_path_ui = bpy.props.StringProperty(name="TexConv2.exe Path", description="Path of the proprietary TexConv2 executable to convert textures with.", subtype='FILE_PATH', get=_get_tex_conv_path, set=_set_tex_conv_path)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "tex_conv_path_ui")


# ---- Methods & Mixins ----

def log(indent, text):
    indent = " " * 2 * indent
    print("BFRES: {}{}".format(indent, text))
