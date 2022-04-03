"""
======================
@author:LCH
@time:2022/4/2:14:05
@email:786608954@qq.com
======================
"""
# --*--encoding:utf-8--*--
import hashlib
class CiphertextMaker:

    def make_md5(self,data):
        md5obj=hashlib.md5(data.encode('utf-8'))
        obj_data=md5obj.hexdigest()
        return obj_data
if __name__ == '__main__':
    o=CiphertextMaker('123333')
    print(o.make_md5())