import re

str_data = """
duplicate key value violates unique constraint "apiv1_phonemodelcustomco_phone_model_id_name_668cb444_uniq"
DETAIL:  Key (phone_model_id, name)=(6, 电源) already exists.
"""

pattern = re.compile(r'=[(](.*),(.*)[)]')
m = pattern.search(str_data)
print(m)
print(m.group(2))
