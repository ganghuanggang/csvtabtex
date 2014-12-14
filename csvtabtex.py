!/usr/bin/python
import sys

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

if __name__=="__main__":
	print sys.argv
	rr=open('/tmp/t2.csv','rU').read()
	t1=[l.split(',') for l in rr.split('\n') if l]
	content=''
	maxlen=max([len(line) for line in t1])
	for l in t1:
		if len(l)<maxlen:
			l.extend((maxlen-len(l))*[' '])
		content+=' & '.join(str(item) for item in l)+r'\\ \hline '+'\n'
	pos='|'+maxlen*' c |'
	print basictab(pos=pos,content=content)
