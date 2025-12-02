---
# User change
title: "Contribute"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Commit your changes

As you are working, use Git to commit your changes. Only you can see the changes made to your fork.

{{% notice Note%}}
Find a Git tutorial if you need help adding and committing the new files. 
{{% /notice %}}

Commits can be done as a single commit or a series of commits. You can also periodically push your changes to GitHub using the `git push` command. 

Continue to make modifications to your new Learning Path and save them along the way.

When you are ready to submit your Learning Path for review, proceed to the next section and submit a pull request.

## Submit a pull request 

Before submitting a pull request, make sure `hugo` runs without errors on the command line. Run this from the top level directory of the repository. 

```console
hugo
```

The output should be a table similar to the one below with no other error messages.

```output

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

After you have reviewed the new material using `hugo server` and there are no issues running `hugo` submit a GitHub pull request. 

You can now submit a GitHub pull request. 

{{% notice Note%}}
If you are new to GitHub, please go to [GitHub's documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)
to learn how to create a pull request from a GitHub fork.
{{% /notice %}}

Optionally, if you would like to add your new Learning Path content to the automated testing framework, for testing instructions and code snippets automatically in the learning path, follow the guidelines in the [Appendix: How to test your code](/learning-paths/cross-platform/_example-learning-path/appendix-3-test).

## Publishing

After submitting a pull request, automated checks will run to validate your metadata format and the Learning Path team will start reviewing your submission. This is done for technical accuracy and to review writing style. Watch the pull request for review comments and respond as needed. Once the pull request is merged, the website is automatically updated with the new contribution. 

{{% notice Note 1 %}}
If there are small typos or formatting issues, we will fix them before publishing. This is done to reduce the amount of back-and-forth overhead on small issues; you will always be able to view all changes through GitHub and let us know if you object to any changes.
{{% /notice %}}

{{% notice Note 2 %}}
If there are large factual or reproducibility errors in your contribution, we will contact you via the pull request to resolve them before publishing.
{{% /notice %}}

## Updating Learning Paths

Learning Paths should be always up to date and high quality. Over time software may change and instructions may become outdated.

Learning Path content is automatically monitored for out of date material. We may contact you to confirm a Learning Path is still current, or requires revision. 

Community members can also submit feedback on Learning Paths and highlight information that has become outdated. We appreciate feedback.

Keep an eye out for requests and please respond as needed.

Thank you for creating and sharing a new Learning Path!

