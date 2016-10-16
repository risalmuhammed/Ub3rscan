import sys
import socket
import argparse
from datetime import datetime
from dict import ports_list, logo_list, author, color

def justify(p_no):
	return (5-len(str(p_no))) * ' '

def scanner(target_ip,port):

	port_range = port.split('-')
	start_time = datetime.now()
	print '\n[*] Scan started at :' + color.RED+ ' {}'.format(start_time) + color.ENDC
	print 'Target: {0}, Ports: {1}\n\n'.format(target_ip,port)

	try:
		for port in range(int(port_range[0]),int(port_range[1])):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			response = sock.connect_ex((target_ip,port))
			if response == 0:	
				service_name = ports_list[str(port)+'/tcp']
				print color.GREEN + '[+] port {0}'.format(port) + justify(port) + \
									'open - {1} '.format(port,service_name) + color.ENDC
			sock.close()
	except KeyboardInterrupt:
		print '\nCtrl+c\nExiting...'
		sys.exit()
	except socket.gaierror:
		print 'Hostname couldn\'t be resolved'
		sys.exit()
	except socket.error:
		print 'Can\'t create socket'
		sys.exit()

	end_time = datetime.now()
	print '\n\n[*] Scan completed at : ' + color.RED +'{}'.format(end_time) + color.ENDC
	run_time = end_time - start_time
	print 'Total time for scanning : {}'.format(run_time)

def banner():
	print color.BOLD + '-' * 44 + color.OKGREEN
	for item in logo_list:
		print item.decode('base64','strict').rstrip('\n')

	print '\n\tAuthor:' + author.decode('base64', 'strict')
	print color.ENDC + color.BOLD
	print '-' * 44 + color.ENDC
def main():
	parser = argparse.ArgumentParser(prog='ub3rscan')
	parser.add_argument('target',help='IP Address of the Target machine (DDN)')
	parser.add_argument('ports',help='Range of ports to scan, ex: 1-65535')	
	args = parser.parse_args()
	
	banner()
	scanner(args.target,args.ports)

if __name__ == '__main__':
	main()
	
	
