
t_name_str = """
apiv1_abnormity
apiv1_abnormitydetail
apiv1_abnormitypolicy
apiv1_abnormitytype
apiv1_account
apiv1_account_device
apiv1_account_subsidiary_device
apiv1_androidversion
apiv1_appgather
apiv1_bug
apiv1_cabinet
apiv1_customtag
apiv1_device
apiv1_device_monitor_index
apiv1_devicecoordinate
apiv1_devicecutcoordinate
apiv1_devicepower
apiv1_devicescreenshot
apiv1_devicetemperature
apiv1_job
apiv1_job_android_version
apiv1_job_custom_tag
apiv1_job_phone_models
apiv1_job_rom_version
apiv1_job_test_area
apiv1_jobflow
apiv1_jobflow_inner_flow
apiv1_jobresourcefile
apiv1_jobtestarea
apiv1_manufacturer
apiv1_monitorport
apiv1_paneslot
apiv1_paneview
apiv1_phonemodel
apiv1_powerport
apiv1_rds
apiv1_rdslog
apiv1_rdsscreenshot
apiv1_reefuser
apiv1_reefuser_groups
apiv1_reefuser_user_permissions
apiv1_romversion
apiv1_simcard
apiv1_subsidiarydevice
apiv1_system
apiv1_tboard
apiv1_tboard_device
apiv1_tboardjob
apiv1_tempport
apiv1_testgather
apiv1_testgather_job
apiv1_tguard
apiv1_unit
apiv1_woodenbox
auth_group
auth_group_permissions
auth_permission
authtoken_token
django_admin_log
django_content_type
django_migrations
django_session
"""

def join_sql():
    t_name_list = [data for data in t_name_str.split('\n') if data not in ['', 'django_session']]
    print(len(t_name_list))
    for t_name in t_name_list:
        print(f"select setval('{t_name}_id_seq', max(id)) from {t_name};")

if __name__ == '__main__':
    join_sql()
