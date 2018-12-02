import pandas as pd 
import glob 

levels = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

csv_dir = 'rawData/'

def parseCSV(level): 
	files = glob.glob(csv_dir + '*_' + str(level) + '.csv')
	
	d = {'time': pd.read_csv(files[0])['time']}
	pid = 1 

	for csv in files: 
		data = pd.read_csv(csv)
		d['status'+str(pid)] = data['status']

		pid += 1 

	return d 

def processData(level):
	def countStatus(x, status): 
		count = 0
		for s in x:
			count = count + 1 if s in status else count 
		return count 


	data = parseCSV(level)
	df = pd.DataFrame(data=data)
	print (df)

	df['unsure'] = df.apply(lambda x: countStatus(x, ['unsure']), axis=1)
	df['green'] = df.apply(lambda x: countStatus(x, ['green']), axis=1)
	df['red'] = df.apply(lambda x: countStatus(x, ['red']), axis=1)
	df['all'] = df.apply(lambda x: countStatus(x, ['unsure', 'green', 'red']), axis=1)

	df['unsure percent'] = round(df['unsure']/df['all'], 4)
	df['green percent'] = round(df['green']/df['all'], 4)
	df['red percent'] = round(df['red']/df['all'], 4)

	return df 

def createCSV(level):
	df = processData(level)
	csvFile = csv_dir + 'processed' + str(level) + '.csv'

	with open(csvFile, 'w') as f: 
		df.to_csv(f)

