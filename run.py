""" Ubuntu Agent POC 
Author by: Suvvada Sonia

It connects to windows machine using WinRm
and executes installer & uninstaller scripts

-----------------------
Author: Suvvada Sonia - Jr. Software Engineer - sonia.s@tessrac.com
CopyRights - Tessrac Innovations Pvt Ltd.

"""

# import winrm

# session = winrm.Session('192.168.43.193', auth = ('CT', '1234567890'))
# # session = winrm.Session('192.168.43.193', auth = ('CT', '1234567890'))
# # session = winrm.Session('192.168.56.1', auth = ('varalaxmi', 'Varalaxmi'))
# # session = winrm.Session('192.168.0.103', auth = ('vinod', 'Do0ordie17k'))
# output = session.run_cmd('ipconfig', ['/all'])

# print(output)

import winrm

s = winrm.Session('10.0.2.15', auth=('SoniaWin', 'Sonia@5355'))
r = s.run_cmd('ipconfig', ['/all'])
print(r.status_code)
print(r.std_out)
print(r.std_err)
