import os
from my_logger import log
from pypdf import PdfReader
from pathlib import Path

# TODO - (INPUT) receive variable input  
BASE_DIR = Path(__file__).resolve().parent.parent  # points to lab1_testing3/
folder_path = BASE_DIR / "lab_sub"
file_names = [f for f in folder_path.iterdir() if f.is_file() and f.suffix.lower() == ".pdf"]

for fn in file_names:
  reader = PdfReader(fn)
  num_pages = len(reader.pages)

  txt = ''
  for i in range(num_pages):
    pge = reader.pages[i]
    t = pge.extract_text()
    if t: txt += t

  # TODO - (PROCESS) each lab 'matched' lab
  file_prefix = Path(fn).stem.lower()  match file_prefix: 
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
