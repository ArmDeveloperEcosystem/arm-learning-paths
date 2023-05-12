# Next steps:
#       Add 'cross platform' into category checking and addition
#       Record same for install guides
#       Verify test data & totals matches reality
#       -------- move on to authors&contributors
#       -------- move on to GitHub API



'''
Goal: Every week, update the stats_data.yml file automatically by reading the current state and GitHub API

Steps:
    1) Read in stats_data.yml as a python dict
    2) Verify we can read in new stats, via a function for each datapoint to log
        2a) Directory structure read
        2b) GitHub API obtain data
    3) If we have new data, append to stats_data.yml. If not, fail script to notify GitHub folks
'''

'''
2023-Mar-03:                    # Date, updated weekly, in YYYY-MMM-DD format
  content:                      # Dict of content related stats. Source: # of LP in each directory
      total: 33                 # raw sum of all all below
      ucontroller: 5            
      embedded: 2               
      desktop: 1                
      server: 10                
      mobile: 3                 
      cross: 2                  # Number of learning paths in cross-platform area; for awareness
      install_guides: 10        
  authors:                      # Dict of author stats. Source: Crawl over each LP and IG, urlize author name, and add totals
      jason_andrews: 24
      pareena_verma: 22
      ronan_synnott: 15
      florent_lebeau: 9
      jane_doe: 2
      john_smith: 2
  contributions:                # Dict of contribution stats. Source: Cross-match found author names in LPs and IGs with 'contributors.csv' to identify them as internal (with company Arm) or external (all others)
      internal: 70
      external: 4
  issues:                               # Dict of GitHub issues raised in this repo. Source: GitHub API
      avg_close_time_hrs: 42            
      percent_closed_vs_total: 90.5
      num_issues: 66
  github_engagement:                    # Dict of GitHub repo webpage engagement numbers. Source: GitHub API
      num_prs: 34
      num_forks: 20
'''


'''
---
summary:                                # Basic summary of tests in this site. Source: adding numbers when iterating over sw_categories below
  content_total: 30             
  content_with_tests_enabled: 10        # Will match the number of learning paths
  content_with_all_tests_passing: 9


sw_categories:                             # Dict of content test status. Source: Iterate over each LP category and IGs _index.md files to scrape data and store in this one place.
  server:
    intrinsics:
      title: Integrate Intrinsics here
      tests_and_status: 
        - amd64/ubuntu:latest: passed
        - arm64v8/ubuntu:latest: passed
    avh_cicd:
      title: AVH Title
      tests_and_status: 
        - RPi3:latest: passed
'''



import os
import sys
import csv
import yaml
from pathlib import Path
from datetime import datetime


# Set paths 
data_weekly_file_path  = Path('../content/stats/stats_weekly_data.yml')
tests_status_file_path = Path('../content/stats/stats_current_test_info.yml')
learning_path_dir = Path('../content/learning-paths/')
install_guide_dir = Path('../content/install-guides/')
lp_and_ig_content_dirs = ['microcontrollers','embedded-systems','laptops-and-desktops','servers-and-cloud-computing','smartphones-and-mobile','cross-platform','install-guides']


# Obtain today's date in YYYY-MM-DD
date_today =  datetime.now().strftime("%Y-%m-%d")

# Set global vars for processing ease
new_weekly_entry = {}
new_tests_entry = {}

#############################################################################
#############################################################################


def pretty(d, indent=0):
   for key, value in d.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))

def urlize(in_str):
    # Replacate Hugo urlize function to make it easier to process strings for consistent analysis.
        # ' ' -> '-'
        # capitals -> lowercase
    return in_str.replace(' ','-').lower()

def mdToMetadata(md_file_path):
    metadata_text = ""
    content_text  = "" 
    inMetadata = False

    # Remove last '---' to propery read in yaml metadata component of .md file
    with open(md_file_path, encoding="utf8") as f:
        for line in (f.readlines()):
            if ('---' in line) and inMetadata:
                break                # go on when needed to gather content text
            elif ('---' in line) and (not inMetadata):
                inMetadata = True
            metadata_text += line

    # Load yaml
    metadata_dic = yaml.safe_load(metadata_text)
    return metadata_dic

def authorAdd(author_name,tracking_dic):
    ### Update 'authors' area, raw number by each author.
    # Check if author already exists as key. If not, add new key
    author_urlized = urlize(author_name)
    if author_urlized in tracking_dic['authors']:
        # Update number for this author
        tracking_dic['authors'][author_urlized] = tracking_dic['authors'][author_urlized] + 1
    else:
        # Add key to dic with 1 to their name
        tracking_dic['authors'][author_urlized] = 1

    ### Update 'contributions' area, internal vs external contributions
    
    # open the contributors CSV file
    with open('../contributors.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for line in csvFile:
            company = line[1]
            # If author in the line, check if they work at Arm or not, and increment contributions number for internal or external
            if author_name in line:
                if company == 'Arm':
                    tracking_dic['contributions']['internal'] = tracking_dic['contributions']['internal'] + 1
                else:
                    tracking_dic['contributions']['external'] = tracking_dic['contributions']['external'] + 1
    
    return tracking_dic

def iterateContentIndexMdFiles():
    # set variables to track as we iterate
        # weekly -> content:
    weekly_count_dic = {'total': 0, 'cross-platform': 0,   'install-guides': 0}
    for category in lp_and_ig_content_dirs:
        weekly_count_dic[category] = 0

        # weekly -> authors AND contributions
    weekly_authors_contributions_dic = {'authors': {}, 'contributions':{'internal': 0, 'external': 0}}

        # tests -> summary:
    content_total = 0
    content_with_tests_enabled = 0
    content_with_all_tests_passing = 0

    # start iterating over all sw_categories including install guides
    for category in lp_and_ig_content_dirs:
        new_tests_entry['sw_categories'][category] = {}        # Add new category key

        # Get list of content to iterate over.
        content_in_dir = []
        if category != 'install-guides': # Learning Path processing
            category_dir = learning_path_dir.parent / (learning_path_dir.name + '/' + category)  
            content_in_dir = [ Path(f.path+"/_index.md") for f in os.scandir(category_dir) if f.is_dir() ]

        else: # Install Guide Processing.   ### Get array of install guide files (everything that IS NOT an _index.md file; so count docker_desktop.md seperate than docker_woa.md under docker dir)
            for ig in os.scandir(install_guide_dir):
                if not ig.is_dir():
                    # Append normal .md files
                    if ig.name != '_index.md': # ignore top level file
                        content_in_dir.append(Path(ig))
                else: # iterate over multi-layer files
                    if ig.name != '_images': # ignore image directory
                        for ig_part in os.scandir(ig): #iterate over all files in multiparge ig dir
                            if ig_part.name != '_index.md': # ignore top level file
                                content_in_dir.append(Path(ig_part))




        # Iterate over all content files
        for content_index_file in content_in_dir:
            content_metadic = mdToMetadata(content_index_file)
            
            # If draft, ignore by continuing right away to the next file
            try:
                if content_metadic['draft']:
                    continue
            except:
                pass
            # If the example learning path, continue
            if '_example-learning-path' in str(content_index_file.parent):
                continue


            # Add to content total (both tests and weekly places for redundency sake)
            weekly_count_dic['total'] = weekly_count_dic['total'] + 1
            content_total = content_total + 1
            # Add to category total
            weekly_count_dic[category] = weekly_count_dic[category] + 1

            ######### AUTHOR info
            weekly_authors_contributions_dic = authorAdd(content_metadic['author_primary'],weekly_authors_contributions_dic)
            

            # Record entry in test file
            try:
                if content_metadic['test_maintenance']: # if actively being tested, record as such
                    # Record test
                    content_with_tests_enabled = content_with_tests_enabled + 1

                    # Add an entry for this dir, with title and test status keys
                    if category == 'install-guides': # Install Guides, shorthand name is the .md file name itself (for multi-part installs, still the individual file name; dir name is ignored)
                        content_dir_name = content_index_file.stem
                    else: # Learning Paths, shorthand name is the directory
                        content_dir_name = os.path.basename(os.path.dirname(content_index_file))

                    new_tests_entry['sw_categories'][category][content_dir_name] = {}
                    new_tests_entry['sw_categories'][category][content_dir_name]['readable_title'] = content_metadic['title']
                    new_tests_entry['sw_categories'][category][content_dir_name]['tests_and_status'] = []
                    all_tests_passing = True # Default to true, change if one is false
                    for i, item in enumerate(content_metadic['test_status']):
                        # Record test status (possibily multiple)
                        new_tests_entry['sw_categories'][category][content_dir_name]['tests_and_status'].append({
                            content_metadic['test_images'][i]: content_metadic['test_status'][i]
                        })   
                        if item != 'passed':
                            all_tests_passing = False
                    # Add if tests are passing count if all tests under this content are passing
                    if all_tests_passing:
                        content_with_all_tests_passing = content_with_all_tests_passing + 1                     
            except:
                pass

    # Update all totals for tests passing or not into the summary 
    new_tests_entry['summary']['content_total'] = content_total
    new_tests_entry['summary']['content_with_tests_enabled'] = content_with_tests_enabled
    new_tests_entry['summary']['content_with_all_tests_passing'] = content_with_all_tests_passing

    # Update stats
    new_weekly_entry[date_today]['content'] = weekly_count_dic
    new_weekly_entry[date_today]['authors'] = weekly_authors_contributions_dic['authors']
    new_weekly_entry[date_today]['contributions'] = weekly_authors_contributions_dic['contributions']            

def callGitHubAPI():
    pass


def main():
    global data_weekly_file_path, tests_status_file_path, learning_path_dir, install_guide_dir, date_today, new_weekly_entry, new_tests_entry

    # Read in data file as python dict
    existing_weekly_dic = yaml.safe_load(data_weekly_file_path.read_text())
    existing_tests_dic  = yaml.safe_load(tests_status_file_path.read_text())

    # Structure new data formats:
    new_weekly_entry = { date_today: {
        "content": {},
        "authors": {},
        "contributions": {},
        "issues": {},
        "github_engagement": {}
        }                    
    }

    new_tests_entry = {
        "summary": {},
        "sw_categories":{}
    }


    # Get new stats, filling in new stat dictionaries:
    iterateContentIndexMdFiles()
    callGitHubAPI()


    # Update/replace yaml files
    '''
    existing_weekly_dic.update()
    new_tests_entry.overwrite tests_status_file_path

    '''
    pretty(new_weekly_entry)
    #pretty(new_tests_entry)
    with open('data.yml', 'w') as outfile:
        yaml.dump(new_tests_entry, outfile, default_flow_style=False)


if __name__ == "__main__":
    main()
