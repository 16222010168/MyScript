import pandas as pd 
from pandas import DataFrame
from pandas import Series
import time


#读取原始excel表格数据
source_path = 'C:/Users/tianan/Desktop/常用表格/servers.xls'
source_path_sheet = 'AllServers'

df = pd.read_excel(source_path,sheet_name=source_path_sheet)
df2 = pd.read_excel('C:/Users/tianan/Desktop/常用表格/bk_cmdb_export_host.xlsx',sheet_name='host')

#获取每个columns的值
Iplist = df['IP地址']
sim_note = df['简要说明']

#账户密码
account = {'appuser':'app@2017' ,'root':'vm@2013','weblogic':'weblogic@2013','loguser':'log@2017'}
#其他信息
sysinfo = {'port':'22','OS':'Linux','privilege':'否'}

#蓝鲸节点管理导入数据
bk_node_man_data = {'IP地址':Iplist,'操作系统':'LINUX','端口':'22','账号':'root','密码':'vm@2013'}
#新堡垒机资产导入数据
new_baoleiji_data = {'资产名称':Iplist,
                     '资产IP':Iplist,
                     '资产类型':sysinfo['OS'],
                     '部门':'基础设施',
                     '编码类型':'UTF-8',
                     '简要说明':sim_note,
                     '责任人':'',
                     '资产组':'',
                     '账号名':'',
                     '密码':'',
                     '是否特权':sysinfo['privilege'],
                     '禁用':''
                     }



#蓝鲸硬件资产导入数据
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

#bk_host_assocation = {'关联标识':'',
#                      '操作':'',
#                      '源实例':'',
#                      '目标实例':''}
#新堡垒机密码导入数据
def new_service_passwd_data(zhanghao):
    new_service_passwd_data = {'资产名称':Iplist,
                           '帐号':zhanghao,
                           '密码':account[zhanghao],
                           '域名':'',
                           '密钥':'',
                           '切换自':'',
                           '是否特权':'否',
                           '密钥列表':''}
    return new_service_passwd_data

#生成Excel表格
def df_maker(data,filename,format):
    format = '.'+ format
    file_locat = 'D:/' + time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())) + filename + format
    df = pd.DataFrame(data)
    df.to_excel(file_locat,index=False)
    return df


def main():
    df_maker(new_baoleiji_data,'new_baoleiji','xlsx')
    df_maker(bk_node_man_data,'bk_node_man','xlsx')
    for i in account:
        
        if i == 'root':
            PasswdData = new_service_passwd_data(i)
            PasswdData['是否特权'] = '是'
        else:
             PasswdData = new_service_passwd_data(i)
             PasswdData['是否特权'] = '否'

        filename = i + 'Password'
        df_maker(PasswdData,filename,'xls')

main()


    


    
