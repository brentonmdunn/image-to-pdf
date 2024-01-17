import os
import img2pdf

def convert_images_to_pdf(input_folder, output_pdf):
    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Sort the image files to ensure the correct order in the PDF
    image_files.sort()

    # Create a list to store the image paths
    image_paths = [os.path.join(input_folder, image) for image in image_files]

    # Convert images to PDF
    with open(output_pdf, 'wb') as pdf_file:
        pdf_file.write(img2pdf.convert(image_paths))

# Specify the input folder containing images and the output PDF file
input_folder_path = input("Path to input folder: ")
output_pdf_path = input("Path and file name to result: ")

# Call the function to convert images to PDF
convert_images_to_pdf(input_folder_path, output_pdf_path)

print(f'PDF created successfully at {output_pdf_path}')
