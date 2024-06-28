import os
import sys
import yaml
from pathlib import Path
import argparse

def mdToMetadata(md_file_path):
    metadata_text = ""
    content_text  = "" 
    inMetadata = False

    # print the files so if 1 has an error, it can be fixed
    #print(md_file_path)

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




def byCount(element):
    # return the only value in dict, which is the count
    return element[next(iter(element))]
    
def Alphabetical(element):
    # return the only value in dict, which is the name
    return next(iter(element)).lower()


def updateFiltersInIndexMD(main_category):
    global status_dic, dir_relative_of_learning_paths
    category_index_md_file = dir_relative_of_learning_paths+main_category+"/_index.md"

    # Read in _index.md of Category as yml
    metadata_dic = mdToMetadata(category_index_md_file)


    '''
    # Define what to add
    updated_category_filters = {'subjects_filter': [], 'operatingsystems_filter': [], 'tools_software_languages_filter': []}
    
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
    #   TSLs
    all_existing_TSLs = status_dic['tools_software_languages'][main_category]
    for tsl in all_existing_TSLs:
        updated_category_filters['tools_software_languages_filter'].append(tsl)       
    # Replace category filters in existing metadata
    metadata_dic['subjects_filter'] = updated_category_filters['subjects_filter']
    metadata_dic['operatingsystems_filter'] = updated_category_filters['operatingsystems_filter']
    metadata_dic['tools_software_languages_filter'] = updated_category_filters['tools_software_languages_filter']
    '''

    '''
    subjects_filter:  
        - ["CI-CD", 8]
    '''
    
    
    to_iterate = ['subjects','operatingsystems','tools_software_languages']
    if main_category == "servers-and-cloud-computing":
        to_iterate.append('cloud_service_providers')

    for filter_name in to_iterate:
        all_existing_filters = status_dic[filter_name][main_category]
        final_filter_with_counts = []
        # Fill out options in filters
        for f_option in all_existing_filters:
            if 'allowed' in all_existing_filters[f_option]: 
                if all_existing_filters[f_option]['allowed']:
                    final_filter_with_counts.append({f_option:all_existing_filters[f_option]['count']})
            else:
                final_filter_with_counts.append({f_option:all_existing_filters[f_option]['count']})

        # Order the filters by count, high to low (not working, don't know why.)
        final_filter_with_counts.sort(key=Alphabetical)   # key=Alphabetical or (reverse=True,key=byCount)

            # code when it was a dict: #final_filter_with_counts =  dict(sorted(final_filter_with_counts.items(), key=lambda x:x[1][1], reverse=True))
        
        # Replace category filters in existing metadata, ordering at the same time
        metadata_dic[filter_name+'_filter'] = final_filter_with_counts


    # re-write the _index.md file, including '---' in the front and back of it
    with open(category_index_md_file, "w") as f:
        f.write('---\n')
        yaml.dump(metadata_dic, f, sort_keys=False) # dump, keeping order that we specified (sort_keys=False)
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

def printToolsSoftwareLanguagesReport():
    global status_dic
    print()
    print()
    print('='*50)
    print('Tools Software Languages per Category')
    all_tsl = []

    for main_category in status_dic['tools_software_languages']:
        cat_dic = status_dic['tools_software_languages'][main_category]
        print('     '+main_category)

        # sort by alphabetical order
        tsl_dic=  dict(sorted(cat_dic.items(), key=lambda x:x[0].lower()))
        for tsl in tsl_dic:
            if tsl not in all_tsl:
                all_tsl.append(tsl)
            print('         '+tsl+' - '+str(tsl_dic[tsl]['count']))
            for lp in tsl_dic[tsl]['learning-path-titles']:
                print('            '+lp)

    print('-'*50)
    print('Tools Software Languages - All')
    for tsl in sorted(all_tsl, key=str.casefold):
        print('        '+tsl)
    print('='*50)
    print()
    print() 

def printCSPsReport():
    global status_dic, dic_allow_list
    print()
    print()
    print('='*50)
    print('Cloud Service Providers')
    for main_category in status_dic['cloud_service_providers']:
        cat_dic = status_dic['cloud_service_providers'][main_category]

        print('     '+main_category)
        print('         '+'Allowed')
        for csp in cat_dic:
            if cat_dic[csp]['allowed']:
                print('             '+str(cat_dic[csp]['count'])+': '+csp)
        print('         '+'Not Allowed')
        for csp in cat_dic:
            if not cat_dic[csp]['allowed']:
                print('             '+csp+'     '+str(cat_dic[csp]['count']))
                for learning_paths in cat_dic[csp]['learning-path-titles']:
                    print('                 '+learning_paths)
        print('         '+'Unused')
        
        for allowed_OS in dic_allow_list["cloud_service_providers"]:
            if allowed_OS not in cat_dic:
                print('             '+allowed_OS)
        print()
    print('='*50)
    print()
    print()







def addSubjectsToStatusDict():
    global status_dic, learning_path_metadata
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

    return status_dic

def addOperatingSystemsToStatusDict():
    global status_dic, learning_path_metadata
    operatingsystems = learning_path_metadata['operatingsystems']
    if operatingsystems is not None:
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

    return status_dic

def addToolsSoftwareLanguagesToStatusDict():
    global status_dic, learning_path_metadata
    tools_software_languages = learning_path_metadata['tools_software_languages']
    if tools_software_languages is not None:
        for tsl in tools_software_languages:
            if tsl not in status_dic['tools_software_languages'][dir_main_category]:
                # create subject key in dic
                status_dic['tools_software_languages'][dir_main_category][tsl] = {}            
                status_dic['tools_software_languages'][dir_main_category][tsl]['count']                = 1                # make count one
                status_dic['tools_software_languages'][dir_main_category][tsl]['learning-path-titles'] = [learning_path_metadata['title']]   # create list with title
            else:
                status_dic['tools_software_languages'][dir_main_category][tsl]['count']               += 1                # increase count by one
                status_dic['tools_software_languages'][dir_main_category][tsl]['learning-path-titles'].append(learning_path_metadata['title'])   # add title to list

    return status_dic


def addCloudServiceProvidersToStatusDict():
    global status_dic, learning_path_metadata
    if 'cloud_service_providers' in learning_path_metadata: # since not all LPs have this filtering mechanism, need this check to avoid errors
        cloud_service_providers = learning_path_metadata['cloud_service_providers']
        if cloud_service_providers is not None:
            if cloud_service_providers not in status_dic['cloud_service_providers'][dir_main_category]:
                # create subject key in dic
                status_dic['cloud_service_providers'][dir_main_category][cloud_service_providers] = {}
                # check if in allow list
                if cloud_service_providers in dic_allow_list["cloud_service_providers"]:
                    status_dic['cloud_service_providers'][dir_main_category][cloud_service_providers]['allowed']          = True              
                else:
                    status_dic['cloud_service_providers'][dir_main_category][cloud_service_providers]['allowed']          = False              
                status_dic['cloud_service_providers'][dir_main_category][cloud_service_providers]['count']                = 1                # make count one
                status_dic['cloud_service_providers'][dir_main_category][cloud_service_providers]['learning-path-titles'] = [learning_path_metadata['title']]   # create list with title
            else:
                status_dic['cloud_service_providers'][dir_main_category][cloud_service_providers]['count']               += 1                # increase count by one
                status_dic['cloud_service_providers'][dir_main_category][cloud_service_providers]['learning-path-titles'].append(learning_path_metadata['title'])   # add title to list

    return status_dic



def checker(report = 'all', update_md_files = False):
    global status_dic, dir_relative_of_learning_paths, dic_allow_list, learning_path_metadata, dir_main_category

    #
    # -1
    # Parse arguments if used as a standalone file
    '''
    arg_parser = argparse.ArgumentParser(description='Filter updater & Checker.', prefix_chars='-')
    arg_parser.add_argument('-u', '--update-md-files', action='store_true', help='Update .md index files filtering information.')
    arg_parser.add_argument('-r', '--report', action='store', help='Report only specific information. Default is none. Set to "all", "subjects", "oses", "csps", or "tools-software-languages"')

    args = arg_parser.parse_args()
    update_md_files = args.update_md_files
    report = args.report
    '''

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
    #       servers-and-cloud-computing:
    #           CI-CD:
    #               allowed: True
    #               count: 2...
    #               learning-path-titles: ['title one', 'title two', ...]
    # }

    status_dic = {
        'subjects':{},
        'operatingsystems':{},
        'tools_software_languages': {},
        'cloud_service_providers': {}
        }

    # iterate over main categories as defined in the dic allow list (embedded, mobile, etc.)
    for dir_main_category in dic_allow_list["subjects"]:
    
        # Initalize status_dic
        status_dic['subjects'][dir_main_category] = {}
        status_dic['operatingsystems'][dir_main_category] = {}
        status_dic['tools_software_languages'][dir_main_category] = {}
        if dir_main_category == "servers-and-cloud-computing":
            status_dic['cloud_service_providers'][dir_main_category] = {}
            

        # iterate over every directory in this category
        learning_paths_in_category = [ Path(f.path+"/_index.md") for f in os.scandir(dir_relative_of_learning_paths+dir_main_category) if f.is_dir() ]
        for learning_path_index_file in learning_paths_in_category:
            learning_path_metadata = mdToMetadata(learning_path_index_file)

            # Update filters
            status_dic = addSubjectsToStatusDict()
            status_dic = addOperatingSystemsToStatusDict()
            status_dic = addToolsSoftwareLanguagesToStatusDict()
            if dir_main_category == "servers-and-cloud-computing":
                status_dic = addCloudServiceProvidersToStatusDict()

    #
    # 2.5
    # Add cross-platform filters
    # Iterate through each LP in cross-platform
    dir_main_category = 'cross-platform'
    learning_paths_in_category = [ Path(f.path+"/_index.md") for f in os.scandir(dir_relative_of_learning_paths+dir_main_category) if f.is_dir() ]
    for learning_path_index_file in learning_paths_in_category:
        # parse into metadata, excluding paths that start with an _ (such as the example learning path)
        if not "_" == os.path.basename(os.path.dirname(learning_path_index_file))[0]:
            learning_path_metadata = mdToMetadata(learning_path_index_file)
            # Iterate over the categories the LP needs to fit into (shared_between list)
            for dir_main_category in learning_path_metadata['shared_between']:
                status_dic = addSubjectsToStatusDict()
                status_dic = addOperatingSystemsToStatusDict()
                status_dic = addToolsSoftwareLanguagesToStatusDict()
                if dir_main_category == "servers-and-cloud-computing":
                    status_dic = addCloudServiceProvidersToStatusDict()

    #
    # 3
    # Report numbers
    if report == 'all':
        printSubjectReport()
        printOSesReport()
        printCSPsReport()
        printToolsSoftwareLanguagesReport()
    elif report == 'subjects':
        printSubjectReport()
    elif report == 'oses':
        printOSesReport()
    elif report == 'csps':
        printCSPsReport()
    elif report == 'tools-software-languages':
        printToolsSoftwareLanguagesReport()

    #
    # 4
    # Overwrite filters.yml file with existing acceptable filters under each learning path
    if update_md_files:
        print('Filter updates:')
        print('    Overwriting category md files now...')
        for main_category in dic_allow_list["subjects"]:
            status = updateFiltersInIndexMD(main_category)
            print("         "+main_category+"/_index.md updating complete")      
    else:
        print('No overwriting specifed with --update-md-files flag. Exiting.')
        print()
        sys.exit(0)

'''
if __name__ == "__main__":
    checker()
'''