import os
from zipfile import ZipFile

_ROCKYOU_ZIP_PATH = os.path.join(
    os.path.dirname(
        os.path.realpath(__file__)
    ),
    'rockyou.zip'
)
_ROCKYOU_FILE_NAME = 'rockyou.txt'


def load():
    with ZipFile(_ROCKYOU_ZIP_PATH) as rockyou_archive:
        with rockyou_archive.open(_ROCKYOU_FILE_NAME) as rockyou:
            for line in rockyou:
                yield line.decode().strip()
