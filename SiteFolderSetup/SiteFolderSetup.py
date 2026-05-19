import os 
print)"Tashwill's Automation Tool: Folder Creator")
print("-" *30)

# 1. Where do i create the folder
base_path = r"C:\Users\USER\Downloads"

# 2. What will i name this folder 
project_name = "NEW_UWC_PROJECT"


# 3. Combining the base path with the project which will create my Folder
full_project_path = os.path.join(base_path, project_name)

# 4. I need to check if the folder already exist.If it doesnt, it must be created.
if not os.path.exist(full_project_path):
    os.makedirs(full_project_path)
    print(f"Created project folder at:{full_project_path}")

else:
    print("Main project folder already exists!")
print("-" *30)


# 5. If i want to create some subfolders within main project
sub_folders = ["Invoices", "Site_Photos","Daily_Logs"]





   
