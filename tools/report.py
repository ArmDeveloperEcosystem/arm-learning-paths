#/usr/bin/env python3

import argparse
import logging
import os
import subprocess
import csv
import json
from pathlib import Path
from datetime import datetime, timedelta

# List of directories to parse for learning paths
dname = ["content/install-tools",
         "content/learning-paths/desktop-and-laptop",
         "content/learning-paths/embedded",
         "content/learning-paths/microcontroller",
         "content/learning-paths/mobile",
         "content/learning-paths/server-and-cloud"]


'''
Recursive content search in d. Update list of articles older than period. Returns count of articles found
'''
def content_parser(d, period):
    count = 0
    result = {}
    l = os.listdir(d)
    for i in l:
        if i.endswith(".md") and not i.startswith("_"):
            count = count + 1
            logging.debug("Checking {}...".format(d+"/"+i))

            date = subprocess.run(["git", "log", "-1" ,"--format=%cs", d +"/" + i], stdout=subprocess.PIPE)
            # strip out '\n' and decode byte to string
            date = date.stdout.rstrip().decode("utf-8")
            logging.debug(date)

            # if empty, this is a temporary file which is not part of the repo
            if(date != ""):
                date = datetime.strptime(date, "%Y-%m-%d")
                # check if article is older than the period
                if date < datetime.now() - timedelta(days = period):
                    result[d + "/" + i] = "{} days ago".format((datetime.now() - date).days)

        # if this is a folder, let's get down one level deeper
        elif os.path.isdir(d + "/" + i):
            res, c = content_parser(d + "/" + i, period)
            result.update(res)
            count = count + c

    return [result, count]


'''
'''
def stats():
    global dname

    orig = os.path.abspath(os.getcwd())

    # If file exists, load data. Create structure otherwise
    if os.path.exists('content/stats/data.json'):
        # Opening JSON file
        f = open('content/stats/data.json', 'r')
        # returns JSON object as a dictionary
        data = json.load(f)
        # Closing JSON file
        f.close()
    else:
        # Create dict
        data = { 
            "data": [
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "install-tools",
                    "xaxis": "x1"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/desktop-and-laptop",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/embedded",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/microcontroller",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/mobile",
                    "xaxis": "x2"
                },
                {
                    "x": [],
                    "y": [],
                    "type": "bar",
                    "name": "learning-paths/server-and-cloud",
                    "xaxis": "x2"
                }
            ],
            "layout": 
            {
                "title": "Number of articles", 
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

    total=0
    for d_idx, d in enumerate(dname):
        res, count = content_parser(d, 0)
        # Sliding windows for data - remove data older than a year - 53 weeks
        if len(data["data"][d_idx]["x"]) > 52:
            data["data"][d_idx]["x"].pop(0)
            data["data"][d_idx]["y"].pop(0)
        # Date
        data["data"][d_idx]["x"].append(datetime.now().strftime("%Y-%b-%d"))
        # Articles counted in category
        data["data"][d_idx]["y"].append(count)
        logging.info("{} articles found in {}.".format(count, d))
        total += count

    logging.info("Total number of Learning Paths is {}.".format(total))

    fn='content/stats/data.json'
    os.chdir(orig)
    logging.info("Results written in " + orig + "/" + fn)

    # Save data in json file
    f = open(fn, 'w')
    # Write results to file
    json.dump(data, f)    
    # Closing JSON file
    f.close()


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
        res, count = content_parser(d, period)
        result.update(res)
        logging.info("Found {} articles in {}. {} of them are outdated.".format(count, d, len(res)))
        total += count

    logging.info("Total number of articles is {}.".format(total))

    fn="outdated_files.csv"
    fields=["File", "Last updated"]
    os.chdir(orig)
    logging.info("Results written in " + orig + "/" + fn)

    with open(fn, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fields)
        writer.writeheader()
        for key in result.keys():
            csvfile.write("%s, %s\n" % (key, result[key]))

