import socket
import subprocess

def v4_or_v6(ip):
    """ Returns - 4 if IP address id valid and supports ipv4
    - 6 if IP address is valid and supporst ipv6
    - None otherwise
    """
    try:
        socket.inet_aton(ip)
        return '4' if ip.count('.') == 3 else None
    except socket.error:
        try:
            socket.inet_pton(socket.AF_INET6, ip)
            return '6'
        except socket.error:
            return None
			

def do_ping(ip, udp=False, count='5', packet_size='50', timeout='1000'):
    """ Executes the system ping command.
    - Returns ping command data.
    """
    command = 'ping'
    if udp:
        command+='6'
    options = ['-c ' + str(count), '-s ' + str(packet_size), '-W ' + str(timeout)]
    try:
        p = subprocess.Popen([command, options[0], options[1], options[2], ip], stdout=subprocess.PIPE)
    except Exception as e:
        return [e.message], None
    output = p.communicate()
    return output[1], output[0].split('\n')
	
	
def ping(ip, udp=False, count='5', packet_size='50', timeout='1000'):
	pa, pb = do_ping(ip, udp, count, packet_size, timeout)
	if pa is not None:
		return None
	ret = dict()
    ret['pingResult'] = '\n'.join(ping_res)
    ret['pingStatus'] = False
    try:
        if not (ping_res[-3].find(' 0 received') > 0):
            ret['pingStatus'] = True
    except Exception as e:
        pass
	return ret
