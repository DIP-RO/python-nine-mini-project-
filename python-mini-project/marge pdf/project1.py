from PyPDF2 import PdfMerger
AllPDF = ["algo4front.pdf","https.pdf"]
merger = PdfMerger()
for i in AllPDF:
    merger.append(i)

merger.write("dipro.pdf")
merger.close()