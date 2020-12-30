import pandas as pd 
from pandas import DataFrame
from pandas import Series
import time

df = pd.read_excel('C:/Users/tianan/Desktop/常用表格/servers.xls',sheet_name='AllServers')
df2 = pd.read_excel('C:/Users/tianan/Desktop/常用表格/bk_cmdb_export_host.xlsx',sheet_name='host')
#获取每个columns的值
Iplist = df['IP地址']
sim_note = df['简要说明']
account = 'appuser'
passwd = 'app@2017'
port = '22'
OS = 'LINUX'
privilege = '否'

#serverfilename = 'D:/' + time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))+'oldserver.xls'
#newserverfilename = 'D:/' + time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))+'newserver.xls'
#passwdfilename = 'D:/' + time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))+'oldpasswd.xls'
#newpasswdfilename = 'D:/' + time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))+'newpasswd.xls'

def df_maker(data,filename,format):
    format = '.'+ format
    file_locat = 'D:/' + time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) + filename + format
    df = pd.DataFrame(data)
    df.to_excel(file_locat,index=False)
    return df

def passwd_df_maker(data,account,passwd,filename,format):
    format = '.'+ format
    file_locat = 'D:/' + time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) + filename + format
    if account == 'root':
        privilege = '是'
    else:
        privilege = '否'
    df = pd.DataFrame(data)
    df.to_excel(file_locat,index=False)
    return df

#def privilege():
#    if account == 'root':
#        privilege = '是'
#    else:
#        privilege = '否'
#    return privilege 

bk_node_man_data = {'IP地址':Iplist,'操作系统':OS,'端口':port,'账号':account,'密码':passwd}
new_baoleiji_data = {'资产名称':Iplist,
                     '资产IP':Iplist,
                     '资产类型':'Linux',
                     '部门':'基础设施',
                     '编码类型':'UTF-8',
                     '简要说明':sim_note,
                     '责任人':'',
                     '资产组':'',
                     '账号名':'',
                     '密码':'',
                     '是否特权':privilege,
                     '禁用':''
                     }

service_passwd_data = {'Server Name':Iplist,
                       'Server Address':Iplist,
                       'Account':account,
                       'Password':passwd,
                       'Domain':'',
                       'Su Account':'',
                       'Domain IP':''}

new_service_passwd_data = {'资产名称':Iplist,
                           '帐号':account,
                           '密码':passwd,
                           '域名':'',
                           '密钥':'',
                           '切换自':'',
                           '是否特权':privilege,
                           '密钥列表':''}

bk_host_data = {'主机ID':'',	
                '内网IP(必填)':Iplist,
                '所在国家':'中国',
                '所在省份':'上海市',	
                '虚拟类型':'exsi',	
                '主机类型':'虚拟机',	
                '数据中心':'卡园',	
                '是否为数据库':'否',	
                '外网IP':'',
                '固资编号':'',	
                '设备SN':'',	
                '质保年限':'',	
                '所属运营商':'',	
                '管理IP':'',
                'FIRMWIRE版本':'',	
                'BIOS版本':'',	
                '所属区域':'',	
                '电源是否打开':'',
                '物理机业务IP':'',	
                '主机名称':'',	
                '操作系统类型':'',	
                '操作系统名称':'',	
                '操作系统版本':'',	
                '操作系统位数':'',	
                'CPU逻辑核心数':'',	
                'CPU频率':'',	
                'CPU型号':'',	
                '内存容量':'',	
                '磁盘容量':'',	
                '内网MAC地址':'',	
                '外网MAC':'',	
                '主要维护人':'',	
                '备份维护人':'',	
                '备注':'',	
                'SLA级别':'',	
                '应用系统名称':'',	
                '使用证书':'',	
                '应用负责人':'',	
                '业务IP1':Iplist,	
                '业务IP2':'',	
                '应用主机类型':'',	
                '业务拓扑':'',
                }

bk_host_assocation = {'关联标识':'',
                      '操作':'',
                      '源实例':'',
                      '目标实例':''}


df_maker(bk_node_man_data,'bk_node','xlsx')
df_maker(new_baoleiji_data,'new_baoleiji','xlsx')
passwd_df_maker(service_passwd_data,'root','vm@2013','service_passwd','xls')
passwd_df_maker(new_service_passwd_data,'root','vm@2013','new_service_passwd','xls')

#df3=DataFrame(bk_host_data)
#bk_host = [df2,df3]
#result = pd.concat(bk_host)
#df4 = pd.DataFrame(bk_host_assocation,index=[0])
#writer = pd.ExcelWriter('D:/bk_host.xlsx')
#result.to_excel(writer,'host',index=False)
#df4.to_excel(writer,'assocation',index=False)
#writer.save()

#result.to_excel('D:/bk_host.xlsx',sheet_name='host',index=False)
#df4.to_excel('D:/bk_host.xlsx',sheet_name='assocation',index=False)
