from cvss import CVSS2, CVSS3, CVSS4


vector = 'AV:L/AC:L/Au:M/C:N/I:P/A:C/E:U/RL:W/RC:ND/CDP:L/TD:H/CR:ND/IR:ND/AR:M'
vector = "AV:L/AC:L/Au:N/C:P/I:N/A:N"
c = CVSS2(vector)
print(vector)
# print(c.get_value('AV'))
print(c.scores())


# vector = 'CVSS:3.0/S:C/C:H/I:H/A:N/AV:N/AC:H/PR:H/UI:R/E:H/RL:O/RC:R/CR:H/IR:X/AR:X/MAC:H/MPR:X/MUI:X/MC:L/MA:X'
# c = CVSS3(vector)
# print(vector)
# print(c.get_value('AV'))
# print(c.scores())
# print(c.severities())