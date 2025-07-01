# File Content Processor 📂✏️

A Python script that reads a file, processes its content (converting to uppercase), and saves the modified version to a new file.

## Features ✨
- File reading with proper error handling
- Content modification (uppercase conversion)
- Safe file writing operations
- Comprehensive error management
- User-friendly console interface

## How It Works 🔧

### Execution Flow
1. Prompts user for input filename
2. Reads file content with UTF-8 encoding
3. Converts content to uppercase
4. Writes modified content to `modified_[original_filename]`
5. Provides success/error feedback

### Code Structure
```python
def read_and_write_file():
    try:
        # 1. File reading
        filename = input("Enter the filename to read: ")
        with open(filename, 'r') as file:
            content = file.read()
        
        # 2. Content processing
        modified_content = content.upper()
        
        # 3. File writing
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            
    # Error handling cases...
