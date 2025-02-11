import hashlib
import time
import gradio as gr
import json

class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_data = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self, difficulty):
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self, difficulty=3):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def add_block(self, transactions):
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), transactions, previous_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False, f"Block {i} hash mismatch!"
            if current_block.previous_hash != previous_block.hash:
                return False, f"Block {i} previous hash mismatch!"
        return True, "Blockchain is valid!"

    def tamper_block(self, index, new_data):
        if index == 0 or index >= len(self.chain):
            return "Invalid block index!"
        self.chain[index].transactions = new_data
        self.chain[index].hash = self.chain[index].calculate_hash()
        return f"Block {index} tampered!"

blockchain = Blockchain()

def add_block_ui(transactions):
    blockchain.add_block(transactions)
    return display_chain()

def display_chain():
    return json.dumps([{ "index": block.index, "transactions": block.transactions, "hash": block.hash, "prev_hash": block.previous_hash } for block in blockchain.chain], indent=4)

def validate_chain():
    valid, message = blockchain.is_chain_valid()
    return message

def tamper_block_ui(index, new_data):
    return blockchain.tamper_block(int(index), new_data)

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# Basic Blockchain Simulation")
    transactions_input = gr.Textbox(label="Enter Transactions")
    add_block_button = gr.Button("Add Block")
    output = gr.Textbox(label="Blockchain", interactive=False)
    add_block_button.click(add_block_ui, inputs=transactions_input, outputs=output)
    
    validate_button = gr.Button("Validate Blockchain")
    validate_output = gr.Textbox(label="Validation Result", interactive=False)
    validate_button.click(validate_chain, outputs=validate_output)
    
    tamper_index = gr.Number(label="Block Index to Tamper")
    tamper_data = gr.Textbox(label="New Transaction Data")
    tamper_button = gr.Button("Tamper Block")
    tamper_output = gr.Textbox(label="Tamper Result", interactive=False)
    tamper_button.click(tamper_block_ui, inputs=[tamper_index, tamper_data], outputs=tamper_output)
    
    output.value = display_chain()

demo.launch()
