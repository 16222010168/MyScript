#!/bin/sh
#遍历目录下的所有文件，并读出写入单独文件
FILE_PATH="/xxx/xxxx"
cd $FILE_PATH
for FILE in `ls`
    do
    cat $FILE >> /tmp/test.log
    echo >> /tmp/test.log
    done


#获取主机的IP地址
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

