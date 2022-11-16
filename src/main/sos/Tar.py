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
        def is_within_directory(directory, target):
            
            abs_directory = os.path.abspath(directory)
            abs_target = os.path.abspath(target)
        
            prefix = os.path.commonprefix([abs_directory, abs_target])
            
            return prefix == abs_directory
        
        def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
        
            for member in tar.getmembers():
                member_path = os.path.join(path, member.name)
                if not is_within_directory(path, member_path):
                    raise Exception("Attempted Path Traversal in Tar File")
        
            tar.extractall(path, members, numeric_owner=numeric_owner) 
            
        
        safe_extract(f)
