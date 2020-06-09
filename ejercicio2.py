import sys

def get_sequence(file):
	next(file)  
	seq = ""

	for linea in file: 
		if len(linea.strip())!=0:
			linea=linea.rstrip('\n')
			seq = seq + linea

	file.close()

	return seq

if __name__ == '__main__':
	
	file1 = sys.argv[1]
	file2 = sys.argv[2]
	windows_size = int(sys.argv[3])
	threshold = int(sys.argv[4])

	f1 = open(file1, "r")
	f2 = open(file2, "r")

	seq1 = get_sequence(f1)
	seq2 = get_sequence(f2)

	#seq1 = "MSSSHSRCAQSAAVASPGKS"
	#seq2 = "MSSSHSRAGQSAAGAAPGGG"