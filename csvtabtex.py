#!/usr/bin/python
import os,sys
import argparse
def basictab(content,pos,caption=None,label=None):
	if caption==None:
		caption=r'test'
	if label==None:
		label=r'test'
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
	print 'filename is',filename
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
	if os.path.splitext(filename)[-1]!='.csv':
		msg = "%s extension is not .csv" % filename
		raise argparse.ArgumentTypeError(msg)
	return filename

if __name__=="__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("input",help="input .csv file, csvtabtex convert it to tex",type=non_zero_file)
	parser.add_argument('-o','--output',help="output .tex file, if not given, use input file with changed extension") 
	parser.add_argument('-f','--force',help="force overwrite output .tex file if existed")
	args=parser.parse_args()
	print args.input
	print args.output	
	csvin=args.input
	if args.output==None:
		
		texout=os.path.splitext(csvin)[0]+'.tex'
	elif args.output=='stdout':
		texout=None
	else:	
		texout=args.output
	tex_str=basictab(**csv2lists(csvin))
	if texout==None:
		print tex_str
	else:
		if not args.force:
			if os.path.exists(tex_str):
				print 'output file %s exist, Overwrite (o) ? Append (a)? Cancel (any other char)?'%tex_str
				response=sys.stdin.read(1)
				if response=='o' or response=='O':
					fwrite=open(texout,'w')
				elif response=='a' or response=='A':
					fwrite=open(texout,'a')
				else: 
					fwrite==None
			else:
				fwrite=open(texout,'w')
		else:
			fwrite=open(texout,'a')
		if fwrite:
			fwrite.write(tex_str)
			print 'write to %s'%texout
			fwrite.close()			


