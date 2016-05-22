import sys
import socket
import argparse
from datetime import datetime
from dict import port_dict, logo_list, author

def scanner(target_ip,port):

	port_range = port.split('-')
	start_time = datetime.now()
	print '\nScan started at : {}'.format(start_time)
	print 'Target: {0}, Ports: {1}\n\n'.format(target_ip,port)

	try:
		for port in range(int(port_range[0]),int(port_range[1])):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			response = sock.connect_ex((target_ip,port))
			if response == 0:
				try:
					service_name = port_dict[port]
				except:
					service_name = 'Unknown Service'	
				print 'port {0}: open - {1} '.format(port,service_name)
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
	print '\n\nScan completed at : {}'.format(end_time)
	run_time = end_time - start_time
	print 'Total time for scanning : {}'.format(run_time)

def banner():
	print '-' * 44
	for item in logo_list:
		print item.decode('base64','strict').rstrip('\n')

	print '\n\tAuthor:' + author.decode('base64', 'strict')
	print '-' * 44
def main():
	parser = argparse.ArgumentParser(prog='ub3rscan')
	parser.add_argument('target',help='IP Address of the Target machine (DDN)')
	parser.add_argument('ports',help='Range of ports to scan, ex: 1-65535')	
	args = parser.parse_args()
	
	banner()
	scanner(args.target,args.ports)

if __name__ == '__main__':
	main()
	
	
