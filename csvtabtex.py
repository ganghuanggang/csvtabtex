#!/usr/bin/python
import os,sys
import argparse
def basictab(caption=r'test',pos=r'|c|c|',content=r'test&test\\\hline',label=r'testlabel'):
	tabletex=r'''\begin{table}[ht]
\caption{%s}
\centering
\begin{tabular}{%s }
\hline
%s
\hline
\end{tabular}
\label{table:%s}
\end{table}'''%(caption,pos,content,label)
	return tabletex

def csv2lists(filename):
	rr=open(filename,'rU').read()
	t1=[l.split(',') for l in rr.split('\n') if l]
	content=''
	maxlen=max([len(line) for line in t1])
	for l in t1:
		if len(l)<maxlen:
			l.extend((maxlen-len(l))*[' '])
		content+=' & '.join(str(item) for item in l)+r'\\ \hline '+'\n'
	pos='|'+maxlen*' c |'
	return {'pos':pos,'content':content}
	
def non_zero_file(filename):
	size=0
	try:
		size=os.stat(filename).st_size
	except:
		msg = "%s is not a non-zero file" % filename
		raise argparse.ArgumentTypeError(msg)
	return filename

if __name__=="__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("input",help="input csv file, csvtabtex convert it to tex",type=non_zero_file)
	parser.add_argument('-o','--output',help="output tex file, if not given, use stdout") 
	args=parser.parse_args()
	print args.input
	
	file='/tmp/t2.csv'
	file=args.input
	print basictab(**csv2lists(file))
