import os, sys
import csv
import frontmatter
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Assume we are in the /tools directory 
lp_base_dir = '../content/learning-paths'
ig_base_dir = '../content/install-guides'

output_csv = 'learning_paths_metadata.csv'

# Hardcoded URLs for the learning paths
learn_url = 'https://learn.arm.com/'


# Define the CSV columns
csv_columns = ['Full URL', 'Learning Path Title', 'Weight', 'Step Title',
               'Author', 'Skill Level', 'Subjects', 'Arm IP', 'OS', 'Tools Software Languages', 'Content Category', 
               'Minutes to Complete', 'Last updated date']


category_name_matching = {
    'cross-platform': 'Cross Platform',
    'embedded-and-microcontrollers': 'Embedded and Microcontrollers',
    'mobile-graphics-and-gaming': "Mobile, Graphics, and Gaming",
    'servers-and-cloud-computing': 'Servers and Cloud Computing',
    'automotive': 'Automotive',
    'laptops-and-desktops': 'Laptops and Desktops'
}


def draftLearningPath(md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        metadata = frontmatter.load(f)
        is_draft = metadata.get('draft', False)
    return is_draft



def getLastModDate(md_file):

    ############ LastMod Date ############
    # Obtain last mod date from index's page. if none found, leave blank
    last_mod = ''
    lp_url = learn_url+md_file.replace('../content/','').replace('_index.md','').replace('.md','').lower()
    response = requests.get(lp_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        last_mod = soup.find(id='last-updated').get_text(strip=True)
        try:
            last_mod_date = datetime.strptime(last_mod, '%d %b %Y')
            last_mod = last_mod_date.strftime('%d-%b-%y')
        except ValueError:
            print(f'Error parsing date: {last_mod}')
    else:
        print(f'Error: {response.status_code} for {lp_url}')

    return last_mod


def processInstallGuide(md_file,multi_title=None):
    last_mod = getLastModDate(md_file)

    with open(md_file, 'r', encoding='utf-8') as f:
        metadata = frontmatter.load(f)

        #### Handel different titles for single vs multi IGs
        if multi_title == None:
            title = metadata.get('title', '')
            step_title = ''
        else:
            title = multi_title
            step_title = metadata.get('title', '')




        return {
            'Full URL': learn_url+md_file.replace('../content/','').replace('.md','').lower(),
            'Learning Path Title': title,
            'Weight': metadata.get('weight', ''),
            'Step Title': step_title,
            'Author': ', '.join(metadata.get('author', [])) if isinstance(metadata.get('author', ''), list) else metadata.get('author', ''),
            'Skill Level': '',
            'Subjects': '',
            'Arm IP': '',
            'OS': '',
            'Tools Software Languages': '',
            'Content Category': '',
            'Minutes to Complete': metadata.get('minutes_to_complete', ''),
            'Last updated date': last_mod
        }


# Function to extract metadata from _index.md
def extract_index_metadata(md_file,category):

    last_mod = getLastModDate(md_file)


    with open(md_file, 'r', encoding='utf-8') as f:
        metadata = frontmatter.load(f)

        ############ Cross Platform change############
        category_final = ''
        if category == 'Cross Platform':
            shared_between = metadata.get('shared_between', [])
            for cat in shared_between:
                category_final = category_final + category_name_matching[cat] + ', '
            category_final = category_final[:-2]
        
        else:
            category_final = category


        return {
            'Learning Path Title': metadata.get('title', ''),
            'Content Category': category_final,
            'Subjects': metadata.get('subjects', ''),
            'Minutes to Complete': metadata.get('minutes_to_complete', ''),
            'Skill Level': metadata.get('skilllevels', ''),
            'Last updated date': last_mod,
            'Author': ', '.join(metadata.get('author', [])) if isinstance(metadata.get('author', ''), list) else metadata.get('author', ''),
            'Arm IP': ', '.join(metadata.get('armips', [])) if isinstance(metadata.get('armips', ''), list) else metadata.get('armips', ''),
            'OS': ', '.join(metadata.get('operatingsystems', [])) if isinstance(metadata.get('operatingsystems', ''), list) else metadata.get('operatingsystems', ''),
            'Tools Software Languages': ', '.join(metadata.get('tools_software_languages', [])) if isinstance(metadata.get('tools_software_languages', ''), list) else metadata.get('tools_software_languages', '')
        }

def extract_step_metadata(md_file):
    step_url = learn_url+md_file.replace('../content/','').replace('_index.md','').lower()

    with open(md_file, 'r', encoding='utf-8') as f:
        metadata = frontmatter.load(f)
        return {
            'Weight': metadata.get('weight', ''),
            'Full URL': step_url,
            'Step Title': metadata.get('title', ''),
        }

# List to hold all rows of metadata
rows = []





#########################################
# Learning Paths
#########################################

# Iterate over all learning path categories
for cat_dir in next(os.walk(lp_base_dir))[1]:

    # Get Category from category _index.md
    with open(os.path.join(lp_base_dir, cat_dir, "_index.md"), 'r', encoding='utf-8') as f:
        metadata = frontmatter.load(f)
        category = metadata.get('title', '')


    # Iterate over all learning path directories in a category (directories one level down from a category)
    for lp_dir in next(os.walk(os.path.join(lp_base_dir, cat_dir)))[1]:

        index_md = os.path.join(lp_base_dir, cat_dir, lp_dir, '_index.md')

        if not draftLearningPath(index_md):
            print(f'Processing {cat_dir}/{lp_dir}')

            # Process the always present _index.md file in a learning path directory
            learning_path_metadata = extract_index_metadata(index_md, category)

            # Make one row for each md_file in the learning path directory whose first row is its unique URL that ends with the md_file name and the rest is the same metadata
            md_files = [f for f in os.listdir(os.path.join(lp_base_dir, cat_dir, lp_dir)) if f.endswith('.md')]
            temp_rows = []
            for md_file in md_files:
                step_metadata = extract_step_metadata(os.path.join(lp_base_dir, cat_dir, lp_dir, md_file))

                temp_rows.append({**learning_path_metadata, **step_metadata})


            # Order temp_rows by the weight key in ascending order
            temp_rows = sorted(temp_rows, key=lambda x: x['Weight'])
            for metadata in temp_rows:
                rows.append(metadata)



#########################################
# Install Guides
#########################################

# Iterate over all files in the install-guides directory
for root, ig_dirs, files in os.walk(ig_base_dir):

    ##########################
    # Process single IGs in files (like bold.md)
    ##########################
    for ig_file in files:
        if ig_file.endswith('.md'):
            if ig_file != '_index.md':

                md_file = os.path.join(root, ig_file)
                if not draftLearningPath(md_file):
                    print(f'Processing SINGLE {md_file}')
                    ig_metadata = processInstallGuide(md_file)
                    rows.append(ig_metadata)


    ##########################
    # Process multi IGs in directories (like docker/)
    ##########################
    for dir in ig_dirs:
        if dir != '_images':
            for ig_multi_file in next(os.walk(os.path.join(root, dir)))[2]:
                if ig_multi_file != '_index.md':
                    md_file = os.path.join(root, dir, ig_multi_file)
                    if not draftLearningPath(md_file):
                        print(f'Processing MULTI {md_file}')
                        ig_metadata = processInstallGuide(md_file,dir)
                        rows.append(ig_metadata)

    # Stop looping after going through multi IGs
    break

        



# Write metadata to CSV
with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
    writer.writeheader()
    writer.writerows(rows)
print(f'Metadata has been written to {output_csv}')