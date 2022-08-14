from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client


class FDFSStorage(Storage):

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        # 创建一个fdfsclient对象
        client = Fdfs_client('utils/fdfs/client.conf')
        ret = client.upload_by_buffer(content.read())
        if ret.get('Status') != 'Upload success.':
            raise Exception('上传文件失败')
        filename = ret.get('Remote file_id')
        return filename

    def exists(self, name):
        # 判断文件名是否可用
        return True
