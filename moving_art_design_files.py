import os
import shutil
def moving_artfile(file_path):
    for folder in os.scandir(file_path):     
        root=f"{file_path}/{folder.name}"
        art_dir= f"{root}/"
        for files in os.scandir(art_dir):
            if files.is_file():
                if files.name.startswith(".DS_"):
                    continue
                all_files=files.name #all files inside design Folder
                new_path="D:\Joel\design"
                print(f"moving file {all_files}")
                shutil.move(f"{art_dir}/{all_files}", new_path)
        print("--------Art Files moved Successfully-----------")    

def move_design_file(file_path):

    for folder in os.scandir(file_path):     
        root=f"{file_path}/{folder.name}"
        design_dir= f"{root}/design"
        for files in os.scandir(design_dir):
            all_files=files.name #all files inside design Folder
            new_path="D:\Joel\design"
            if not os.path.exists(new_path):
                os.mkdir(new_path)
                print("created Successfully")
            print(f"moving file {all_files}")
            shutil.move(f"{design_dir}/{all_files}", new_path)            
        print("--------Design files Moved Successfully--------")
                    
           


move_design_file("D:\Joel\After script")
moving_artfile("D:\Joel\After script")