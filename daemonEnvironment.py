# Automation to check environment
import psutil as ps
import sys, os, time

def sys_check(percent):
	cpu_each = ps.cpu_percent(interval = 1, percpu = True)
	cpu_average = sum(cpu_each) / len(cpu_each)
	if percent >= int(100 - ps.virtual_memory().percent) or percent >= int(100 - cpu_average):
		print("warning sys")
		return False
	else:
		return True

def bat_check(flag, percent = None):
	battery = ps.sensors_battery()
	plugged = battery.power_plugged
	if bool(flag) == True and plugged == False:
		warn_F = 1
		print("warning bat")
	elif bool(flag) == False and bool(percent) == True:
		b_percent = int(battery.percent)
		if b_percent < percent:
			print("warning bat")
			return False		
		else:
			return True
	else:
		return True
		


def wifi_check(flag):
	net_stat = os.popen("hostname -I").read().strip()
	if bool(flag) == True and bool(net_stat) == False:
		print("warning sys")
		return False
	else:
		return True


if __name__ == "__main__":
	# environment check
	'''
	sys_flag = sys_check(50)
	bat_flag = bat_check(1)
	wifi_flag = wifi_check(1)
	sys_flag = 1
	bat_flag = 1
	wifi_flag = 1
	'''
	while True:
		sys_flag = sys_check(20)
		bat_flag = bat_check(1)
		wifi_flag = wifi_check(1)
		f = open("temppid.txt", "r")
		temp = f.read()	
		if bool(sys_flag) and bool(bat_flag) and bool(wifi_flag) == True:
			ps.Process(int(temp)).resume()
			time.sleep(5)
		else:
			ps.Process(int(temp)).suspend()



	
