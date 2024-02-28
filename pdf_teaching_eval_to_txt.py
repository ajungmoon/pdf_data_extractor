import sys
import os
import subprocess


#outdir = './PDF_to_TXT'

# Import a list of file locations (file_locations.txt) to pull PDFs from
# Use ls > file_locations.txt in commandline if importing all files from a specific folder

# OR alternatively, in commandline of the folder with PDFs, do ==> for i in *.pdf; do pdftotext "$i"; done
# This produces .txt files with the same file name as the PDFs.

## EXTRACT Mean values only by first looking for the "Value" as keyword and printing 12 lines below (capturing Mean,SD,SE), then pipe it to print specific statistic (e.g., Mean) and numbers only.
# grep -A 12 "Value" filename.txt | grep -A 2 "Mean" | grep -E '[0-9\.]*' -o

## Do this in a for loop within the folder containing the .txt files if we want to walk through each file
# for i in *.txt; do printf "%s%s" $i; printf "\n"; grep -A 12 "Value" "$i" | grep -A 2 "Mean" | grep -E '[0-9\.]*' -o; done >> Mean.txt
# for i in *.txt; do printf "%s%s" $i; printf "\n"; grep -A 12 "Value" "$i" | grep -A 2 "Standard Error" | grep -E '[0-9\.]*' -o; done >> SE.txt
# for i in *.txt; do printf "%s%s" $i; printf "\n"; grep -A 12 "Value" "$i" | grep -A 2 "Standard Deviation" | grep -E '[0-9\.]*' -o; done >> SD.txt



with open('file_locations.txt', 'r') as f:
    for count, line in enumerate(f, start=1):
        ext = os.path.splitext(line.strip())[-1].lower()
        # print("preparing output in" +
        #       os.path.join(outdir, "file-%02d.txt" % count))
        if ext == '.pdf':
            try:
                subprocess.check_output(['pdftotext', line.strip()])
            except subprocess.CalledProcessError as e:
                print(line.strip())
                print(e.output)
                pass
        elif ext == '.docx':
            try:
                subprocess.check_output(
                    ['pandoc', line.strip(), '-o',
                     os.path.join(outdir, "file-%02d.txt" % count)])
            except subprocess.CalledProcessError as e:
                print(line.strip())
                print(e.output)
                pass
        else:
            print(line.strip())
            pass
