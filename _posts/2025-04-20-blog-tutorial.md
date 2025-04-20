---
layout: post
title:  "How to publish a blog website"
date:   2025-04-20 13:48:44 -04:00
categories: tutorials
published: false
---

Have you ever wondered how so many people are able to publish their own content? This tutorial demonstrates one method of creating a simple website for free!

> Note: following this tutorial does not require any website programming experience or knowledge of typical developer tools.

---

# Preface
There are many options for deploying a free website. This tutorial uses the [**Cloudfare platform**] to deploy a website stored in a git repository hosted on GitHub. 

This tutorial will help you create a website by using the following platforms, frameworks, and file formats: GitHub, Cloudfare, Jekyll, Liquid, Front Matter, and Markdown [**TODO: LINKS**]. See the [**"further reading"**] section below to learn more about how each of these technologies work. However, it is not required to understand each of these components in detail.

> Note: GitHub provides a built-in website publishing service called [GitHub Pages - **TODO: LINK**]. This is an alternate solution to Cloudfare.

This tutorial is broken into four parts. You will have deployed a fully functional website after completing each of these!

---

# Part I: Create a website repository

1. Create a GitHub Account  
    [https://github.com/signup](https://github.com/signup)

2. Create a new repository from this premade template 
    1. Click the link below and follow the onscreen prompts:  
        [**LINK**]

    1. Choose your account for the repository
    1. Choose a repo name
    1. Click "create repository"
    1. Bookmark the URL for your new repository. You will need it later!

Tutorial Reference: [**ADD SOURCE**]


# Part II: Deploy your website

1. Create a Cloudfare account  
    [https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)

1. Click the "Add" button on the top-right of the header bar
1. Click "Pages" on the drop-down menu that appears.
1. Click the "Connect to git" button.
1. Click the "Connect GitHub" button and follow the onscreen prompts.

Tutorial Reference: [Deploy with Cloudfare Pages](https://developers.cloudflare.com/pages/framework-guides/deploy-a-jekyll-site/#deploy-with-cloudflare-pages)


# Part III: Customize your website settings

1. Navigate to your GitHub repository link (from Part I above).
1. Click on the `_config.yml` file link.
1. Click the pencil icon in the top-right menu bar to edit the file.
1. Modify the `_config.yml` file settings:
    1. Update the `title` value with the name of your website.
    1. Update the `description` value with a short description for your website

1. Click the "Commit changes" button and follow the onscreen prompts to save your modifications.
1. Navigate to your Cloudfare Pages project dashboard. You should see the changes applied automatically.


# Part IV: Create some content!

1. Navigate to your GitHub repository link (from Part I above).
1. Click on the `_posts` directory link.
1. Click on the "Add file" drop-down menu button.
1. Click on "Create new file".
1. Type a file name
    1. Use the form `YYYY-MM-DD-NAME.md` for the file name:
    1. `YYYY-MM-DD`: date of the post
    1. `NAME`: Filename of the post
1. Add the "post" front matter to the top of the file:
    ```
    ---
    layout: post
    title:  "YOUR POST TITLE"
    date:   YYYY-MM-DD HH:MM:SS -0500
    category: OPTIONAL CATEGORY NAME
    ---
    ```

1. Use the markdown file format to add the post page content into the file.
1. Click the "Commit changes" button and follow the onscreen prompts to save your modifications.
1. Navigate to your Cloudfare Pages project dashboard. You should see the changes applied automatically.

> See the [markdown] references in the "further reading" section below to understand the file format syntax. You can view the `_posts/YYYY-MM-DD-SAMPLE.md` file in your repository as an example for how to write markdown.

# Part V: Deploy your site!
1. Navigate to your Cloudfare Pages project dashboard. 
1. Deploy your application!

<br/>
<br/>

---

# Further Reading

**git** is a version control system popular amongst programmers for storing the complete revision history of a program. Over the past decade, it has also become popular among website content creators to keep a history of the website content revisions over time. The most common method for using git is via a command-line terminal program. See this [git handbook](https://docs.github.com/en/get-started/using-git/about-git) for more information on the typical usage for git.

**GitHub** is a Microsoft platform for storing and archiving git repositories. All website content should be stored in a single git repository.


**Jekyll** – [https://jekyllrb.com/](https://jekyllrb.com/)

**Markdown**
- https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

- https://docs.github.com/en/contributing/writing-for-github-docs/using-markdown-and-liquid-in-github-docs

