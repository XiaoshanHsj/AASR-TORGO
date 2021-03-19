import os
torgo_path = "/project_bdda3/bdda/sjhu/Data/torgo/"
speakers = ["F01", "F03", "F04", "FC01", "FC02", "FC03","M01", "M02", "M03", "M04", "M05", "MC01", "MC02", "MC03", "MC04"]

for sp in speakers:
    sp_path = torgo_path + sp
    dirs = os.listdir(sp_path)
    for d in dirs:
        if d.find("Session") != -1:
            sess = sp_path + "/" + d
            command = "rm "+ sess+ "/wav.mapped/*"
            os.system(command)
