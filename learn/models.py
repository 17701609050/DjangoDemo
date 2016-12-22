#coding:utf-8
from django.db import models
import json

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
    # 在Python3中使用 def __str__(self)
        return self.name

class CmccProjectChip(models.Model):
	chipid = models.AutoField(primary_key=True)
	chip_name = models.CharField(max_length=50)
	CPM = models.CharField(max_length=50)
	SW_TAM = models.CharField(max_length=50)
	HW_TAM = models.CharField(max_length=50)
	HW_RF = models.CharField(max_length=50)
	Audio_PL = models.CharField(max_length=50)
	Power_PL = models.CharField(max_length=50)
	PPM = models.CharField(max_length=50)
	Ali_PM = models.CharField(max_length=50)
	PLD_PM = models.CharField(max_length=50)
	CSD_PM = models.CharField(max_length=50)
	PHY_PL = models.CharField(max_length=50)
	Test_PL = models.CharField(max_length=50)
	PICLAB_FO = models.CharField(max_length=50)
	FT_FO = models.CharField(max_length=50)

	def toJSON(self):
		
	    return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

	def __unicode__(self):
	# 在Python3中使用 def __str__(self)
	    return self.chipid


class CmccProject(models.Model):
    ''' 项目信息表 '''

    project_id = models.AutoField(primary_key=True)
    chip_name = models.CharField(max_length=50)
    cust_name = models.CharField(max_length=50)
    send_test_type = models.CharField(max_length=50)
    test_range =models.CharField(max_length=50)
    plan_sendtest_time = models.CharField(max_length=50)
    operate_system =models.CharField(max_length=50)
    Radiofrequency_PA = models.CharField(max_length=50)
    project_name = models.CharField(max_length=50)
    config_name = models.CharField(max_length=50)
    current_status = models.CharField(max_length=50)
    v1_sendtest_time = models.CharField(max_length=50)
    v1_software_version = models.CharField(max_length=50)
    v2_sendtest_time = models.CharField(max_length=50)
    v2_software_version = models.CharField(max_length=50)
    v3_sendtest_time = models.CharField(max_length=50)
    v3_software_version = models.CharField(max_length=50)
    onmeeting_time = models.CharField(max_length=50)
    passed_time = models.CharField(max_length=50)
    v2_plan_sendtest_time = models.CharField(max_length=50)
    v3_plan_sendtest_time = models.CharField(max_length=50)
    passed_round_number = models.CharField(max_length=50)
    test_round_number = models.CharField(max_length=50)
    warehousing_month = models.CharField(max_length=50)
    out_warehousing_month = models.CharField(max_length=50)
    warehousing_days = models.CharField(max_length=50)
    project_status = models.CharField(max_length=50)
    submiter = models.CharField(max_length=50)
    Network_type = models.CharField(max_length=50)
    Project_owner = models.CharField(max_length=50)
    test_items = models.CharField(max_length=500)
    Cust_Model = models.CharField(max_length=500)

    def toJSON(self):
	    
	    return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
