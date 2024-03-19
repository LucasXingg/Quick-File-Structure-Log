import os

def scan_directory(path, prefix=''):
    """
    Scan the directory at 'path' and return its contents in a Markdown-formatted list.
    'prefix' is used internally to handle indentation for subdirectories.
    """
    # Initialize an empty list to hold the directory contents in Markdown format
    markdown_list = []

    # Get all items in the current directory sorted alphabetically
    items = sorted(os.listdir(path))
    
    # Loop through each item in the current directory
    for item in items:
        # Construct the full path to the item
        full_path = os.path.join(path, item)
        
        # Check if the item is a directory
        if os.path.isdir(full_path):
            # Add the directory name to the list, formatted as a Markdown list item
            markdown_list.append(f"{prefix}- {item}/")
            # Recursively scan the subdirectory, increasing the indentation
            markdown_list += scan_directory(full_path, prefix + '    ')
        else:
            # Add the file name to the list, formatted as a Markdown list item
            markdown_list.append(f"{prefix}- {item}")

    return markdown_list

def save_to_markdown_file(markdown_list, output_file_path):
    """
    Saves the markdown list to a file.
    """
    # Make sure the output directory exists
    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
    
    # Write the Markdown list to the file
    with open(output_file_path, 'w') as md_file:
        md_file.write('\n'.join(markdown_list))


if __name__ == "__main__":

    # Get the root directory path to scan
    root_path = input('Path to log: ')

    # Get teh folder name
    folder_name = root_path.split('/')[-1]

    # The path where the Markdown file will be saved
    output_file_path = f'./output/{folder_name}_structure.md'

    # Scan the directory and retrieve the Markdown list
    markdown_output = scan_directory(root_path)

    # Save the Markdown list to a file
    save_to_markdown_file(markdown_output, output_file_path)

    # Console Log
    print(f"Directory structure saved to {output_file_path}")