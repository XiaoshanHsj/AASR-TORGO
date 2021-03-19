import os
torgo_path = "/project_bdda3/bdda/sjhu/Data/torgo/"
speakers = ["F01", "F03", "F04", "FC01", "FC02", "FC03","M01", "M02", "M03", "M04", "M05", "MC01", "MC02", "MC03", "MC04"]

tag_path = "/project_bdda3/bdda/sjhu/Projects/AASR-TORGO/all_speakers/"
options = ["multi", "single"]

for op in options:
    utt_path = tag_path + "utt_" + op + "_tag"
    with open(utt_path, "r") as f:
        utts = f.readlines()
    
    for utt in utts:
        index, tran, tag = utt.split("\t")
        if tag.rstrip("\n") == "unseen" or tag.rstrip("\n") == "seen":
            tag = tag.rstrip("\n") + "Test"
        want_id = index+"-"+tag.rstrip("\n") +"Set-"+tran.rstrip("\n") + ".wav"
        
        spk, sess, mic_type, num = index.split("-")
        
        source_path = torgo_path + spk + "/" + sess + "/wav_" + mic_type + "/" + num + ".wav"
        des_path = torgo_path + spk + "/" + sess + "/wav.mapped/" + want_id
        
        command = "ln -s " + source_path + " " + des_path
        
        print(command)

