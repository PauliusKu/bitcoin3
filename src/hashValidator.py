import binascii
import hashlib

from bitcoin.rpc import RawProxy

class HashValidator:

    __rawProxy = RawProxy()

    def validate(self, blockHeight):

        blockHash = self.__rawProxy.getblockhash(int(blockHeight))
        blockHeader = self.__rawProxy.getblockheader(blockHash)

        headerHex = (self.__toLittleEndian(blockHeader['versionHex']) +
                     self.__toLittleEndian(blockHeader['previousblockhash']) +
                     self.__toLittleEndian(blockHeader['merkleroot']) +
                     self.__toLittleEndian(format(int(blockHeader['time']), 'x')) +
                     self.__toLittleEndian(blockHeader['bits']) +
                     self.__toLittleEndian(format(int(blockHeader['nonce']), 'x')))

        headerBinary = binascii.unhexlify(headerHex)
        newHash = self.__toLittleEndian(hashlib.sha256(hashlib.sha256(headerBinary).digest()).hexdigest())

        if blockHash == newHash:
            return True
        else:
            return False

    def __toLittleEndian(self, input):
        byteArr = bytearray.fromhex(input)
        byteArr.reverse()
        return ''.join(format(x, '02x') for x in byteArr)
