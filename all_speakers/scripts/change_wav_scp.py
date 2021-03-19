file_path = "/project_bdda3/bdda/sjhu/Projects/AASR-TORGO/all_speakers/"

options = ["sentence", "word"]

for op in options:
    op_path = file_path + op
    wav_path = op_path + "/wav.scp"
    with open(wav_path,"r") as f:
        wavs = f.readlines()
    
    
    for i in range(len(wavs)):
        wav = wavs[i]
        
        index, tran, tag = wav.split("\t")
        if tag.rstrip("\n") == "unseen" or tag.rstrip("\n") == "seen":
            tag = tag.rstrip("\n") + "Test"
        want_id = index+"-"+tag.rstrip("\n")+"Set-"+tran.rstrip("\n") + "\n"
        
        wavs[i] = want_id
        
        print(wavs[i])
    
    with open(wav_path,"w") as f:
        f.writelines(wavs)
