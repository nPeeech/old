#!/bin/sh

while true
do

    clipboard=`xsel --clipboard --output`

    if echo $clipboard | grep -i youtube >/dev/null && echo $clipboard | grep -i watch >/dev/null; then
    
        xsel --clipboard --clear

        vlc $clipboard
    fi

    sleep 3s

done
