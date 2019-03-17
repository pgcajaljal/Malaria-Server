
from ..models import db, Case, Image, Database, Chunklist, Chunk, Infection
import os, sys, threading, random, time

class detectionThread(threading.Thread):
	def __init__(self, name):
		threading.Thread.__init__(self)
		self.name = name
		self.threadID = random.randint(1, 1000)
		self.startt = time.time()
		self.setDaemon(True)
		# TODO: Create a string function for printable version

	def run(self):
		print(sys.platform)
		if (not self.system()):	
			print("Detection thread is stopped.")
			return		
		# while(1):

		print(threading.enumerate())
		if(len(threading.enumerate()) > 2):
			print("Too many threads")
			return
		print("\"I am continuously running\" - " + self.name, self.startt, time.time() - self.startt)
		x = self.query()
		if x == 0:
			print('No more detections to do.')
		print("Detection thread is stopped.")
		time.sleep(15)
		
	def query(self):
		inf = Infection.query.filter(Infection.name=="Malaria").first()
		caselist = Case.query.filter(Case.infection_id==inf.id).all()	

		for case in caselist:
			if case.chunklist_id == None:	continue
			chunklist = Chunklist.query.filter(Chunklist.id==case.chunklist_id).first()
			imagelist = Image.query.filter(Image.case_id==case.id, Image.prelim_diagnosis=="").all()
			for image in imagelist:
				print("THIS X"+image.prelim_diagnosis+"X")
				print("yip", chunklist.filename, image.id, image.case_id, image.prelim_diagnosis)
				img = [f for f in os.listdir(str('upload/'+chunklist.filename)) if f[-4:] == ".jpg" or f[-4:] == ".png"][image.number-1]
				print(img)
				if (self.system): self.detector(str('~/Desktop/remidiv2/upload/'+chunklist.filename)+'/'+img, image.id)
		return 0



	def detector(self, img, img_id):
		print("SOME DETECTOR IS RUNNING")
		import subprocess
		imgfile = img
		print(img)
		jsonfile = "jsonfile.txt"		
		f = open("./serveus/darknet/"+jsonfile, 'w')
		f.close()
		print(os.getcwd())
		weights = "thin_weights.weights"
		cmd = "nohup ./darknet detector test thin/thin_data.data thin/thin_cfg.cfg thin/thin_weights.weights " +imgfile+" -out "+jsonfile+" &"
		pro = subprocess.Popen(cmd, cwd="serveus/darknet/", shell = True)
		time.sleep(60)
		pro.wait()
		print("SOME DETECTOR IS AWAKE")
		self.savetodb(img_id, jsonfile)

	def savetodb(self, img_id, jsonfile):
		print("Saving to DB")
		# Clean save_json_file
		f = open("./serveus/darknet/"+jsonfile, 'r')
		jsonstr = "{" + ''.join([line for line in f.readlines()][4:-2]).strip() + "}"
		f.close()
		print("JSTR ", jsonstr)
		# Save to DB1
		img = Image.query.filter(Image.id==img_id).first()
		img.prelim_diagnosis = jsonstr
		db.session.commit()
		print("DB SAVED")
		print(Image.query.filter(Image.id==img.id).first().prelim_diagnosis)

	def system(self):
		if "linux" in sys.platform:
			print("Server is running on Linux!")
			return True
		elif sys.platform == "win32":
			print("Server is currently running on Windows. Malaria detection is only configured to run in Linux.")
			return False	

def main():
	thread1 = detectionThread("Malaria Detection")
	thread1.start()

if __name__ == "__main__":
	main()

