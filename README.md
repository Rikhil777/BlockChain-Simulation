
# Basic Blockchain in Python

This project is a simple implementation of a blockchain in Python. It demonstrates the basic structure and functionalities of a blockchain, including proof-of-work mining, block creation, and chain validation. 

## Features
- **Genesis Block Creation:** Initializes the blockchain with the first "Genesis Block."
- **Proof of Work:** Implements mining by adjusting the `nonce` value to meet a required difficulty level.
- **Chain Validation:** Ensures the integrity of the blockchain by verifying that each block is linked correctly and that no data has been altered.
- **Data Storage:** Allows data to be added to each block.

## How It Works
1. **Block Creation:** Each block contains an index, timestamp, data, hash of the previous block, and its own unique hash.
2. **Mining Blocks:** The `mine_block` method performs proof-of-work by finding a hash that meets the specified difficulty level.
3. **Chain Validation:** The `is_chain_valid` method checks the integrity of the chain by verifying each block’s hash and the link between blocks.

## Code Structure

- `Block` Class: Represents each block in the chain.
  - `calculate_hash()`: Generates the SHA-256 hash for the block.
  - `mine_block(difficulty)`: Mines the block by finding a valid hash.
  
- `Blockchain` Class: Manages the chain and block addition.
  - `create_genesis_block()`: Creates the first block of the blockchain.
  - `add_block(data)`: Adds a new block with given data.
  - `is_chain_valid()`: Validates the blockchain integrity.
  - `display_chain()`: Prints details of each block in the blockchain.

## Getting Started

## Prerequisites
- Python 3.x
- `hashlib` and `time` libraries (standard in Python 3)

## Running the Code
1. Clone the repository:
   ```bash
   git clone https://github.com/Rikhil777/BlockChain-Simulation.git
   cd your-repository-name
   ```
2. Run the blockchain script:
   ```bash
   python blockchain.py
   ```

### Example Output
```plaintext
Mining block 1...
Block 1 mined with hash: <hash>
Mining block 2...
Block 2 mined with hash: <hash>
Mining block 3...
Block 3 mined with hash: <hash>

Blockchain:
Block 0 [Hash: <hash>]
  Previous Hash: 0
  Data: Genesis Block
  Timestamp: <timestamp>
  Nonce: <nonce>
...
```

## License
This project is licensed under the MIT License.

## Contact
Created by [Rikhil Kakani](https://github.com/Rikhil777). For any questions, please reach out to kakanirikhil7@gmail.com.


