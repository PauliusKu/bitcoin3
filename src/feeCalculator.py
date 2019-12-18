from bitcoin.rpc import RawProxy

class FeeCalculator:

    __rawProxy = RawProxy()

    def calculate(self, trxId):
        trx = self.__getTransaction(trxId)

        inputSum = 0
        outputSum = 0

        for vOutput in trx['vout']:
            outputSum += vOutput['value']

        for vInput in trx['vin']:
            inputSum += self.__getTrxOutputByIndex(vInput['txid'], vInput['vout'])

        return inputSum - outputSum

    def __getTrxOutputByIndex(self, trxId, outputIndex):
        trx = self.__getTransaction(trxId)
        itr = 0

        for vOutput in trx['vout']:
            if outputIndex == itr:
                return vOutput['value']
        itr += itr

    def __getTransaction(self, trxId):
        rawTrx = self.__rawProxy.getrawtransaction(trxId)
        return self.__rawProxy.decoderawtransaction(rawTrx)
 
