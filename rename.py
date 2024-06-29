import os
import re

def rename_file(file_path):
  """Renames a .txt file based on the number in the filename and the H1 title.

  Args:
      file_path (str): The path to the .txt file.
  """

  # Extract the number from the filename
  file_name = os.path.basename(file_path)
  match = re.search(r'\d+', file_name)
  if not match:
    return  # Skip files without a number

  file_number = match.group()

  # Extract the H1 title from the file content
  with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
    match = re.search(r'^# (.*)', content, re.MULTILINE)
    if not match:
      return  # Skip files without an H1 title

    h1_title = match.group(1).strip()

  # Sanitize the H1 title for filename use
  h1_title = re.sub(r'[<>:"/\\|?*]', '', h1_title)  # Remove invalid characters
  h1_title = h1_title.replace(' ', '-')  # Replace spaces with hyphens

  # Construct the new filename (truncate to 250 characters)
  new_file_name = f"{file_number}-{h1_title[:245 - len(file_number)]}.txt"
  new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

  # Rename the file
  os.rename(file_path, new_file_path)

# Get all .txt files in the current directory
txt_files = [f for f in os.listdir() if f.endswith('.txt')]

# Rename each .txt file
for file in txt_files:
  file_path = os.path.join(os.getcwd(), file)
  rename_file(file_path)
