import os

def scan_directory(path, prefix=''):
    markdown_list = []
    dir_list = []
    file_dict = []

    # Scan the current directory
    items = sorted(os.listdir(path))
    for item in items:
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            # Directories are added to a list and processed first
            dir_list.append(item)
        else:
            file_dict.append(item)

    # Add directories to markdown_list
    for d in dir_list:
        markdown_list.append(f"{prefix}- {d}/")
        markdown_list += scan_directory(os.path.join(path, d), prefix + '    ')

    # Sort and add files to markdown_list
    for file in file_dict:
        markdown_list.append(f"{prefix}- {file}")

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