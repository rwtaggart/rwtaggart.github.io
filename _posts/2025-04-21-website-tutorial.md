---
layout: post
title:  "How to publish a website"
date:   2025-04-21 13:48:44 -04:00
categories: tutorials
---

Have you ever wondered how so many people are able to publish their own content? This tutorial demonstrates one method of creating a simple website for free!

> Note: following this tutorial does not require any website programming experience or knowledge of typical developer tools.

---

# Preface
There are many options available for deploying a website. This tutorial uses the [Cloudflare](#cloudflare) platform to deploy a website stored in a [git](#git) repository hosted on [GitHub](#github). Both platforms offer a free tier for hosting content.

This article will help you create a website by using the following platforms, frameworks, and file formats: [GitHub](#github), [Cloudflare](#cloudflare), [git](#git), [Jekyll](#jekyll), [Liquid](#liquid), [Front Matter](#front-matter), and [Markdown](#markdown). See the ["further reading"](#further-reading) section below to learn about the purpose of each dependency. It is not required to understand the details of these components for the purposes of this tutorial.

> Note: GitHub provides a built-in website publishing service called [GitHub Pages](#github-pages). This is an alternate solution to Cloudflare.

You will deploy your own website after completing all five of the sections below!

---

# Part I: Create a website repository

1. Create a GitHub Account  
    [https://github.com/signup](https://github.com/signup)

2. Create a new repository from the pre-made [jekyll-blog-template](https://github.com/rwtaggart/jekyll-blog-template).
    1. Click this link and follow the onscreen prompts:  
        [Create a new repository](https://github.com/new?template_name=jekyll-blog-template&template_owner=rwtaggart)

    1. Confirm your account name for the repository owner
    1. Choose a new repository name.
    1. Click the "create repository" button.
    1. Bookmark the URL for your new repository. You will need it later!

> _Tutorial reference:_  
> [Start your journey: learn the basics of GitHub](https://docs.github.com/en/get-started/start-your-journey)


# Part II: Deploy your website

1. Create a Cloudflare account  
    [https://dash.cloudflare.com/sign-up](https://dash.cloudflare.com/sign-up)

1. Click the "Add" button on the top-right of the header bar
1. Click "Pages" on the drop-down menu that appears.
1. Click the "Connect to git" button.
1. Click the "Connect GitHub" button and follow the onscreen prompts.

> _Tutorial reference:_  
> [Deploy with Cloudflare Pages](https://developers.cloudflare.com/pages/framework-guides/deploy-a-jekyll-site/#deploy-with-cloudflare-pages)


# Part III: Customize your website settings

1. Navigate to your GitHub repository link (from Part I above).
1. Click on the `_config.yml` file link.
1. Click the pencil icon in the top-right menu bar to edit the file.
1. Modify the `_config.yml` file settings:
    1. Update the `title` value with the name of your website.
    1. Update the `description` value with a short description for your website

1. Click the "Commit changes" button and follow the onscreen prompts to save your modifications.
1. Navigate to your Cloudflare Pages project dashboard. You should see the changes applied automatically.


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
1. Navigate to your Cloudflare Pages project dashboard. You should see the changes applied automatically.

1. You can also modify and commit changes to the `about.markdown` file to include content specific to your website!

> See the [markdown](#markdown) references in the "further reading" section below to understand the file format syntax. You can view the `_posts/YYYY-MM-DD-SAMPLE.md` file in your repository as an example for how to write markdown.

# Part V: Deploy your site!
1. Navigate to your Cloudflare Pages project dashboard. 
1. Deploy your application!

<br/>
<br/>

---

# Further Reading

<a id="git" />
[**git**](https://docs.github.com/en/get-started/using-git/about-git) is a version control system popular amongst programmers for storing the complete revision history of a program. Over the past decade, it has also become popular among website content creators to keep a history of website content revisions over time. The most common method for using git is via a command-line terminal program. See this [git handbook](https://docs.github.com/en/get-started/using-git/about-git) for more information on the typical usage.


<a id="github" />
[**GitHub**](https://github.com) is a Microsoft cloud platform for storing and archiving git repositories. All content for a given website should be stored in a single git repository.


<a id="cloudflare" />
[**Cloudflare**](https://cloudflare.com) is a cloud provider with a free tier available for publishing websites!


<a id="github-pages" />
[**GitHub Pages**](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) - is a service provided by GitHub and is an alternate solution to Cloudflare.


<a id="jekyll" /><a id="front-matter" /><a id="liquid" />
[**Jekyll**](https://jekyllrb.com/) is a static website generator for creating and publishing websites and blogs. It uses [markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax), [front-matter](https://jekyllrb.com/docs/front-matter/), and [liquid](https://jekyllrb.com/docs/liquid/) to generate HTML files for your website.


<a id="markdown" />
[**Markdown**](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github) is an easy-to-read, easy-to-write language for formatting plain text. The [basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax) GitHub documentation is a great place to get started if you are new to the markdown format!
