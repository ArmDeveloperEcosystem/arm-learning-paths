The Arm Learning Paths website is available at https://learn.arm.com/

# Arm Learning Paths  

This repository contains the source files for the Arm Learning Paths static website, serving learning based technical content for Arm software developers. 

The Learning Paths created here are maintained by Arm and the Arm software development community. Learning Paths are meant to solve problems developers face while developing on and for Arm. Helpful instructions to install a variety of software tools are also provided.

<br/>

# How To Contribute

All contributions are welcome as long as they relate to software development for the Arm architecture. 
  * Write a Learning Path (or improve existing content)
    * Fork this repo and submit pull requests; follow the step by step instructions in [Create a Learning Path](https://learn.arm.com/learning-paths/cross-platform/_example-learning-path/) on the website.
  * Ideas for a new Learning Path
    * Create a new GitHub idea under the [Discussions](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/discussions) area in this GitHub repo.
  * Log a code issue (or other general issues)
    * Log a [issue on GitHub](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/issues) or from the Learning Path on the left-hand nav bar.

Note that all site content, including new contributions, is licensed under a [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/).

<br/>

# Other Arm Learning Resources
The Learning Path site contains software-based Learning Paths and Tool Install Guides, and complements the other Arm resources in the Arm Developer Hub and beyond. Here are links to other areas depending on what/how you want to learn:
  * [Learning Paths](https://learn.arm.com/learning-paths)
  * [Tool Install Guides](https://learn.arm.com/install-guides)
  * [Arm IP Documentation](https://developer.arm.com)  



# Directory Structure

This site is built on the [Hugo](https://gohugo.io/) web framework, ideal for generating static websites. Below is a brief description of the key files and directories:

  * /content
    * contains all Learning Paths and install guides
  * /themes
    * where the html elements are defined to render /content into stylized HTML
  * /tools
    * python scripts to automatically check website integrity
  * LICENSE files
    * where the license information is contained
  * config.toml
    * where the high-level website configuration settings are defined
 
