import hashlib

class NeuralCoinBLock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Keegan sends 2 BTC to Jeff"
t2 = "Jevan sends 6.3 BTC to Keegan"
t3 = "Jeff sends 3 BTC to Marcel"
t4 = "Marcel sends 7 BTC to Mike"
t5 = "Mike sends 8 BTC to Jevan"

intial_block = NeuralCoinBLock("Initial String", [t1,t2])
print(intial_block.block_data)
print(intial_block.block_hash)