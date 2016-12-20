import os
import tarfile

def tar_extract_all(tar_file_name, tmp_dir):
     if not os.path.exists(tmp_dir):
         os.mkdir(tmp_dir)
         with tarfile.open() as f:
             for tarinfo in f:
                 if not (tarinfo.isreg() and tarinfo.name.endwith('.xml')):
                     continue
                 tarinfo.name = os.path.basename(tarinfo.name)
             f.extractall(tarinfo, tmp_dir)

def tar_mkdir(tmp_dir):
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)

def tar_extract(tar_file_name):
    with tarfile.open(tar_file_name, 'r:xz') as f:
        f.extractall()
