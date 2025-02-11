This is a simple blockchain simulation built using Python. It allows users to add transactions, generate new blocks, validate the blockchain, and detect tampering. The interface is implemented using Gradio for user-friendly interaction.

Block Structure: Each block contains an index, timestamp, transactions, previous hash, and current hash.
SHA-256 Hashing: Ensures data integrity by linking blocks cryptographically.
Proof-of-Work (PoW): Implements basic difficulty-based mining.
Blockchain Validation: Detects tampering by checking hash integrity.
Gradio UI: Simple and interactive web interface for managing the blockchain.
🛠️ Setup & Installation
1️⃣ Prerequisites
Ensure you have Python installed on your system. You can check this by running:

python --version
If not installed, download Python from python.org.

2️⃣ Install Required Libraries
Run the following command to install dependencies:

pip install gradio
▶️ Running the Application
Execute the following command in the terminal or command prompt:

python blockchain.py
After running the script, a Gradio interface will open in your browser.

🎮 How to Use
Enter Transactions: Type a transaction and click "Add Block".
View Blockchain: The UI will display the list of blocks.
Validate Blockchain: Click "Validate Blockchain" to check integrity.
Tamper Data & Test Integrity: Modify a block and test if validation fails.

🛠️ File Structure

├── blockchain.py   # Main Python script
├── README.md       # Setup and usage instructions
📜 License
This project is for educational purposes. Feel free to modify and experiment! 🚀
