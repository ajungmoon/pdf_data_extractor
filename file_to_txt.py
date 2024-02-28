import sys
import os
import subprocess


outdir = './PDF_to_TXT'

# Import a list of file locations (file_locations.txt) to pull PDFs from
with open('file_locations.txt', 'r') as f:
    for count, line in enumerate(f, start=1):
        ext = os.path.splitext(line.strip())[-1].lower()
        # print("preparing output in" +
        #       os.path.join(outdir, "file-%02d.txt" % count))
        if ext == '.pdf':
            try:
                subprocess.check_output(['pdftotext', line.strip(),
                                         os.path.join(outdir, "file-%02d.txt" % count)])
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
