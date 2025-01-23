# Next steps:
#       Add 'cross platform' into category checking and addition
#       Record same for install guides
#       Verify test data & totals matches reality
#       -------- move on to individual_authors&contributors
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
weekly_in_YYYY_MMM_DD:
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
    individual_authors:                      # Dict of author stats. Source: Crawl over each LP and IG, urlize author name, and add totals
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
import argparse
import requests
from pathlib import Path
from datetime import datetime


# Set paths 
data_weekly_file_path  = Path('../data/stats_weekly_data.yml')
tests_status_file_path = Path('../data/stats_current_test_info.yml')
learning_path_dir = Path('../content/learning-paths/')
install_guide_dir = Path('../content/install-guides/')
lp_and_ig_content_dirs = ['embedded-and-microcontrollers','iot','laptops-and-desktops','servers-and-cloud-computing','mobile-graphics-and-gaming','automotive','cross-platform','install-guides']


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

def printInfo(week,test):
    print('============================================================================')
    print('New weekly entry dict appended:')
    pretty(week)
    print('============================================================================')
    print('New test entry dict overwriting:')
    pretty(test)
    print('============================================================================')


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
    ### Update 'individual_authors' area, raw number by each author.
    # Check if author already exists as key. If not, add new key
    author_urlized = urlize(author_name)
    if author_urlized in tracking_dic['individual_authors']:
        # Update number for this author
        tracking_dic['individual_authors'][author_urlized] = tracking_dic['individual_authors'][author_urlized] + 1
    else:
        # Add key to dic with 1 to their name
        tracking_dic['individual_authors'][author_urlized] = 1

    ### Update 'contributions' area, internal vs external contributions
    
    # open the contributors CSV file
    with open('../assets/contributors.csv', mode ='r')as file:
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
    weekly_authors_contributions_dic = {'individual_authors': {}, 'contributions':{'internal': 0, 'external': 0}}

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
    new_weekly_entry['content'] = weekly_count_dic
    new_weekly_entry['individual_authors'] = weekly_authors_contributions_dic['individual_authors']
    new_weekly_entry['contributions'] = weekly_authors_contributions_dic['contributions']            

def callGitHubAPI(GitHub_token,GitHub_repo_name):

    weekly_github_dic = {'issues': {}, 'github_engagement': {}}


    headers = {
        'Authorization': f'token {GitHub_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    url_issues = f'{GitHub_repo_name}issues'
    url_pulls  = f'{GitHub_repo_name}pulls'
    url_forks  = f'{GitHub_repo_name}forks'

    # Get Number of Forks
    response = requests.get(url_forks, headers=headers)
    if response.ok:
        forks = response.json()
        weekly_github_dic['github_engagement']['num_forks'] = len(forks)
    else:
        print(f'ERROR: Failed to fetch GitHub API forks: {url_forks} {response.status_code} {response.reason}')
        sys.exit(1)

    # Get Number of Pull Requests
    response = requests.get(url_pulls, headers=headers)
    if response.ok:
        pulls = response.json()
        weekly_github_dic['github_engagement']['num_prs'] = len(pulls)
    else:
        print(f'ERROR: Failed to fetch GitHub API forks: {url_pulls} {response.status_code} {response.reason}')
        sys.exit(1)

    # Get Issues information
    response = requests.get(url_issues, headers=headers)
    if response.ok:
        issues = response.json()

        # Iterate over each issue and read the state
        closed_num = 0
        time_differences = []
        for issue in issues:
            if issue['state'] == 'closed':
                # Increment number of closed
                closed_num = closed_num + 1

                # Get average time
                created_at = datetime.fromisoformat(issue['created_at'][:-1])
                closed_at = datetime.fromisoformat(issue['closed_at'][:-1])
                difference = closed_at - created_at
                time_differences.append(difference.total_seconds() / 3600)  # Convert to hours
                
            print(issue['title'],issue['state'])

        # Calculate average time to close
        if time_differences:
            avg_time_to_close = sum(time_differences) / len(time_differences)
        else:
            avg_time_to_close = 0

        # Store all stats in github dic            
        weekly_github_dic['issues']['num_issues'] = len(issues)
        weekly_github_dic['issues']['percent_closed_vs_total'] = round( (closed_num/len(issues)) * 100, 1) 
        weekly_github_dic['issues']['avg_close_time_hrs'] = round(avg_time_to_close,1)
           
    else:
        print(f'ERROR: Failed to fetch GitHub API issues:  {url_issues} {response.status_code} {response.reason}')
        sys.exit(1)
    

    # Assign to main file
    new_weekly_entry['issues'] = weekly_github_dic['issues']
    new_weekly_entry['github_engagement'] = weekly_github_dic['github_engagement']


def main():
    global data_weekly_file_path, tests_status_file_path, learning_path_dir, install_guide_dir, date_today, new_weekly_entry, new_tests_entry

    # Read in params needed for reading GitHub API
    arg_parser = argparse.ArgumentParser(description='Update Stats')
    arg_parser.add_argument('-t','--token', help='GitHub personal access token', required=True)
    arg_parser.add_argument('-r','--repo', help='GitHub repository name', required=True)
    args = arg_parser.parse_args()



    # Read in data file as python dict
    existing_weekly_dic = yaml.safe_load(data_weekly_file_path.read_text())
    existing_tests_dic  = yaml.safe_load(tests_status_file_path.read_text())

    # Structure new data formats:
    new_weekly_entry = { 
        "a_date": date_today,
        "content": {},
        "individual_authors": {},
        "contributions": {},
        "issues": {},
        "github_engagement": {}    
    }

    new_tests_entry = {
        "summary": {},
        "sw_categories":{}
    }


    # Get new stats, filling in new stat dictionaries:
    iterateContentIndexMdFiles()
    callGitHubAPI(args.token, args.repo)

    

    # Debug prints in flow
    printInfo(new_weekly_entry,new_tests_entry)

    # Update/replace yaml files

    ### Weekly
    # if weekly dict is empty, create key
    if not existing_weekly_dic:
        print('no existing dic, starting from scratch.')
        existing_weekly_dic = [new_weekly_entry]
    # Otherwise append it
    else:  
        print('weekly data exists...checking to see if date exists.')
        # Check if date already a key in there
        exists=False
        for dic in existing_weekly_dic:
            if date_today == dic["a_date"]:
                print('date today included, don"t save')
                exists=True
                break
        if not exists:
            print('date doesn"t exist, appending data')
            existing_weekly_dic.append(new_weekly_entry)

    # Alter existing dic to be a list of dates for easier processing:
    with open(data_weekly_file_path, 'w') as outfile:
        print('printing weekly dict format, and dumping into this file: ')
        print(outfile)
        print(existing_weekly_dic)
        yaml.dump(existing_weekly_dic, outfile, default_flow_style=False)

    ### Tests
    existing_tests_dic = new_tests_entry
    with open(tests_status_file_path, 'w') as outfile:
        yaml.dump(existing_tests_dic, outfile, default_flow_style=False)

if __name__ == "__main__":
    main()
