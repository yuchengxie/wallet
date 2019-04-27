# from binascii import hexlify
# from binascii import unhexlify
import binascii
import hashlib
import wallet
import struct


# def sha256(data):
#     return hashlib.sha256(data).digest()

# # print(hexlify(b'abcd123'))
# # h = sha256(sha256(b'abcd123'))
# def ttt():
#     s0=b'010000000131a66dd0de9f7f68936a1058ecc1c6c623018f73deca93744b4124ed9fb6aa0f010000002876b8230000db83cf42e02199d4fa29d14a197a167ade519298f0c2f98ec5478092497bcd5c00b7acffffffff0200e1f505000000002876b8230000e5c7b20d5b5037f86e9861cd8795be42e8093c61bd36256a2b5a22df6508a8ba00b7aca0ff2d6f090000002876b8230000db83cf42e02199d4fa29d14a197a167ade519298f0c2f98ec5478092497bcd5c00b7ac0000000001000000'

#     s1=unhexlify(s0)

#     addr = wallet.read_account_('addr1', 'xieyc', True)
#     app = wallet.WalletApp(addr, vcn=0)

#     # h = sha256(sha256(s1))

#     # print('>>> payload抓换hash:\n', hexlify(h), len(hexlify(h)))
#     #70-72
#     s1 = addr.sign(s0)
#     print('>> sign:\n',hexlify(s1),len(s1))

# ttt()


wallet.record('helloworld')

# values = (1, 'ab'.encode('utf-8'), 2.7)
# values = ('ab'.encode('utf-8'))
# # s=struct.Struct('I2sf')
# s=struct.Struct('2s')
# packed_data=s.pack(*values)

# print('原始值:', values)
# print('格式符:', s.format)
# print('占用字节:', s.size)
# print('打包结果:', binascii.hexlify(packed_data))







