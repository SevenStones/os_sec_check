from ccvapp.tasks import winrm_cmd

def winrm_cmd_munger():

    result = {}
    task_out = {}

    result['ipconfig'] = winrm_cmd.apply_async(('ipconfig',), countdown=1)
    task_out['ipconfig'] = result['ipconfig'].get()
    task_out['ipconfig']['results_div'] = "ipconfig"

    result['lastlogins'] = winrm_cmd.apply_async((r"powershell.exe C:\Users\Administrator\desktop\lastlogins.ps1",), countdown=1)
    task_out['lastlogins'] = result['lastlogins'].get()

    result['password_age'] = winrm_cmd.apply_async((r"powershell.exe Get-ItemProperty -Path HKLM:\SYSTEM\CurrentControlSet\Services\Netlogon\Parameters -Name MaximumPasswordAge",), countdown=1)
    task_out['password_age'] = result['password_age'].get()

    result['ntp'] = winrm_cmd.apply_async((r"powershell.exe C:\Users\Administrator\desktop\ntpstatus.ps1",), countdown=0)
    task_out['ntp'] = result['ntp'].get()

    result['lmcompat'] = winrm_cmd.apply_async((r"powershell.exe Get-ItemProperty -Path hklm:\System\CurrentControlSet\Control\Lsa -Name LmCompatibilityLevel",), countdown=0)
    task_out['lmcompat'] = result['lmcompat'].get()

    return task_out
