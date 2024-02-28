# pdf_data_extractor
Extract text data from a series of standardised PDF files.

In the case of McGill Teaching Evaluation PDFs, run the following in commandline in the folder containing all pdfs. It produces .txt files of the same filename.

for i in *.pdf; do pdftotext "$i"; done

Then, in the folder containing the converted .txt files, run each of the following lines to produce text summaries of Mean, SD, and SE. Copy manually into a spreadsheet etc. afterwards.
# for i in *.txt; do printf "%s%s" $i; printf "\n"; grep -A 12 "Value" "$i" | grep -A 2 "Mean" | grep -E '[0-9\.]*' -o; done >> Mean.txt
# for i in *.txt; do printf "%s%s" $i; printf "\n"; grep -A 12 "Value" "$i" | grep -A 2 "Standard Error" | grep -E '[0-9\.]*' -o; done >> SE.txt
# for i in *.txt; do printf "%s%s" $i; printf "\n"; grep -A 12 "Value" "$i" | grep -A 2 "Standard Deviation" | grep -E '[0-9\.]*' -o; done >> SD.txt

