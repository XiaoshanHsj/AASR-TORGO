torgo_path = "/project_bdda3/bdda/sjhu/Data/torgo/"

file_path = "/project_bdda3/bdda/sjhu/Projects/AASR-TORGO/all_speakers/"
options = ["sentence", "word"]

for op in options:
    op_path = file_path + op
    wav_path = op_path + "/wav.scp"
    with open(wav_path,"r") as f:
        wavs = f.readlines()
     
    #wavs = ["F01-Session1-arrayMic-0008-trainSet-S62"]    
        
    for i in range(len(wavs)):
        wav = wavs[i]
        
        spk = wav.split("-")[0]
        sess = wav.split("-")[1]
        
        d_path = torgo_path + spk + "/" + sess + "/wav.mapped/" + wav.rstrip("\n") + ".wav"
        
        wavs[i] = wavs[i].rstrip("\n") + " " + d_path + "\n"
        
        #print(wavs[i])
    with open(wav_path,"w") as f:
        f.writelines(wavs)
