import pytest
from sos.Tar import *

#1. 폴더 확인
def test_tarfile_mkdir():
    assert tar_mkdir('/Users/TRQ1/Downloads/tmp/') == '/Users/TRQ1/Downloads/tmp/'

#2. 압축 풀기
def test_tarfile_extrect():
    assert tar_extract('/Users/TRQ1/Downloads/sosreport-localhost.localdomain-20161115170426.tar.xz') == '/Users/TRQ1/Downloads/sosreport-localhost.localdomain-20161115170426'

#3. 폴더 생성 및 압축 풀기
def test_tarfile_extrect_all():
    assert tar_extract_all('/Users/TRQ1/Downloads/sosreport-localhost.localdomain-20161115170426.tar.xz', '/Users/TRQ1/Downloads/tmp/') == '/Users/TRQ1/Downloads/sosreport-localhost.localdomain-20161115170426'

