from winrm.protocol import Protocol
#
# s = winrm.Session('192.168.183.156', auth=('Administrator', 'Octl!9!2'), transport='basic')
# t = s.run_cmd('ipconfig', ['/all'])


def winrm_cmd(cmd):

    p = Protocol(
        endpoint='https://192.168.183.186:5986/wsman',
        transport='basic',
        username=r'Administrator',
        password='Octl!9!2',
        server_cert_validation='ignore')
    shell_id = p.open_shell()
    command_id = p.run_command(shell_id, cmd)
    std_out, std_err, status_code = p.get_command_output(shell_id, command_id)
    p.cleanup_command(shell_id, command_id)
    p.close_shell(shell_id)

    return std_out

