#!/bin/bash
echo "[+] Executing autocommit script"
grep "successfully pushed to Docker Hub" /tmp/log.txt | awk '{print $2}' >> /tmp/updated_images.txt
if [ -s /tmp/updated_images.txt ] ; then 
    printf "\n### ["$(date +%F)"]\n" >> $PWD/LOG.md ;
    for i in `cat /tmp/updated_images.txt`; do split=(${i//:/ }) ; echo "- ${split} updated to version ${split[1]}" >> $PWD/LOG.md ; done
fi

# Use the exit code got from the log
exit_code=$(grep "RAUDI completed" /tmp/log.txt | awk '{print $8}')
echo "[+] Exiting with the same exit code got from the logs ($exit_code)"
exit $exit_code