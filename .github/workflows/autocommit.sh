#!/bin/bash
echo "Printing workflow log..."
cat /tmp/log.txt
grep -B3 "Image successfully pushed" /tmp/log.txt | grep "secsi/" | awk '{print $6}' >> /tmp/updated_images.txt
if [ -s /tmp/updated_images.txt ] ; then 
    printf "\n["$(date +%F)"]\n" >> $PWD/LOG.txt ;
    for i in `cat /tmp/updated_images.txt`; do split=(${i//:/ }) ; echo "${split} updated to version ${split[1]}" >> $PWD/LOG.txt ; done
fi