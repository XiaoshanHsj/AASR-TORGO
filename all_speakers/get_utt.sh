text=/project_bdda3/bdda/sjhu/Projects/torgo_asr/data/all_speakers/text

awk 'NF>2' $text > utt_multi
awk 'NF==2' $text > utt_single
