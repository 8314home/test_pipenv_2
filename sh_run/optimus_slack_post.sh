#!/bin/sh

#################################################################################################
# Script_name : optimus_slack_post.sh
# Author : smukherjee
# Description: This script read from teradata table sandbox.post_slack_message for slack messages to be posted.
#              Query result is put into a csv file. If any records present, slack posts will be done to corresponding
#              Channels. Once posted those records will be updated.
#              Exit 2 code is returned if slack is not in list of allowed slack channels
# Usage: sh optimus_slack_post.sh
#################################################################################################

export DAT=/tmp
export SLACK_FILE=/tmp/optimus_jobs_slack_post.csv
export login=/home/svc_ima/common/.tdwd_logon_ub_ma_emea
export dbpassword=$(awk -F '[,;]' '{print $2}' ${login})

rm -rf $SLACK_FILE

# tdsql feature - https://github.com/groupon/tdsql

# Select all records for which slack post is not done yet
tdsql -H tdwd -u ub_ma_emea -p $dbpassword -c UTF8 -m ANSI -o $SLACK_FILE -f csv "select REGEXP_REPLACE(slack_message||' UTC-'||job_completion_time||' Job Name-'||job_name||';'||channel,'\n','') as full_record from sandbox.post_slack_message where posted_flag='FALSE';"


# Perform Slack Post
# ---- Check for file record count
file_record_count=`wc -l < $SLACK_FILE`
echo "SLACK_FILE = $SLACK_FILE"
echo "file_record_count = $file_record_count"

# ---- Check if any jos completed to do a slack post, 0 mean no job completed
if [ "$file_record_count" = "0" ]
then
  echo "No Jobs completed recently ,$SLACK_FILE is empty "
else
  while IFS= read -r line
  do
    echo "line= $line"
    # ";" is being used as a delimiter
    slack_message=$(echo "$line"|cut -d';' -f1)
    slack_channel=$(echo "$line"|cut -d';' -f2)
    echo -e "\nslack_message = $slack_message"
    echo -e "slack_channel = $slack_channel"
    webhook_slack_channel=$(grep -w "$slack_channel" ~/common/.all_slack_channels|cut -d"=" -f2)

    # Add any new channel in file ~/common/.all_slack_channels
    if [ "$webhook_slack_channel" = "" ]
    then
      echo "Error: $slack_channel not in list of slack channels.
      Either add channel in file or configure to post into channel. below are list of channels supported "
      cut -d'=' -f1 < ~/common/.all_slack_channels
      echo "SKIP - skipping this post"
    else
      curl -X POST -H 'Content-type: application/json' --data "{'text': '$slack_message' }" $webhook_slack_channel
    fi
    # echo -e "webhook_slack_channel = $webhook_slack_channel"

    echo -e "\n ------------------------"
  done < "$SLACK_FILE"
fi

# Update records as slack post is done now
tdsql -H tdwd -u ub_ma_emea -p $dbpassword -c UTF8 -m ANSI "update sandbox.post_slack_message set posted_flag='TRUE' where posted_flag='FALSE';"

echo "Completing script"
exit 0
