#/usr/bin/env python3

import logging
import os
import shutil
import subprocess
import json
from junit_xml import TestCase
import alive_progress

"""
Checks a dictionary for a given key. Helper function to avoid runtime errors.
"""
def dictionary_lookup(dictionary, key):
    try:
        # Try that the value exists, and that it is not None
        value = dictionary[key]
        assert value
        return True
    except Exception:
        logging.debug(f"\"{key}\" was not found in dictionary {dictionary}.")
        return False


"""
Initializes a Docker container and runs a few commands to set it up.

    - Install dependencies
    - Set up user permissions
    - Remove the default .bashrc on Ubuntu (since it returns when not interactive)
    - Allow write permissions on shared folder

If the passed image is not supported, an IOError is thrown.
"""
def init_container(i_img, img):
    # Launch
    container_name = f"test_{i_img}"
    logging.info(f"Initializing {container_name} -> {img}")
    init_docker_cmd = [f"docker run --rm -t -d -v $PWD/shared:/shared --name test_{i_img} {img}"]
    logging.debug(init_docker_cmd)
    subprocess.run(init_docker_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    package_manager = ""
    user = ""
    if img.startswith(("ubuntu", "mongo", "arm-tools")):
        package_manager = "apt"
        user = "sudo"
    elif "fedora" in img:
        package_manager = "yum"
        user = "wheel"
    else:
        raise SystemExit(f"Image {img} not supported")

    docker_cmd = [f"docker exec test_{i_img} {package_manager} update"]
    logging.debug(docker_cmd)
    subprocess.run(docker_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    if "arm-tools" in img:
        # These images already have a 'ubuntu' user account set up
        pass

    docker_cmd = [
                f"docker exec {container_name} {package_manager} install -y sudo wget curl git",
                f"docker exec {container_name} useradd user -m -G {user}",
                f"docker exec {container_name} bash -c \"cat << EOF > /etc/sudoers.d/user\n user ALL=(ALL) NOPASSWD:ALL\nEOF\"",
                f"docker exec {container_name} rm /home/user/.bashrc",
                f"docker exec {container_name} chmod ugo+rw /shared"
                ]
    for cmd in docker_cmd:
        logging.debug(cmd)
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    return container_name

"""
Checks the test for a number of commands and write it to the test command file.
"""
def write_commands_to_file(test_cmd_filename, test):
    # Write series of commands in this file
    cmd = ""
    f = open(test_cmd_filename, "w")

    # Check if:
    # - A file needs to be sourced
    # - Working directory is specified
    # - An environment variable is specified
    cmd_args = {
                "env_source":".",
                "cwd":"cd ",
                "env":"export"
                }
    for cmd_arg in cmd_args.keys():
        if cmd_arg in test:
            # Retrieve the command as string
            cmd_arg_test = test[cmd_arg] if isinstance(test[cmd_arg], str) else test[cmd_arg][0]
            cmd = cmd_args[cmd_arg] + " " + cmd_arg_test
            logging.debug(f"FINAL COMMAND: {cmd}")
            write_cmd_to_file(f, test_cmd_filename, cmd)

    # Check if commands need to be run before the test
    if "pre_cmd" in test:
        pre_cmd = test["pre_cmd"]
        cmd = pre_cmd
        write_cmd_to_file(f, test_cmd_filename, cmd)

    # Check if the test has multiple lines
    if test.get("ncmd"):
        for cmd_line in range(0, test["ncmd"]):
            if "expected" in test.keys():
                # Do not run output commands
                if cmd_line in test["expected"]:
                    continue
            cmd = test[f"{cmd_line}"]
            write_cmd_to_file(f, test_cmd_filename, cmd)

    f.close()
    return cmd

"""
Write a command to a file and log it for debugging.
"""
def write_cmd_to_file(f, test_cmd_filename, cmd):
    logging.debug(f"Command argument written to {test_cmd_filename}: {cmd}")
    cmd_str = f"{cmd}\n"
    f.write(cmd_str)
    logging.info(cmd_str)

"""
Parse JSON file with commands from the Markdown article,
run commands in Docker and log the result in the console.
"""
def check(json_file, start, stop, md_article):
    with open(json_file) as jf:
        data = json.load(jf)

    if dictionary_lookup(data, "test_images"):
        test_images = data["test_images"]
    else:
        logging.info(f"No test_images could be parsed from {md_article}, skipping")
        return {}

    # Create one test suite for each image
    test_cases= [[] for img in test_images]
    # Create array to store test result
    results = {img:0 for img in test_images}

    # Check if there are tests / code blocks
    if not dictionary_lookup(data, "ntests"):
        logging.info(f"No tests were parsed from {md_article}, skipping")
        return results

    # Run code blocks
    test_images = data["test_images"]
    for n_image, test_image in zip(range(0, len(test_images)), test_images):
        logging.info(f"--- Testing on {test_image} ---")

        if test_image != "ubuntu:latest":
            container_name = init_container(i_img=n_image, img=test_image)
            logging.info(f"{container_name} initialized")

        with alive_progress.alive_bar(data["ntests"], title=test_image, stats=False) as bar:
            for n_test in range(0, data["ntests"]):
                if dictionary_lookup(data, f"{n_test}"):
                    test = data[f"{n_test}"]
                else:
                    logging.info(f"Error getting test from JSON file, skipping")
                    continue

                test_target = test.get("target") or ""
                if test_target and test_target != test_image:
                    bar(skipped=True)
                    continue
                elif not test_target:
                    pass
                elif test_target:
                    pass
                else:
                    bar(skipped=True)
                    continue

                if "file_name" in test:
                    test_cmd_filename = test["file_name"]
                else:
                    test_cmd_filename = ".tmpcmd"

                cmd = write_commands_to_file(test_cmd_filename, test)

                username = "ubuntu" if "arm-tools" in test_images[0] else "user"

                test_type = test["type"]
                # Check type
                if test_type == "bash":
                    if "ubuntu" in test_image:
                        # chmod cmd file
                        run_command = [f"chmod +x {test_cmd_filename}"]
                        subprocess.run(run_command, shell=True, capture_output=True)
                        logging.debug(run_command)
                        # execute file as is with bash
                        run_command = [f"bash ./{test_cmd_filename}"]
                    elif "fedora" in test_target:
                        # copy files to docker
                        docker_cmd = [f"docker cp {test_cmd_filename} test_{n_image}:/home/{username}/"]
                        subprocess.run(docker_cmd, shell=True, capture_output=True)
                        logging.debug(docker_cmd)
                        run_command = [f"docker exec -u {username} -w /home/{username} test_{n_image} bash {test_cmd_filename}"]
                    else:
                        logging.debug(f"Image {test_image} not supported for testing. Contact the maintainers if you think this is a mistake.")
                        bar(skipped=True)
                        continue
                elif test_type == "fvp":
                    # Start instance for image
                    if start:
                        container_name = init_container(i_img=n_image, img=test_image)
                        logging.info(f"{container_name} initialized")
                    else:
                        logging.debug("Parameter start is false, skipping container(s) initialization")

                    # copy files to docker
                    docker_cmd = [f"docker cp {test_cmd_filename} test_{n_image}:/home/{username}/"]
                    subprocess.run(docker_cmd, shell=True, capture_output=True)
                    logging.debug(docker_cmd)


                    ethos_u65 = ""
                    fvp_name = test["fvp_name"]
                    if fvp_name == "FVP_Corstone_SSE-300_Ethos-U65":
                        ethos_u65 = "ETHOS_U65=1 -e"
                        test_cwd = test["cwd"]
                    # Only allow single line commands
                    run_command = test["0"].replace(f"{fvp_name}",
                                                    f"docker run --rm -ti -v $PWD/shared:/shared -w {test_cwd} -e \
                                                    {ethos_u65} NON_INTERACTIVE=1 --name test_fvp flebeau/arm-corstone-300-fvp"
                    )
                else:
                    logging.debug(f"Type '{test_type}' not supported for testing. Contact the maintainers if you think this is a mistake.")
                    bar(skipped=True)
                    continue



                logging.debug(run_command)
                process = subprocess.run(run_command, shell=True, capture_output=True)
                process_output = process.stdout.rstrip().decode("utf-8")
                process_error = process.stderr.rstrip().decode("utf-8")

                # Remove the file storing the command since we now ran it
                os.remove(test_cmd_filename)

                # Create test case
                test_case_name = json_file.replace("_cmd.json","")
                test_case = TestCase(f"{test_case_name}_{test_images[n_image]}_test-{n_image}",
                                        cmd, 0, process_output, '')
                test_cases[n_image].append(test_case)
                test_ret_code = int(test["ret_code"]) if test.get("ret_code") else 0

                test_passed = False
                # if success
                if process.returncode == test_ret_code:
                    # check with expected result if any
                    if "expected" in test.keys():
                        for line in test["expected"]:
                            exp = test[str(line)]
                            if exp == process_output:
                                test_passed = True
                                msg = "PASSED"
                            else:
                                msg = f"ERROR. Expected '{exp}'"
                                test_cases[n_image][-1].add_failure_info(msg)
                                results[test_images[n_image]] = results[test_images[n_image]]+1
                    else:
                        test_passed = True
                        msg = "PASSED"
                else:
                    msg = f"ERROR. Expected return code {test_ret_code} but got {process.returncode}"
                    test_cases[n_image][-1].add_failure_info(msg)
                    results[test_images[n_image]] = results[test_images[n_image]]+1
                bar()
                if not test_passed and process_error:
                    logging.info(f"{process_error}")
                elif not test_passed and process_output:
                    logging.info(f"{process_output}")
                else:
                    logging.debug(f"{process_output}")
                logging.info(f"{msg}")
                logging.info("---------")
        result = "failed" if results[test_images[n_image]] else "passed"
        logging.info(f"Tests {result} on {test_image}")

    # Remove command file if no tests existed
    if os.path.exists(test_cmd_filename):
        os.remove(test_cmd_filename)

    # Remove files that were generated from the tests, if any
    untracked_files_process = subprocess.run("git ls-files --others --exclude-standard", shell=True, capture_output=True)
    untracked_files = untracked_files_process.stdout.decode("utf-8").splitlines()
    paths_to_remove = [ file_name for file_name in untracked_files \
                        if "_cmd.json" not in file_name \
                        and "test-lp-output.txt" not in file_name ]

    if paths_to_remove:
        logging.info(f"Removing files that were created during testing from repository")
        for path in paths_to_remove:
            try:

                if os.path.isfile(path) or os.path.islink(path):
                        os.chmod(path, 0o777)
                        os.remove(path)


                elif os.path.isdir(path):
                    shutil.rmtree(path)
                logging.debug(f"Removed {path}")
            except PermissionError as e:
                    logging.debug(f"Failed to remove {path} with error: {e}")

    # Stop instance
    if stop:
        logging.debug("Terminating container(s)")
        for i_img, img in enumerate(test_images):
            cleanup_cmd = [f"docker stop test_{i_img}"]
            logging.debug(cleanup_cmd)
            subprocess.run(cleanup_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

        logging.debug("Removing shared directory")
        cleanup_cmd = ["rm -rf shared"]
        logging.debug(cleanup_cmd)
        subprocess.run(cleanup_cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    else:
        logging.debug("Parameter stop is false, skipping container(s) termination")
    return results