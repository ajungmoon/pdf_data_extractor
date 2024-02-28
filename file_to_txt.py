import sys
import os
import subprocess


outdir = './PDF_to_TXT'

# Import a list of file locations (file_locations.txt) to pull PDFs from
# Use ls > file_locations.txt in commandline if importing all files from a specific folder

# OR alternatively, in commandline of the folder with PDFs, do ==> for i in *.pdf; do pdftotext "$i"; done
# GREP function to optiomise ==> grep -B2 -Pzo "(?s)Statistics.*Value.*Mean.*Standard Deviation.*?Standard Error.*?[0-9]\.[0-9]"  ECSE\ 200\ \ Electric\ Circuits\ 1\ -\ Lecture\ \(Section\ 001\ \ CRN\ 2275\)\ -\ Marwan\ Kanaan\ \(Fall\ 2023\)_d68f6d1b-82a6-42bb-8573-c2ca67805e14en-US.txt 


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
