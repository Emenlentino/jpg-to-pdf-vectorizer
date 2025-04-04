# JPG to PDF Vectorizer

This Python script automates the process of converting JPG images into vectorized PDF files using the Solid vectorization method from the `s2c` library.

## Features
- Converts all JPG images in a specified directory to vector PDFs.
- Customizable segmentation parameters for image processing.
- Handles any number of JPG images in the input directory.

## Requirements
- Python 3.x
- `s2c` library: You can install it using `pip install s2c`.

## How to Use
1. Clone this repository:
    ```bash
    git clone https://github.com/Emenlentino/jpg-to-pdf-vectorizer.git
    cd jpg-to-pdf-vectorizer
    ```

2. Install the required dependencies:
    ```bash
    pip install s2c
    ```

3. Modify the input and output directory paths in the script:
    ```python
    input_dir = "path/to/your/input_directory"
    output_dir = "path/to/your/output_directory"
    ```

4. Run the script:
    ```bash
    python jpg_to_pdf_vectorizer.py
    ```

5. Check the output PDFs in the specified output directory.

## Example Usage

```python
convert_jpg_to_pdf("path/to/input_directory", "path/to/output_directory")
