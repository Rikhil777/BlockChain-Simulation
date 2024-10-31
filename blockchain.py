import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.nonce = 0  # Initialize nonce before calculating the hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        # Proof of work: make hash start with a certain number of zeroes
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
        print(f"Block {self.index} mined with hash: {self.hash}")


class Blockchain:
    def __init__(self, difficulty=2):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        # The first block of the blockchain with a fixed previous hash
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(index=latest_block.index + 1,
                          previous_hash=latest_block.hash,
                          data=data)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Verify that all blocks are linked correctly
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check hash consistency
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid hash at block {current_block.index}")
                return False
            # Check hash link with the previous block
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid link between block {previous_block.index} and {current_block.index}")
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(f"Block {block.index} [Hash: {block.hash}]")
            print(f"  Previous Hash: {block.previous_hash}")
            print(f"  Data: {block.data}")
            print(f"  Timestamp: {block.timestamp}")
            print(f"  Nonce: {block.nonce}")
            print("")


# Testing the Blockchain
if __name__ == "__main__":
    # Create a new blockchain and add some blocks
    my_blockchain = Blockchain(difficulty=2)

    print("Mining block 1...")
    my_blockchain.add_block("First block data")

    print("\nMining block 2...")
    my_blockchain.add_block("Second block data")

    print("\nMining block 3...")
    my_blockchain.add_block("Third block data")

    # Display the blockchain
    print("\nBlockchain:")
    my_blockchain.display_chain()

    # Check if the blockchain is valid
    print("Is blockchain valid?", my_blockchain.is_chain_valid())
