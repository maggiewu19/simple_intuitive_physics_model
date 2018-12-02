import subprocess 
import glob 

kerberos = ['adcheng', 'cylin321', 'ergold', 'eweng', 'graceyin', 'isab8liu',
			'leonyim', 'maggiewu', 'phuongpm', 'shinc', 'tifftao', 'wclaudia', 
			'weitung', 'wkl', 'wualbert', 'xzou', 'yunb']

folder = 'rawData/'

for name in kerberos: 
	name_len = len(name)
	folder_len = len(folder)
	files = glob.glob(folder + name + '*.csv')

	for f in files: 
		new_name = f[folder_len:folder_len+name_len] + '_' + f[folder_len+name_len:]
		MV_CMD = 'mv ' + f + ' ' + new_name
		subprocess.check_output(MV_CMD, shell=True)