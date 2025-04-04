# jpg_to_pdf_vectorizer.py

import os
import s2c

def convert_jpg_to_pdf(input_directory, output_directory, segment_params=(5, 3)):
    """
    Converts all JPG images in the specified input directory to vectorized PDF files.
    
    Args:
        input_directory (str): Path to the directory containing JPG images.
        output_directory (str): Path to the directory where the output PDF files will be saved.
        segment_params (tuple): Tuple containing two integers for segmentation (default: (5, 3)).
    """
    
    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Set up preset for vectorization
    preset = s2c.Preset()
    preset.method = s2c.Preset.Method.Solid
    
    # List all JPG images in the input directory
    imgs = s2c.list(input_directory, "jpg")
    
    for i in imgs:
        try:
            # Open image
            img = i.open()
            
            # Segment image
            img.segment(*segment_params)
            
            # Vectorize image
            vectorized_img = img.vectorize(preset)
            
            # Define output file path
            output_file = os.path.join(output_directory, f"{os.path.basename(i.path)}.pdf")
            
            # Export to PDF
            vectorized_img.exportToPdf(output_file)
            
            print(f"Successfully converted {i.path} to PDF.")
        
        except Exception as e:
            print(f"Error processing {i.path}: {e}")

if __name__ == "__main__":
    # Define input and output directories
    input_dir = "path/to/your/input_directory"  # Change to your input folder path
    output_dir = "path/to/your/output_directory"  # Change to your output folder path

    # Call the conversion function
    convert_jpg_to_pdf(input_dir, output_dir)
