import os, hashlib, shutil

def hashfile(file):
	BUFFSIZE = 147456
	sha1 = hashlib.sha1()
	with open(file, 'rb') as f:
		while True:
			data = f.read(BUFFSIZE)
			if not data:
				break
			sha1.update(data)
		return sha1.hexdigest()

def remdup(path):
	for root, dirs, files in os.walk(path):
		Files = []
		for file in files:		
			file_loc = os.path.join(root, file)
			hashed_file = hashfile(file_loc)
			print(file)

			if (hashed_file not in Files):
				Files.append(hashed_file)

			else:
				print('duplicate removed')
				dup_dir_loc = os.path.join(root, 'duplicate_files')
				if (not os.path.exists(dup_dir_loc)):
					os.makedirs(dup_dir_loc)
				
				shutil.move(file_loc, os.path.join(dup_dir_loc, file))

remdup(path)