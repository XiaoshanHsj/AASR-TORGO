speakers="F01 F03 F04 FC01 FC02 FC03 M01 M02 M03 M04 M05 MC01 MC02 MC03 MC04"

for spk in $speakers; do
    #cat $spk/text | cut -d' ' -f2- | sort | uniq > $spk/text_uniq
    awk 'NF>2' $spk/text > $spk/text_multi
    awk 'NF==2' $spk/text > $spk/text_single
done
