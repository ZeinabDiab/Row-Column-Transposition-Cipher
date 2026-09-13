# 🔐 Row-Column Transposition Cipher

> An interactive educational GUI application for demonstrating the
> Row-Column Transposition Cipher using Python and Tkinter.

---

## 📌 Overview

This project is an interactive implementation of the **Row-Column Transposition Cipher**, developed as an educational tool to demonstrate how transposition-based encryption and decryption work.

The application provides a simple graphical interface where users can:

- Enter plaintext or ciphertext.
- Provide a permutation key.
- Encrypt text using the Row-Column Transposition algorithm.
- Decrypt ciphertext back to plaintext.
- Validate permutation keys.
- Visualize the practical use of the algorithm through a GUI.

The project was developed to connect **cryptography concepts, algorithms, and GUI development** in one practical application.

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Understand the working principle of the Row-Column Transposition Cipher.
- Implement both encryption and decryption algorithms.
- Demonstrate permutation-based column ordering.
- Validate encryption keys before processing.
- Handle plaintext of different lengths.
- Build an easy-to-use graphical interface for educational purposes.
- Provide a visual explanation of the algorithm through an accompanying presentation.

---

## 🔑 How the Algorithm Works

The Row-Column Transposition Cipher rearranges the characters of a message according to a **permutation key**.

### Example Key


3 1 4 2The key determines the order in which columns are read during encryption.

Encryption Process
Remove spaces from the input text.
Convert the text to uppercase.
Validate that the key is a valid permutation.
Place the plaintext into a matrix row by row.
Determine the column reading order from the permutation key.
Read the matrix column by column according to the key order.
Produce the resulting ciphertext.
Decryption Process
Remove spaces from the ciphertext.
Validate the permutation key.
Calculate the number of rows and the length of each column.
Determine the original column order from the key.
Fill the matrix column by column using the ciphertext.
Read the matrix row by row.
Recover the original plaintext.
🧠 Algorithm Concepts

This implementation demonstrates several important concepts:

Permutation keys
Matrix representation
Row-wise insertion
Column-wise traversal
Column reordering
Encryption and decryption
Input validation
Modular algorithmic thinking
🖥️ Graphical User Interface

The application was built using Tkinter, Python's standard GUI library.

The interface contains:

Text input area
Permutation key input
Encrypt button
Decrypt button
Output area
Error handling for invalid keys
Example Key Format
```text
3 1 4 2

The key must contain every integer from 1 to n exactly once.

For example:

3 1 4 2     ✅ Valid
1 2 3 4     ✅ Valid
1 2 2 4     ❌ Invalid
1 2 3       ❌ Invalid for a 4-column key
🛠️ Technologies Used
Technology	Purpose
Python	Core programming language
Tkinter	Graphical User Interface
Cryptography	Cipher implementation
Algorithms	Encryption and decryption logic
📂 Project Structure
Row-Column-Transposition-Cipher/
│
├── row_column_transposition.py
│
├── Presentation/
│   └── Row-Column-Transposition-Presentation.pdf
│
├── screenshots/
│   └── gui.png
│
└── README.md
▶️ How to Run
1. Clone the repository
git clone https://github.com/YOUR_USERNAME/row-column-transposition-cipher.git
2. Navigate to the project directory
cd row-column-transposition-cipher
3. Run the application
python row_column_transposition.py

No external Python packages are required because the project uses Python's built-in tkinter library.

🧪 Example
Input
HELLOWORLD
Key
3 1 4 2

The algorithm:

Places the characters into a matrix.
Determines the column order using the permutation key.
Reads the columns according to the key.
Produces the ciphertext.

The ciphertext can then be entered into the application and decrypted using the same key.

⚠️ Key Validation

The application verifies that the provided key is a valid permutation.

A key is considered valid when:

sorted(key) == [1, 2, ..., n]

For example:

Key: 3 1 4 2

Sorted Key:
1 2 3 4

Result:
Valid permutation

Invalid keys trigger an error message instead of performing encryption or decryption.

📚 Educational Presentation

An accompanying presentation was created to explain:

The concept of transposition ciphers
The Row-Column Transposition algorithm
Encryption steps
Decryption steps
Permutation keys
Matrix construction
Practical examples
Implementation details

The presentation is included in this repository for reference.

💡 What I Learned

Through this project, I practiced:

Translating cryptographic algorithms into working code.
Designing encryption and decryption workflows.
Working with matrices and permutations.
Handling input validation and errors.
Building desktop GUI applications with Tkinter.
Explaining technical algorithms through visual and presentation-based material.
Connecting theoretical cryptography concepts with practical implementation.
🔐 Disclaimer

This project is developed for educational and demonstration purposes.

The Row-Column Transposition Cipher is a classical cryptographic technique and should not be considered secure for modern real-world communication.

👩‍💻 Author

Zeinab Abd El Monem Mohamed Diab

Computer Science & Artificial Intelligence Student
Information Systems

GitHub: ZeinabDiab
LinkedIn: Zeinab Diab
⭐ Project Highlights
🔐 Classical cryptography implementation
🔄 Encryption & decryption
🔑 Permutation key validation
🧮 Matrix-based algorithm
🖥️ Interactive Tkinter GUI
📚 Accompanying educational presentation
🐍 Pure Python implementation
