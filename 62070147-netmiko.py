from netmiko import ConnectHandler

device = {
    'ip' : '10.0.15.108',
    'username': 'admin',
    'password': 'cisco',
    'device_type': 'cisco_ios'
}

commands_create = ["int loopback 62070147",
            "ip add 192.168.1.1 255.255.255.0",
            "no shut"]

commands_delete = ["no int loopback 62070147"]

with ConnectHandler(**device) as ssh:
    result = ssh.send_command('sh ip int loopback 62070147')
    words = result.strip().split('\n')
    if words[1][-14:] == '192.168.1.1/24':
        ssh.send_config_set(commands_delete)
    else:
        ssh.send_config_set(commands_create)
    # print(words[1][-14:])
    # result = ssh.send_config_set(commands)