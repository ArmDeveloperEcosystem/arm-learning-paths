#/usr/bin/env python3

import argparse
import logging
import os
import subprocess
import csv
import json
import re
from pathlib import Path
from datetime import datetime, timedelta

# List of directories to parse for learning paths
dname = ["content/install-guides",
         "content/learning-paths/cross-platform",
         "content/learning-paths/laptops-and-desktops",
         "content/learning-paths/embedded-systems",
         "content/learning-paths/microcontrollers",
         "content/learning-paths/smartphones-and-mobile",
         "content/learning-paths/servers-and-cloud-computing"]


'''
Recursive content search in d. 
Returns: 
- list of articles older than period in d
- count of articles found in d
- list of primary authors in d
'''
def content_parser(d, period):
    count = 0
    art_list = {}
    auth_list = []
    l = os.listdir(d)
    for i in l:
        item = i
        if item.endswith(".md") and not item.startswith("_"):
            count = count + 1
            if "learning-paths" in d:
                item = "_index.md"

            logging.debug("Checking {}...".format(d+"/"+item))

            date = subprocess.run(["git", "log", "-1" ,"--format=%cs", d +"/" + item], stdout=subprocess.PIPE)
            # strip out '\n' and decode byte to string
            date = date.stdout.rstrip().decode("utf-8")
            logging.debug("Last updated on: " + date)
            author = "None"
            for l in open(d +"/" + item): 
                if re.search("author_primary", l):
                    # split and strip out '\n'
                    author = l.split(": ")[1].rstrip()
            logging.debug("Primary author: " + author)
            if not author in auth_list:
                auth_list.append(author)

            # if empty, this is a temporary file which is not part of the repo
            if(date != ""):
                date = datetime.strptime(date, "%Y-%m-%d")
                # check if article is older than the period
                if date < datetime.now() - timedelta(days = period):
                    if item == "_index.md":
                        art_list[d + "/"] = "{} days ago".format((datetime.now() - date).days)
                    else:
                        art_list[d + "/" + item] = "{} days ago".format((datetime.now() - date).days)

            if "learning-paths" in d:
                # no need to iterate further
                break

        # if this is a folder, let's get down one level deeper
        elif os.path.isdir(d + "/" + item):
            res, c, a_l = content_parser(d + "/" + item, period)
            art_list.update(res)
            count = count + c
            for a in a_l:
                if not a in auth_list:
                    auth_list.append(a)

    return [art_list, count, auth_list]


'''
Initialize Plotly data structure for stats
1 graph on the left with data for install tool guides 
1 graph on the right with data for learning paths
Input: title for the graph
'''
def init_graph(title):
    data = { 
            "data": [
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "install-guides",
                    "xaxis": "x1"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/cross-platform",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/laptops-and-desktops",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/embedded-systems",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/microcontrollers",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/smartphones-and-mobile",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/servers-and-cloud-computing",
                    "xaxis": "x2"
                }
            ],
            "layout": 
            {
                "title": title, 
                "xaxis": 
                {
                    "tickangle": -45,
                    "domain": [0, 0.45],
                    "anchor": "x1"
                }, 
                "xaxis2": 
                {
                    "tickangle": -45,
                    "domain": [0.55, 1],
                    "anchor": "x2"
                }, 
                "barmode": "stack", 
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "rgba(0,0,0,0)",
                "font": 
                {
                    "color": "rgba(130,130,130,1)"
                },
                "legend": 
                {
                    "bgcolor": "rgba(0,0,0,0)"
                }
            }
        }

    return data


'''
Generate JSON data for stats page
'''
def stats():
    global dname

    orig = os.path.abspath(os.getcwd())

    # If file exists, load data. Create structure otherwise
    if os.path.exists('content/stats/lp_data.json'):
        # Opening JSON file
        f = open('content/stats/lp_data.json', 'r')
        # returns JSON object as a dictionary
        lp_data = json.load(f)
        # Closing JSON file
        f.close()
    else:
        # Create dict
        lp_data = init_graph("Number of installation guides and learning paths")

    # If file exists, load data. Create structure otherwise
    if os.path.exists('content/stats/contrib_data.json'):
        # Opening JSON file
        f = open('content/stats/contrib_data.json', 'r')
        # returns JSON object as a dictionary
        contrib_data = json.load(f)
        # Closing JSON file
        f.close()
    else:
        # Create dict
        contrib_data = init_graph("Number of contributors")

    total=0
    for d_idx, d in enumerate(dname):
        res, count, authors = content_parser(d, 0)
        # Sliding windows for data - remove data older than a year - 53 weeks
        if len(lp_data["data"][d_idx]["x"]) > 52:
            lp_data["data"][d_idx]["x"].pop(0)
            lp_data["data"][d_idx]["y"].pop(0)
        if len(contrib_data["data"][d_idx]["x"]) > 52:
            contrib_data["data"][d_idx]["x"].pop(0)
            contrib_data["data"][d_idx]["y"].pop(0)
        # Date
        lp_data["data"][d_idx]["x"].append(datetime.now().strftime("%Y-%b-%d"))
        contrib_data["data"][d_idx]["x"].append(datetime.now().strftime("%Y-%b-%d"))
        # Articles counted in category
        lp_data["data"][d_idx]["y"].append(count)
        # Authors counted in category
        contrib_data["data"][d_idx]["y"].append(len(authors))

        if "learning-paths" in d:
            logging.info("{} Learning Paths found in {} and {} contributor(s).".format(count, d, len(authors)))
            total += count
        else:
            logging.info("{} articles found in {} and {} contributor(s).".format(count, d, len(authors)))

    logging.info("Total number of Learning Paths is {}.".format(total))

    fn_lp='content/stats/lp_data.json'
    fn_contrib='content/stats/contrib_data.json'
    os.chdir(orig)
    logging.info("Learning Path data written in " + orig + "/" + fn_lp)
    logging.info("Contributors data written in " + orig + "/" + fn_contrib)

    # Save data in json file
    f_lp = open(fn_lp, 'w')
    f_contrib = open(fn_contrib, 'w')
    # Write results to file
    json.dump(lp_data, f_lp)
    json.dump(contrib_data, f_contrib)    
    # Closing JSON file
    f_lp.close()
    f_contrib.close()


'''
List pages older than a period in days and save result as CSV
Generate JSON file with data
'''
def report(period):
    global dname

    orig = os.path.abspath(os.getcwd())

    # chdir to the root folder
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/..")

    result = {}

    total=0
    for d_idx, d in enumerate(dname):
        res, count, authors = content_parser(d, period)
        result.update(res)
        if "learning-paths" in d:
            logging.info("Found {} Learning Paths in {}. {} of them are outdated.".format(count, d, len(res)))
            total += count
        else:
            logging.info("Found {} articles in {}. {} of them are outdated.".format(count, d, len(res)))

    logging.info("Total number of Learning Paths is {}.".format(total))

    fn="outdated_files.csv"
    fields=["File", "Last updated"]
    os.chdir(orig)
    logging.info("Results written in " + orig + "/" + fn)

    with open(fn, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        for key in result.keys():
            csvfile.write("%s, %s\n" % (key, result[key]))

