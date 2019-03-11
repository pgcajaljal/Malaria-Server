import subprocess
import time, datetime

def main():

	fname = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')


	# case = "20190225_211556_dinmt_8052813_32"
	case = "20190225_212143_dinmt_14355325_32"
	txtfile = case+'_prelim.txt'
	cmd2 = "touch logs/"+txtfile
	pro2 = subprocess.Popen(cmd2.split())
	x = pro2.wait()
	print('done x',x,cmd2)
	weights = "thin/thin_weights.weights"
	
	# plist = ["smp.jpg", "scream.jpg"]	
	# plist = ["20190225_211418_slide.jpg"]
	plist = ["20190225_211949_slide.jpg","20190225_212056_slide.jpg"]
	for file in plist:

		# imgfile = "smp.jpg"
		tempfile = "temp.txt"
		dumpfile = "dump.txt"

		cmd = "nohup ./darknet detector test thin/thin_data.data thin/thin_cfg.cfg "+weights+" "+file+" -out "+tempfile+" &"
		# cmd = "nohup ./darknet detector test thin/thin_data.data thin/thin_cfg.cfg thin/thin_weights.weights smp.jpg &> logs/"+fname+".txt &"
		pro = subprocess.Popen(cmd.split())
		print("I'm running", cmd)
		y = pro.wait()
		print('done y', y)


		cmd2 = "cat "+tempfile+" >> logs/"+txtfile
		print("I'm running 2", cmd2)
		pro2 = subprocess.Popen(cmd2, shell=True)
		z = pro2.wait()
		print('done z',z)

if __name__ == '__main__':
	main()
	# print(saved_output)