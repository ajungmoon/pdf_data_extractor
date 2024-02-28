import sys
import os
import subprocess


outdir = './PDF_to_TXT'

# Import a list of file locations (file_locations.txt) to pull PDFs from
# Use ls > file_locations.txt in commandline if importing all files from a specific folder

# OR alternatively, in commandline of the folder with PDFs, do ==> for i in *.pdf; do pdftotext "$i"; done

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
