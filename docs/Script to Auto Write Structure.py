import os

# Define the path to your vault directory
# Place this script where you want the structure to be written.
vault_path = os.getcwd()


# Function to create the mkdocs navigation structure
def generate_nav_structure(root_dir):
    nav = {}
    for root, dirs, files in os.walk(root_dir):
        relative_path = os.path.relpath(root, root_dir)
        if relative_path == ".":
            relative_path = ""
        for file in files:
            if file.endswith(".md"):
                section = relative_path.replace(os.sep, " > ")
                if section not in nav:
                    nav[section] = []
                nav[section].append(file)
    return nav

# Generate navigation structure
nav_structure = generate_nav_structure(vault_path)

# Print the structure in mkdocs.yml format
if os.path.exists('File Structure.txt') == False:
    pass
else:
    print('File Already Existed, Deleting...')
    os.remove('File Structure.txt')
    print('File Deleted')
    

print('Creating File Structure...')

logfile = open('File Structure.txt','a')
for section, files in nav_structure.items():
    if section:
        logfile.write(f"{section}:\n")
        # print(f"{section}:")
    for file in files:
        file_title = os.path.splitext(file)[0].replace("-", " ").title()
        file_path = os.path.join(section.replace(" > ", "/"), file).replace(" ", "%20")
        logfile.write(f"  - {file_title}: {file_path}\n")
        # print(f"  - {file_title}: {file_path}")
logfile.close()


input('Press enter to close')
