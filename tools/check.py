#/usr/bin/env python3

import logging
import os
import subprocess
import json
import yaml
from junit_xml import TestSuite, TestCase


'''
Parse header and patch file with test results
'''
def patch(article, results, lk):
    with open(article, mode='r') as f:
        content = f.read()
        f.close()
        header = []

    for i in content:
        start = content.find("---") + 3
        end = content.find("---", start)

        if end == start-3:
            # No header
            logging.debug("No header found in {}".format(article))
            return
        else:
            header = content[start:end]
            markdown = content[end+3:]
            data = yaml.safe_load(header, )

    # Update status or create section
    arr = []
    
    # Check if this is a learning path
    if isinstance(results, list) and data.get("test_images"):
        for res in data["test_images"]:
            failed = False
            for el in (results):
                if el[res] != 0:
                    logging.debug("Status on {}: FAILED".format(res))
                    arr.append("failed")
                    failed = True
                    break

            if not failed:
                logging.debug("Status on {}: passed".format(res))
                arr.append("passed")
    elif data.get("test_images"):
        for res in data["test_images"]:
            if results[res] != 0:
                logging.debug("Status on {}: FAILED".format(res))
                arr.append("failed")
            else:
                logging.debug("Status on {}: passed".format(res))
                arr.append("passed")    

    data["test_status"] = arr

    data["test_link"] = lk

    # update markdown files with test results
    with open(article, mode='w') as f:
        f.write("---\n")
        yaml.dump(data, f)
        f.write("---")
        f.close()

    # write the rest of the content
    with open(article, mode='a') as f:
        for i in markdown:
            f.write(i)
        f.close()


'''
Read json file and run commands in Docker
'''
def check(json_file, start, stop):
    with open(json_file) as jf:
        data = json.load(jf)

    # Start instances for all images
    if start and data.get("image"):
        for i, img in enumerate(data["image"]):
            # Launch
            logging.info("Container instance test_{} is {}".format(i, img))
            cmd = ["docker run --rm -t -d -v $PWD/shared:/shared --name test_{} {}".format(i, img)]
            logging.debug(cmd)
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

            # Create user and configure
            if  "arm-tools" in img:
                # These images already have a 'ubunutu' user account set up.
                cmd = ["docker exec test_{} apt update".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            elif "ubuntu" in img or "mongo" in img:
                cmd = ["docker exec test_{} apt update".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                cmd = ["docker exec test_{} apt install -y sudo wget curl git".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                cmd = ["docker exec test_{} useradd user -m -G sudo".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                cmd = ["docker exec test_{} bash -c \"cat << EOF > /etc/sudoers.d/user\n user ALL=(ALL) NOPASSWD:ALL\nEOF\"".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                # The default .bashrc on Ubuntu returns when not interactive so removing it
                cmd = ["docker exec test_{} rm /home/user/.bashrc".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                # Allow write permissions on shared folder
                cmd = ["docker exec test_{} chmod ugo+rw /shared".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            elif "fedora" in img:
                cmd = ["docker exec test_{} yum update".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                cmd = ["docker exec test_{} yum install -y sudo wget curl git".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                cmd = ["docker exec test_{} useradd user -m -G wheel".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                cmd = ["docker exec test_{} bash -c \"cat << EOF > /etc/sudoers.d/user\n user ALL=(ALL) NOPASSWD:ALL\nEOF\"".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                # Allow write permissions on shared folder
                cmd = ["docker exec test_{} chmod ugo+rw /shared".format(i)]
                logging.debug(cmd)
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        logging.info("Container(s) initialization completed")
    else:
        logging.debug("Skip container(s) launch")

    if data.get("image"):
        # Create 1 test suite for each image
        test_cases= [[] for img in data["image"]]
        # Create array to store test result
        results = {img:0 for img in data["image"]}
    else:
        test_cases = []
        results = {}

    # Check if there are tests
    if not "ntests" in data.keys():
        return results

    # Run bash commands
    print(data["ntests"])
    for i in range(0, data["ntests"]):
        if not data.get("{}".format(i)):
            continue
        print(i)
        t = data["{}".format(i)]
        print(t)

        # Check if file name is specified
        if "file_name" in t:
            fn = t["file_name"]
        else:
            fn = ".tmpcmd"

        # Write series of commands in this file
        c = ""
        f = open(fn, "w")
        # Check if a file needs to be sourced
        if "env_source" in t:
            env_source = t["env_source"]
            c = "source " + env_source
            logging.debug("Copying command to file to file {}: {}".format(fn, c))
            f.write("{}\n".format(c))
        # Check if env var are specified
        if "env" in t:
            env = t["env"]
            for el in env:
                c = "export " + el
                logging.debug("Copying command to file to file {}: {}".format(fn, c))
                f.write("{}\n".format(c))
        # Check if commands need to be run beforehand
        if "pre_cmd" in t:
            pre_cmd = t["pre_cmd"]
            c = pre_cmd
            logging.debug("Copying command to file to file {}: {}".format(fn, c))
            f.write("{}\n".format(c))
        # Check if cwd is specified
        if "cwd" in t:
            c = "cd " + t["cwd"]
            logging.debug("Copying command to file {}: {}".format(fn, c))
            f.write("{}\n".format(c))
        if t.get("ncmd"):
            for j in range(0, t["ncmd"]):
                if "expected" in t.keys():
                    # Do not run output commands
                    if j == (int(eval(t["expected"]))-1):
                        break
                c = t["{}".format(j)]
                logging.debug("Copying command to file {}: {}".format(fn, c))
                f.write("{}\n".format(c))
        f.close()

        # Check if a target is specified
        if "target" in t:
            # get element index of instance
            idx = data["image"].index(t["target"])
            inst = range(idx, idx+1)
        else:
            inst = range(0, len(data["image"]))

        username = "ubuntu" if "arm-tools" in data["image"][0] else "user"
        for k in inst:
            # Copy over the file with commands
            cmd = ["docker cp {} test_{}:/home/{}/".format(fn, k, username)]
            subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            logging.debug(cmd)

            # Check type
            if t["type"] == "fvp":
                # Only allow single line commands
                if t["fvp_name"] == "FVP_Corstone_SSE-300_Ethos-U65":
                    cmd = t["0"].replace("FVP_Corstone_SSE-300_Ethos-U65", "docker run --rm -ti -v $PWD/shared:/shared -w {} -e ETHOS_U65=1 -e NON_INTERACTIVE=1 --name test_fvp flebeau/arm-corstone-300-fvp".format(t["cwd"]))
                else:
                    cmd = t["0"].replace("FVP_Corstone_SSE-300_Ethos-U55", "docker run --rm -ti -v $PWD/shared:/shared -w {} -e NON_INTERACTIVE=1 --name test_fvp flebeau/arm-corstone-300-fvp".format(t["cwd"]))
            elif t["type"] == "bash":
                cmd = ["docker exec -u {} -w /home/{} test_{} bash {}".format(username, username, k, fn)]
            else:
                logging.debug("Omitting type: {}".format(t["type"]))
                cmd = []

            if cmd != []:
                logging.debug(cmd)
                p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                # create test case
                test_cases[k].append(TestCase("{}_{}_test-{}".format(json_file.replace("_cmd.json",""), data["image"][k], i), c, 0, p.stdout.rstrip().decode("utf-8"), ''))

                ret_code = 0
                if "ret_code" in t.keys():
                    ret_code = int(t["ret_code"])

                # if success
                if p.returncode == ret_code:
                    # check with expected result if any
                    if "expected" in t.keys():
                        t_expected = t.get("{}".format(int(eval(t["expected"]))-1))
                        if t_expected:
                            exp = t[t_expected]
                            # strip out '\n' and decode byte to string
                            if exp == p.stdout.rstrip().decode("utf-8"):
                                msg = "Test passed"
                            else:
                                msg = "ERROR (unexpected output. Expected {} but got {})".format(exp, p.stdout.rstrip().decode("utf-8"))
                                test_cases[k][-1].add_failure_info(msg)
                                results[data["image"][k]] = results[data["image"][k]]+1
                    else:
                        msg = "Test passed"
                else:
                    msg = "ERROR (command failed. Return code is {} but expected {})".format(p.returncode, ret_code)
                    test_cases[k][-1].add_failure_info(msg)
                    results[data["image"][k]] = results[data["image"][k]]+1

                logging.debug("Test {}: {}".format(i, msg))
                logging.info("{:.0f}% of all tests completed on instance test_{}".format(i/data["ntests"]*100, k))

        # Remove file with list of commands
        os.remove(fn)

    logging.info("100% of all tests completed")

    # add to test suite and write junit results
    ts = []
    for k in range(0, len(data["image"])):
        ts.append(TestSuite("{} {}".format(json_file,data["image"][k]), test_cases[k]))

    with open(json_file.replace(".json", ".xml"), mode='w') as lFile:
        TestSuite.to_file(lFile, ts, prettyprint=True)
        lFile.close()
        logging.info("Results written in {}".format(json_file.replace(".json", ".xml")))

    # Stop instance
    if stop:
        logging.info("Terminating container(s)...")
        for i, img in enumerate(data["image"]):
            cmd = ["docker stop test_{}".format(i)]
            logging.debug(cmd)
            subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        logging.info("Removing shared directory...")
        cmd = ["sudo rm -rf shared"]
        logging.debug(cmd)
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    else:
        logging.debug("Skip container(s) termination...")

    return results
