#!/bin/bash
mkdir /tmp/struts2result2020
cd /tmp/struts2result2020
get_lan_ip  () {
   #
   ip addr | \
       awk -F'[ /]+' '/inet/{
               split($3, N, ".")
               if ($3 ~ /^192.168/) {
                   print $3
               }
               if (($3 ~ /^172/) && (N[2] >= 16) && (N[2] <= 31)) {
                   print $3
               }
               if ($3 ~ /^10\./) {
                   print $3
               }
          }'

   return $?
}

ip=$(get_lan_ip | head -1)
touch /tmp/struts2result2020/$ip
echo -n $ip >> /tmp/struts2result2020/$ip

if [ -d "/app/deployment" ];then
    result=$(find /app/deployment/ -name "struts2-core*" -print)
    
    if [ -z $result ];then
        echo "null" >> /tmp/struts2result2020/$ip
    else
        echo -n $result >> /tmp/struts2result2020/$ip
    fi
else
    echo "NoStruts" >> /tmp/struts2result2020/$ip
fi

