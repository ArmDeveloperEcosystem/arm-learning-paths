---
# User change
title: "Contribute"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Contribute your changes

Commit your changes to your GitHub fork using git. This can be done with a single commit or a series of commits. 

Before submitting a pull request, make sure `hugo` runs without errors on the command line. This should be run from the top level directory of the repository. 

```console
hugo
```

The output should be a table similar to the one below with no other error messages.

```console

                   | EN
-------------------+------
  Pages            | 685
  Paginator pages  |   0
  Non-page files   | 189
  Static files     |  53
  Processed images |   0
  Aliases          |   0
  Sitemaps         |   1
  Cleaned          |   0

Total in 864 ms
```

If there are any errors, such as incorrect formatting of metadata, fix them and try again. 

You can now submit a GitHub pull request. Optionally, if you would like to add your new learning path content to the automated testing framework, follow the guidelines in the [Apppendix: How to test your code](/learning-paths/cross-platform/_example-learning-path/appendix-3-test).
After you have reviewed the new material using `hugo server` and there are no issues running `hugo` submit a GitHub pull request. 

Search for a tutorial about how to create a pull request from a GitHub fork if you need guidance on creating the pull request. 

## Publishing

After submitting a pull request, automated checks will run to validate your metadata format and the Learning Path team will start reviewing your submission. This is done for technical accuracy and to review writing style. Watch the pull request for review comments and respond as needed. Once the pull request is merged, the website is automatically updated with the new contribution. 

{{% notice Note 1 %}}
If there are small typos or formatting issues, we will fix them before publishing. This is done to reduce the amount of back-and-forth overhead on small issues; you will always be able to view all changes through GitHub and let us know if you object to any changes.
{{% /notice %}}

{{% notice Note 2 %}}
If there are large factual or reproducibility errors in your contribution, we will contact you via the pull request to resolve them before publishing.
{{% /notice %}}

## Updating Learning Paths

Learning Paths should be always up to date and high quality. Over time software may change and instructions may be out of date.

Learning Path content is automatically monitored for out of date material. We may contact you to confirm a Learning Path is still up to date or to request some modifications to a Learning Path that has become out of date. 

Community members may also submit feedback on Learning Paths so we appreciate any help on keeping content current.

Keep an eye out for requests and please respond as needed.

Thank you!

