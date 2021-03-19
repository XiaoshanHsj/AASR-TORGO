import os

wav_scp = "/project_bdda3/bdda/sjhu/Projects/torgo_asr/data/all_speakers/wav.scp"
data_path = "/project_bdda3/bdda/sjhu/Data/torgo"
wav_num = 0
arti_num = 0
with open(wav_scp, 'r') as f:
    lines = f.readlines()
    for line in lines:
        name = line.split()[0]
        wav_num = wav_num + 1
        speaker, session, _, utterance = name.split("-")
        arti_path = data_path + "/" + speaker + "/" + session + "/pos/" + utterance + ".pos"
        if os.path.exists(arti_path):
            arti_num = arti_num + 1

print("wav_num: ", wav_num)
print("arti_num: ", arti_num)
print("radio: ", arti_num / wav_num * 100, "%")
