#!/usr/bin/python
# -*- coding: cp936 -*-
# -*- coding: encoding -*-
import cx_Oracle
class connectOracle():
    def __init__(self,ora="PH_CS "):
        if ora=="ORCL_ODS":
            self.db = cx_Oracle.connect("pcl/Phpcl321@221.236.20.211:15213/orcl")  # �������ݿ�
            self.cr = self.db.cursor()  # ����cursor
        elif ora=='wms':
            self.db = cx_Oracle.connect("wms/wms@112.45.122.19:11521/orcl")  # �������ݿ�
            self.cr = self.db.cursor()  # ����cursor
        elif ora=='wms_pro':
            self.db = cx_Oracle.connect("smsplat/s0splm@221.236.20.212:15212/orcl")  # �������ݿ�
            self.cr = self.db.cursor()  # ����cursor
        elif ora=='PH_CS':
            self.db = cx_Oracle.connect("pcltest/Phtest123@221.236.20.222:15218/orcl")  # �������ݿ�
            self.cr = self.db.cursor()  # ����cursor

    def sqlSelect(self,sql):
        global rs
        try:
            self.cr.execute(sql)#zִ��sql���
            rs=self.cr.fetchall()#һ�η������н����
        except Exception as err:
            print(err)
        finally:
            self.cr.close()
            self.db.close()
        return rs
    def sqlDML(self,sql):
        global rs
        try:
            self.cr.execute(sql)  # zִ��sql���
            rs = self.cr.fetchall()  # һ�η������н����
        except Exception as err:
            print(err)
        finally:
            self.cr.close()
            self.db.commit()
        return rs
    def sqlFlashBack(self):
        self.cr.execute("select sql_text,last_load_time from v$sql where sql_text like '%update%' order by last_load_time desc")  # ����SQLִ����ʷȷ�����ݻع�ʱ���
        self.cr.execute("alter table tablename enable row movement")#�ٽ����ݻع�����Ҫ��ʱ���
        self.cr.execute("flashback table tablename to timestamp to_timestamp('xxxx-xx-xx xx:xx:xx', 'yyyy-mm-dd hh24:mi:ss')")
sql=" select * from (select tb.*, rownum " \
    "from T_SMSPLTFORM_SNED_DATA tb where tb.applic_code = 'DH_NOTICE' order by tb.busi_dt desc)" \
    "where rownum=1 "
#f=connectOracle("wms_pro").sqlSelect(sql)
#print (f[0][2]).decode('GBK').encode('UTF-8')#������ģ���������

#context_demo = connectOracle("wms_pro").sqlSelect(sql)
#context = (context_demo[0][2]).decode('GBK').encode('UTF-8')
#print(context)