import os

'''
categories = []

for file in os.listdir('data/images/T_files'):
    category = file.split('_')[0]

    if category not in categories:
        try:
            os.mkdir(BASE_PATH+'/'+category)
        except:
            pass

    source_path = BASE_PATH+'/T_files/'+file
    dest_path = BASE_PATH+f'/{category}/{file}'
    os.rename(source_path, dest_path)'''

'''runs = 0

for cat_folder in os.listdir('data/images'):
    try:
        suffix = cat_folder[-4:]
    except:
        continue

    if  suffix == '.png':
        os.rename(f'data/images/{cat_folder}/{cat_folder}', f'data/images/manual_sort/{cat_folder}')
        os.rmdir(f'data/images/{cat_folder}')
        runs += 1
print(runs)'''
