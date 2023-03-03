import os
import sys
import yaml
from pathlib import Path


def mdToMetadata(md_file_path):
    metadata_text = ""
    content_text  = "" 
    inMetadata = False

    # Remove last '---' to propery read in yaml metadata component of .md file
    with open(md_file_path) as f:
        for line in (f.readlines()):
            if ('---' in line) and inMetadata:
                break                # go on when needed to gather content text
            elif ('---' in line) and (not inMetadata):
                inMetadata = True
            metadata_text += line

    # Load yaml
    metadata_dic = yaml.safe_load(metadata_text)
    return metadata_dic



def updateClosedCategoryFiltersInIndexMD(main_category):
    global status_dic, dir_relative_of_learning_paths
    category_index_md_file = dir_relative_of_learning_paths+main_category+"/_index.md"

    # Read in _index.md of Category as yml
    metadata_dic = mdToMetadata(category_index_md_file)

    # Define what to add
    updated_category_filters = {'subjects_filter': [], 'operatingsystems_filter': []}
    
    # Fill out filters dic
    #   SUBJECTS
    all_existing_subjects = status_dic['subjects'][main_category]
    for subject in all_existing_subjects:
        if all_existing_subjects[subject]['allowed']:
            updated_category_filters['subjects_filter'].append(subject)
    #   OSes
    all_existing_OSes = status_dic['operatingsystems'][main_category]
    for operatingsystem in all_existing_OSes:
        if all_existing_OSes[operatingsystem]['allowed']:
            updated_category_filters['operatingsystems_filter'].append(operatingsystem)    


    # Replace category filters in existing metadata
    metadata_dic['subjects_filter'] = updated_category_filters['subjects_filter']
    metadata_dic['operatingsystems_filter'] = updated_category_filters['operatingsystems_filter']

    # re-write the _index.md file, including '---' in the front and back of it
    with open(category_index_md_file, "w") as f:
        f.write('---\n')
        yaml.dump(metadata_dic, f)
        f.write('---\n')

    return True








def updateOpenFiltersInIndexMD():
    global status_dic, dir_relative_of_learning_paths
    crossplatform_index_md_file = dir_relative_of_learning_paths+"cross-platform/_index.md"

    # Read in _index.md of Category as yml
    metadata_dic = mdToMetadata(crossplatform_index_md_file)

    # Define what to add
    updated_category_filters = {'softwares_filter': [], 'tools_filter': []}

    # Fill out filters dic
    #   SOFTWARES
    all_existing_sw = status_dic['softwares']
    for sw in all_existing_sw:
        # urlize and place them in the same area if needed
        #sw = sw.lower().replace(' ','-')
        #if sw not in updated_category_filters['softwares_filter']:
        if sw != 'None':
            updated_category_filters['softwares_filter'].append(sw)

    #   OSes
    all_existing_t = status_dic['tools']
    for t in all_existing_t:
        # urlize and place them in the same area if needed
        #t = t.lower().replace(' ','-')
        #if t not in updated_category_filters['tools_filter']:
        if t != 'None':
            updated_category_filters['tools_filter'].append(t)


    # Replace category filters in existing metadata
    metadata_dic['softwares_filter'] = updated_category_filters['softwares_filter']
    metadata_dic['tools_filter'] = updated_category_filters['tools_filter']

    # re-write the _index.md file, including '---' in the front and back of it
    with open(crossplatform_index_md_file, "w") as f:
        f.write('---\n')
        yaml.dump(metadata_dic, f)
        f.write('---\n')

    return True






def printSubjectReport():
    global status_dic, dic_allow_list
    print()
    print()
    print('='*50)
    print('Subjects')
    for main_category in status_dic['subjects']:
        cat_dic = status_dic['subjects'][main_category]

        print('     '+main_category)
        print('         '+'Allowed')
        for subject in cat_dic:
            if cat_dic[subject]['allowed']:
                print('             '+str(cat_dic[subject]['count'])+': '+subject)
        print('         '+'Not Allowed')
        for subject in cat_dic:
            if not cat_dic[subject]['allowed']:
                print('             '+subject+'     '+str(cat_dic[subject]['count']))
                for learning_paths in cat_dic[subject]['learning-path-titles']:
                    print('                 '+learning_paths)
        print('         '+'Unused')
        
        for allowed_subject in dic_allow_list["subjects"][main_category]:
            if allowed_subject not in cat_dic:
                print('             '+allowed_subject)
        print()
    print('='*50)
    print()
    print()



def printOSesReport():
    global status_dic, dic_allow_list
    print()
    print()
    print('='*50)
    print('Operating Systems')
    for main_category in status_dic['operatingsystems']:
        cat_dic = status_dic['operatingsystems'][main_category]

        print('     '+main_category)
        print('         '+'Allowed')
        for operatingsystem in cat_dic:
            if cat_dic[operatingsystem]['allowed']:
                print('             '+str(cat_dic[operatingsystem]['count'])+': '+operatingsystem)
        print('         '+'Not Allowed')
        for operatingsystem in cat_dic:
            if not cat_dic[operatingsystem]['allowed']:
                print('             '+operatingsystem+'     '+str(cat_dic[operatingsystem]['count']))
                for learning_paths in cat_dic[operatingsystem]['learning-path-titles']:
                    print('                 '+learning_paths)
        print('         '+'Unused')
        
        for allowed_OS in dic_allow_list["operatingsystems"]:
            if allowed_OS not in cat_dic:
                print('             '+allowed_OS)
        print()
    print('='*50)
    print()
    print()



def printSoftwaresReport():
    global status_dic
    print()
    print()
    print('='*50)
    print('Softwares')
    # sort by alphabetical order
    sw_dic=  dict(sorted(status_dic['softwares'].items(), key=lambda x:x[0].lower()))
    for sw in sw_dic:
        print('    '+sw+' - '+str(sw_dic[sw]['count']))
        for lp in sw_dic[sw]['learning-path-titles']:
            print('        '+lp)

    print('='*50)
    print()
    print() 

def printToolsReport():
    global status_dic
    print()
    print()
    print('='*50)
    print('Tools')
    # sort by alphabetical order
    t_dic=  dict(sorted(status_dic['tools'].items(), key=lambda x:x[0].lower()))
    for t in t_dic:
        print('    '+t+' - '+str(t_dic[t]['count']))
        for lp in t_dic[t]['learning-path-titles']:
            print('        '+lp)

    print('='*50)
    print()
    print() 



def checker(report = 'all', update_md_files = False):
    global status_dic, dir_relative_of_learning_paths, dic_allow_list

    #
    # 0
    # Initalize variables
    file_yml_allow_list_filters = str(Path((__file__)).parent.resolve())+"/closed-filters-allow-list.yml"
    dir_relative_of_learning_paths = str(Path((__file__)).parent.resolve())+"/../content/learning-paths/"

    #
    # 1
    # Load allow list dictionary
    dic_allow_list = yaml.safe_load(Path(file_yml_allow_list_filters).read_text())

    #
    # 2
    # Loop over all content, read into new dic
    # { subjects: 
    #       server-and-cloud:
    #           CI-CD:
    #               allowed: True
    #               count: 2...
    #               learning-path-titles: ['title one', 'title two', ...]
    # }

    status_dic = {
        'subjects':{},
        'operatingsystems':{},
        'softwares': {},
        'tools': {}
        }

    # iterate over main categories as defined in the dic allow list (embedded, mobile, etc.)
    for dir_main_category in dic_allow_list["subjects"]:
    
        # Initalize status_dic
        status_dic['subjects'][dir_main_category] = {}
        status_dic['operatingsystems'][dir_main_category] = {}

        # iterate over every directory in this category
        learning_paths_in_category = [ Path(f.path+"/_index.md") for f in os.scandir(dir_relative_of_learning_paths+dir_main_category) if f.is_dir() ]
        for learning_path_index_file in learning_paths_in_category:
            learning_path_metadata = mdToMetadata(learning_path_index_file)

            # Analyze Learning Path subjects, update status_dic
            subject = learning_path_metadata['subjects']
            if subject not in status_dic['subjects'][dir_main_category]:
                # create subject key in dic
                status_dic['subjects'][dir_main_category][subject] = {}
                # check if in allow list
                if subject in dic_allow_list["subjects"][dir_main_category]:
                    status_dic['subjects'][dir_main_category][subject]['allowed']          = True              
                else:
                    status_dic['subjects'][dir_main_category][subject]['allowed']          = False              
                status_dic['subjects'][dir_main_category][subject]['count']                = 1                # make count one
                status_dic['subjects'][dir_main_category][subject]['learning-path-titles'] = [learning_path_metadata['title']]   # create list with title
            else:
                status_dic['subjects'][dir_main_category][subject]['count']               += 1                # increase count by one
                status_dic['subjects'][dir_main_category][subject]['learning-path-titles'].append(learning_path_metadata['title'])   # add title to list

            # Analyze Learning Path operatingsystems, update status_dic
            operatingsystems = learning_path_metadata['operatingsystems']
            if not operatingsystems:
                operatingsystems = ['None']
            for opsys in operatingsystems:
                if opsys not in status_dic['operatingsystems'][dir_main_category]:
                    # create subject key in dic
                    status_dic['operatingsystems'][dir_main_category][opsys] = {}
                    # check if in allow list
                    if opsys in dic_allow_list["operatingsystems"]:
                        status_dic['operatingsystems'][dir_main_category][opsys]['allowed']          = True              
                    else:
                        status_dic['operatingsystems'][dir_main_category][opsys]['allowed']          = False              
                    status_dic['operatingsystems'][dir_main_category][opsys]['count']                = 1                # make count one
                    status_dic['operatingsystems'][dir_main_category][opsys]['learning-path-titles'] = [learning_path_metadata['title']]   # create list with title
                else:
                    status_dic['operatingsystems'][dir_main_category][opsys]['count']               += 1                # increase count by one
                    status_dic['operatingsystems'][dir_main_category][opsys]['learning-path-titles'].append(learning_path_metadata['title'])   # add title to list

            # Analyze Learning Path software, update status_dic
            softwares = learning_path_metadata['softwares']
            if not softwares:
                softwares = ['None']
            for sw in softwares:
                if sw not in status_dic['softwares']:
                    # create subject key in dic
                    status_dic['softwares'][sw] = {}            
                    status_dic['softwares'][sw]['count']                = 1                # make count one
                    status_dic['softwares'][sw]['learning-path-titles'] = [learning_path_metadata['title']]   # create list with title
                else:
                    status_dic['softwares'][sw]['count']               += 1                # increase count by one
                    status_dic['softwares'][sw]['learning-path-titles'].append(learning_path_metadata['title'])   # add title to list

            # Analyze Learning Path tools, update status_dic
            tools = learning_path_metadata['tools']
            if not tools:
                tools = ['None']
            for t in tools:
                if t not in status_dic['tools']:
                    # create subject key in dic
                    status_dic['tools'][t] = {}            
                    status_dic['tools'][t]['count']                = 1                # make count one
                    status_dic['tools'][t]['learning-path-titles'] = [learning_path_metadata['title']]   # create list with title
                else:
                    status_dic['tools'][t]['count']               += 1                # increase count by one
                    status_dic['tools'][t]['learning-path-titles'].append(learning_path_metadata['title'])   # add title to list


    #
    # 3
    # Report numbers
    if report == 'all':
        printSubjectReport()
        printOSesReport()
    elif report == 'subjects':
        printSubjectReport()
    elif report == 'oses':
        printOSesReport()
    elif report == 'softwares':
        printSoftwaresReport()
    elif report == 'tools':
        printToolsReport()

    #
    # 4
    # Overwrite filters.yml file with existing acceptable filters under each learning path
    if update_md_files:
        print('CLOSED filter updates:')
        print('    Overwriting category md files now...')
        for main_category in dic_allow_list["subjects"]:
            status = updateClosedCategoryFiltersInIndexMD(main_category)
            print("         "+main_category+"/_index.md updating complete")

        print('OPEN filter updates:')
        print('    Overwriting cross-platform md file now...')
        status = updateOpenFiltersInIndexMD()
        print("     /cross-platform/_index.md updating complete")        
    else:
        print('No overwriting specified with --update-md-files flag. Exiting.')
        print()
        sys.exit(0)
