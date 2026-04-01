import os
from my_logger import log
from pypdf import PdfReader

# TODO - (INPUT) receive variable input  
folder_path = "lab_sub/"
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
file_names = [f for f in file_names if f.rsplit('.')[-1].lower() == 'pdf']

for fn in file_names:
  reader = PdfReader(file_path)
  num_pages = len(reader.pages)

  txt = ''
  for i in range(num_pages):
    pge = reader.pages[i]
    txt += pge.extract_text()

  # TODO - (PROCESS) each lab 'matched' lab
  file_prefix = fn.rsplit('.')[0].lower()
  match file_prefix:  
    case "sample_report":
      q1,num_split,rest = txt.partition('2.')
      
      q1 = q1.replace('\n',' ')
      q1 = q1.lower()
      check_flag = 'input' in q1 and 'process' in q1 and 'output' in q1
      
      assert check_flag, "expecting mention of input/process/output"
      print("q1, passed")
    case _:  
      log.error(f"{file_prefix} does not exist")
