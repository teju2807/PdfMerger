import PyPDF2

pdfiles=[]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfiles=open(filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfiles)
    merger.append(pdfReader)
pdfiles.close()
merger.write('merged.pdf')