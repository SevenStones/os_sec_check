from winrm.protocol import Protocol
from celery import Celery, task, shared_task

#
# s = winrm.Session('192.168.183.156', auth=('Administrator', 'Octl!9!2'), transport='basic')
# t = s.run_cmd('ipconfig', ['/all'])

@shared_task()
def winrm_cmd(cmd):

    result = {
        'std_out': "",
        'std_err': "",
    }

    p = Protocol(
        endpoint='https://192.168.183.203:5986/wsman',
        transport='basic',
        username=r'user_name',
        password='password',
        server_cert_validation='ignore')

    try:
        shell_id = p.open_shell()
    except ConnectionError as e:
        result['std_err'] = str(e)
        return result
    except Exception as e:
        result['std_err'] = str(e)
        return result


    command_id = p.run_command(shell_id, cmd)
    std_out, std_err, status_code = p.get_command_output(shell_id, command_id)

    p.cleanup_command(shell_id, command_id)
    p.close_shell(shell_id)

    # result['std_out'] = std_out.decode()
    result['std_out'] = std_out.decode()
    result['std_err'] = std_err.decode()

    return result