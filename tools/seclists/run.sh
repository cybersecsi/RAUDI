#!/bin/sh

cat << EOF 
This is the docker image of SecLists repository

https://github.com/danielmiessler/SecLists  
bind the volume on a useful path: 

docker run --rm -v $PWD/wordlists:/usr/share/wordlists/SecLists secsi/seclists  

EOF
tail -f /dev/null