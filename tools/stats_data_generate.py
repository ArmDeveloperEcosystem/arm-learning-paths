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
  content:                      # Dict of content related stats. Source: # of LP in each directory + cross-platform LPs (should be identical to search number)
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
summary:                        # Basic summary of tests in this site. Source: adding numbers when iterating over categories below
  content_total: 30             
  tests_enabled_total: 10
  tests_passing: 9


categories:                     # Dict of content test status. Source: Iterate over each LP category and IGs _index.md files to scrape data and store in this one place.
  server:
    intrinsics:
      enabled: true
      status: 
        - test1:
          framework: Docker
          target: amd64/ubuntu:latest
          status: passed
        - test2:
          framework: Docker
          target: arm64v8/ubuntu:latest
          status: passed
    avh_cicd:
      enabled: true
      status: 
        - test1:
          framework: AVH
          target: RPi3:latest
          status: passed
    csp:
      enabled: false            # If no tests enabled, don't input a 'status'

'''



import os
import sys
import yaml
from pathlib import Path
from datetime import datetime


# Set paths 
data_weekly_file_path  = Path('../content/stats/stats_weekly_data.yml')
tests_status_file_path = Path('../content/stats/stats_current_test_info.yml')
learning_path_dir = Path('../content/learning-paths/')
install_guide_dir = Path('../content/install-guides/')

# Obtain today's date in YYYY-MM-DD
date_today =  datetime.now().strftime("%Y-%m-%d")

# Set global vars for processing ease
new_weekly_entry = {}
new_tests_entry = {}

def iterateContentIndexMdFiles():
    # set variables to track as we iterate
        # weekly -> content:
    ucontroller = 0
    embedded = 0
    desktop = 0
    server = 0
    mobile = 0
    cross = 0
    install_guides = 0
        # tests -> summary:
    content_total = 0
    tests_enabled_total = 0
    tests_passing = 0

    # start iterating over all LP categories (IGs next)
    for root, dirs, files in os.walk(learning_path_dir):
        print(root)
        print('   ',dirs)

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
        "categories":{}
    }


    # Get new stats, filling in new stat dictionaries:
    print(new_weekly_entry)
    iterateContentIndexMdFiles()
    print(new_weekly_entry)

    # Update/replace yaml files
    '''
    existing_weekly_dic.update()
    new_tests_entry.overwrite tests_status_file_path
    '''









if __name__ == "__main__":
    main()
