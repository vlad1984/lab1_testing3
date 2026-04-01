import os
from my_logger import log
from pypdf import PdfReader

# TODO - (INPUT) receive variable input  
folder_path = "lab_sub/"
file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
file_names = [f for f in file_names if f.rsplit('.')[-1].lower() == 'pdf']

for fn in file_names:
  reader = PdfReader(fn)
  num_pages = len(reader.pages)

  txt = ''
  for i in range(num_pages):
    pge = reader.pages[i]
    t = pge.extract_text()
    if t: txt += t

  # TODO - (PROCESS) each lab 'matched' lab
  file_prefix = fn.rsplit('.')[0].lower()
  match file_prefix:  
    case "sample_report":
      q1,num_split,rest = txt.partition('2.')
      
      q1 = q1.replace('\n',' ')
      q1 = q1.lower()
      check_flag = all(word in q1 for word in ["input", "process", "output"])      

      if check_flag:  log.info("q1, passed")
      else:  
        log.error("expecting mention of input/process/output")
        failed = True
        
    case _:  
      log.error(f"{file_prefix} does not exist")
