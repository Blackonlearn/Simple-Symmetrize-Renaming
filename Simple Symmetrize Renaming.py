#This simple code is mine, and it has already been pushed to github repo as my archive:https://github.com/Blackonlearn/Simple-Symmetrize-Renaming

import bpy

C = bpy.context
D = bpy.data

def symmetrizeName():
    L_Name = C.active_bone
    for i,j in enumerate(C.selected_pose_bones):
        if j.name == L_Name.name:
            pass
        else:
            a = f"{L_Name.name}"
            if ".L" in a:
                R_Name = a.replace(".L",".R")
            elif ".R" in a:
                R_Name = a.replace(".R",".L")
            elif ".F" in a:
                R_Name = a.replace(".F",".B")
            elif ".B" in a:
                R_Name = a.replace(".B",".F")
            print(R_Name)
            j.name = R_Name
        
symmetrizeName()
