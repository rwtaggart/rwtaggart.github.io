---
layout: post
title:  "How do I learn to trust AI?"
date:   2026-02-07 08:12:12 -04:00
category: ai
---

A 10-hour curriculum for introducing the concepts and theory of AI, data analysis, and computer science.
{: .sub}


### Preface
Today, Generative AI (GenAI) tools interpret natural language to determine a set of actions that will generate a result.
Agentic AI represents a natural progression of this process. In the agent-based (i.e., "agentic") AI paradigm, 
agents are trained to perform a specific task, and they are invoked with a specific instruction.
Multiple agents may be combined to perform more complicated sets of actions.

Each section of this course provides a brief introduction to the topic, each of which is supported by a complete subdomain of mathematics, science, and engineering. Some sections are more focused on defining terminology and industry-specific jargon, while others teach the fundamental principles of a particular topic. 
Each section also contains further reading to inspire curiosity and continued learning.
The field of computer science provides the theory and practical basis for AI technology.
It is from this context that AI researches and developers create and deliver AI-enabled assistants, agents, and tools.


---

### Course Outline
1. **AI, GenAI and Agentic AI**
    1. What is GenAI and Agentic AI good at?
    1. Workslop and the pervasive fear of uncaught mistakes
    1. How do we mitigate the risk of making mistakes?

1. **Theory of Computer Science**
    1. Computer Architecture
    1. Computer Instructions
    1. Programs
    1. Assembly and Compilers
    1. C (Programming Language)
    1. Bits, Bytes, and YotaBytes!
    1. The Binary Number System
    1. Data Types and Encoding
    1. Algorithms and Data Structures
    1. Variables and Functions
    1. Control Flow
    1. Creating an algorithm  
        _"What is well-defined repeatable task that can I automate?"_
    1. Writing a program: "Hello, world!"

1. **Data Analysis**
    1. Introducing Python
    1. Intrepreters
    1. Packaging Modules
    1. Using free open source software
    1. Collecting Information
    1. Number crunching with `Pandas` and `numpy`
    1. Data visualization with `matplotlib`
    1. Analyzing data  
        _"What interesting ***trends*** exist within the data?"_
    1. Writing a program: "Hello, data."

1. **Using AI**
    1. Prompt Engineering
    1. Large-scale language models (LLMs)
    1. Agents
    1. MCP
    1. Creating with VS Code
    1. Troubleshooting
    1. Interpreting data  
        _"What underlying phenomena ***caused*** the observed data?"_
    1. Generating a program: "Hello, reason?"

1. **Managing AI Projects**
    1. Version Control Systems
    1. git
    1. GitHub
    1. Repository
    1. Artifact States
    1. Local and Remote
    1. Clone
    1. Stage, Commit, and Push
    1. Pull, Fetch, Merge, and Rebase
    1. Diff
    1. Using git in VS Code

---

## AI, GenAI, and Agentic AI

GenAI tools excel at generating information. Often the content is reasonable, but sometimes it is so far off-topic 
or incorrect that the end result is useless.
This type of fabricated content is the result of hallucinations. These types of errors are often caused by an AI model creating relationships from incompatible, incomplete, or incorrect information.

Our collective pervasive fear of AI stems from a simple question, _"how do I trust or verify information presented to me?"_
The answer to this question is identical to the title question of this article. Get curious, ask questions, learn the fundamental concepts, and build a solid foundation based on knowledge and experience. 
Our largest asset is our ability to learn. More importantly, it is our ability to unlearn.

At this juncture, we need to ask ourselves new versions of familiar questions. 
_"How do I know this information is real?"_
_"What assumptions were used to perform this analysis?"_
_"What mistakes or errors are common for this type of analysis?"_
_"What am I missing?"_

In the context of using AI generated information, we must understand how the models work, 
so we can understand where they veer away from the intended process, and then we can correct errors.

This requires understanding the fundamental behavior of digital information and computing.


---

## Theory of Computer Science

### Computer Architecture
Every computer is composed of the same types of components which are used as basic building blocks: arithmetic, memory, and networking.
Furthermore, every computer uses a predefined set of instructions that specify how to manipulate digital data stored in these components.
More complex modules such as computer-processing units (CPUs), graphics-processing units (GPUs), tensor-processing units (TPUs), field-gate programmable arrays (FPGAs), and microcontrollers 
are each created with a special combination of these blocks.
The main difference between these modules are how the components are designed, and how they interact together.
Some have more memory, some execute faster commands, and some handle higher network traffic data bandwidth.

The process of creating a flexible programmable machine was invented by Allen Turing,
which is why the computer science community refers to modern computers as _"Turing Machines."_


### Computer Instructions
A computer implements a specific computer architecture, which will typically fall into two categories: reduced instruction-set computer (RISC) or complex instruction-set computer (CISC).
Nearly every commercial computer uses a CISC architecture based processor of either x86 or Arm.

A computer instruction is the atomic processing unit of a computer. An instruction corresponds to a single atomic operation.

The arithmetic components implement instructions that perform mathematic operations: add, subtract, and multiply. These operate on both integer (i.e., fixed-point) and decimal (i.e. floating-point) numbers.

The memory components implement instructions that perform data manipulation operations: store, move, copy, and delete.

The networking components implement instructions that perform inter-process and inter-computer operations: encode, decode, encrypt, decrypt, transmit, and receive.


### Programs
A program is a sequence of computer instructions compiled into a particular order to manipulate information which yields a desired result.
All programs require a user interface (UI). Some programs are designed to interact only with each other via an API request. There are two categories of user interface paradigms in practice today: graphical user interface (GUI) and terminal user interface (TUI). Most people interact with the GUI window rendered by a program. A terminal-based program would run in a dedicated program shell application such as Microsoft Windows PowerShell.


### Assembly and Compilers
The assembly language is a basic programming language to describe a sequence of instructions to complete a task.
Modern-day programming languages leverage program compilers to interpret abstract statements and expressions, and translate them into specific computer instructions. This is where assembly code, and machine code, byte code are used.
The compiler that translates a set of program source code written in the assembly language syntax into machine-executable bytecode is called an "assembler."


### C
C is one of the oldest and most widely used programming languages.
It was designed as a systems programming language intended to provide direct access to computer instructions while providing higher-level constructs for adding layers of abstraction.
It became the defacto standard for writing operating systems, 
and it provided the basis for modern software development.

The C application binary interface (ABI) specification remains the standard for specifying 
binary-based program interfaces for compiled software. C++ is a related programming language,
and the C++ standard is a superset of the C programming language.
Therefore, every C program can be compiled as a valid C++ program, 
but a C++ program is not guaranteed to be a valid C program.

The compiler that compiles a C or C++ program into machine-readable binary bytecode is called a compiler.


### Bits, Bytes, and Yotabytes!
Transistors are the smallest atomic devices for storing and manipulating information in computers. 
They are are electronic semiconductor devices with a special property.
A transistor may hold the voltage across two wires in two distinct states: "on" and "off," 
or more precisely "high" and "low."

These two states provide the basis for the function of all Turing-based computers.
Multiple transistors can be wired together in parallel or in series to combine logical states and represent a wide spectrum of values.

A transistor in a computer stores the value of a bit; it is a physical implementation of this theoretical construct.

A bit is a mathematical binary construct with two valid states: "true" or "false."
This is the atomic unit of boolean algebra.

Many bits may be strung together, and computers arrange bits in logical groups of eight.
A byte is a group of eight bits that represent a single entity, also known as a "word."

A Yottabyte is one-septillion (i.e., 10^24) bytes, 10^24*8 bits, or 1 trillion Terabytes.

Boolean algebra is the domain of mathematics that describes logic. The basic logical operations are "not," "and," and "or." These are known as bitwise operators because the inputs and outputs of these functions are bits with possible values of either true or false. These operators can be combined to implement more complex functions described by integer algebra and other mathematical constructs.


### The Binary Number System
Numbers may be encoded by using multiple representations.
The binary number system has a base of 2. 
Every digit in each place has a value of 0 or 1, and the value of the position is a power of two.
Similarly, the decimal number system uses a base of 10. Valid digit values are 0-9, and each place multiples the digit by a power of 10.


### Data Types and Encoding
The direct result of the relationship between these numbers systems means there is a deterministic method to translate numbers between these systems.
Computers use bits to store information, bits are collected in groups to store binary numbers, and decimal numbers may be translated or encoded into binary numbers.

Therefore, computers have the ability to encode, decode, store, and operate on many types of data including single boolean bit values (true or false), binary numbers, integers, decimals, and even alphanumeric characters! Characters can be stored by using encoding rules such as ASCII or UTF-8. In this case, each character is assigned a number which is then stored in memory.

Furthermore, the field of computer science defines methods for implementing various algebraic and other mathematical operations for each of these data types as instructions executed by the computer.

All data stored in a computer is encoded as a digital value, where each digit is reduced to a group of bits, where each bit has a binary value of "high" or "low."
Therefore, there are natural phenomena that are difficult to represent or store using a computer. 
This presents a wide range of problems to be solved.
Further reading: representing digital and analog signals.


### Algorithms and Data Structure
An algorithm is a predefined complete sequence of steps.
Computer science is the study of implementing and executing instructions to perform an algorithm. 
Data structures are predefined constructs used to organize data in a logical manner to assist with the act of writing programs. 
These data structures often map to mathematical constructs such as arrays, sets, and maps.


### Variables and Functions
Programs can execute instructions that operate on stored instructions.
The algorithms used specify both the order of the instructions and the nature of the data structures being operated on.
Variables are used to denote which data are mutable and indicate which operations are valid for the type of data being stored.
Functions are used to organize related instructions through the use of statements, expressions, and variables.


### Control Flow
Programming languages define control structures that allow programs to implement conditional logic.
These structures are translated into computer instructions that allow the program to manipulate the behavior of the computer and program state.
Control Statements or expressions are used to specify how these conditions
affect the subsequent order of program statements and expressions executed by the program.
Examples include "if" and "else" conditional statements, and "for" and "while" loop expressions.


### Creating an algorithm
This is a practical example. Ask yourself the question, _"what is a well-defined repeatable task that I can automate?"_ Write down all the steps required to implement this task.
As a personal challenge, See if you can use the concepts from this chapter to write a program that implements this algorithm!


### Writing a program: "Hello, world!"
```c
// hello_world.c
// This is a simple C program
// REFERENCE:
// http://cppreference.com/w/c.html

#include <stdio.h>

int main() {
    printf("Hello, world!\n");
    return 0;
}
```

**Further reading:** 
[C Reference](https://cppreference.com/w/c.html) \|
[C tutorial](https://www.w3schools.com/c/index.php)


---

## Data Analysis
### Introducing Python
Python has become the de facto standard for data analysis and artificial intelligence.
It is used pervasively across industries, and it continues to grow in popularity.
The Python programming language is growing in popularity as a premier programming language for data science applications especially with the rapid adoption of AI assistants.
The Python development community maintains the foundation of modern artificial intelligence (AI) applications. The popularity of AI assistants is accelerating, and public perception and excitement of their potential seems boundless. 


### Interpreters
Python is an interpreted programming language. It requires a special program, the Python interpreter, to run. This is a prominent feature of the language, because it provides a dynamic runtime execution environment. This allows programmers to modify the program as it runs, and lazy-load modules as needed.

CPython is the C-based implementation of the Python language, and it is the default and most widely used implementation. This Python interpreter is a C program. Therefore, it is compatible with other C libraries that can be packaged and installed in a Python runtime environment. This provides an excellent balance between enabling developers to create fast optimized compiled C libraries and use them with flexible dynamic Python modules. 
This approach is the reason Python has become so popular for rapid application development and creating proofs-of-concept.


### Packaging Modules
The Python development community creates and maintains a broad set of open-source packages
published on the Python Package Index (PyPI). This ecosystem has fueled rapid development and adoption of the language as the defacto standard for data science.


### Using free and open source software
Free open source software is widely available and distributed for free.
There are many types of licenses that describe the terms of use for software.
Ensure any software being used complies with the needs and use case being developed. The [Open Source Initiative](https://opensource.org/licenses) contains more information about how to understand the terms and conditions 
of the various open source software licenses.


### Collecting Information
The single most important aspect of data science is preserving data integrity.
The quality of the source information is as important as the analysis.
Creating a data pipeline to sanitize and organize the data is the first step of 
data engineering.
There are several Python packages available to implement these types of activities.


### Number crunching with `Pandas` and `numpy`
`Pandas` and `numpy` are Python packages used for analyzing data.
They provide native support for multiple data file formats including Microsoft Excel.
They allow developers to write programs that operate on tabular data called "DataFrames,"
perform basic statistical operations, and run higher-order analysis.
Furthermore, the `Pandas` package is distributed with `matplotlib` for visualizing data.


### Data visualization with `matplotlib`
There are many packages available for rendering data plots and data visualization.
`matplotlib` is a versatile and popular package for rendering plots.
Visit the package documentation for tutorials and examples.


### Analyzing data
This is a practical example. Ask yourself the question,
"what is something I would like to learn from data?"
Once you identify a dataset to analyze, ask your self these questions. 
"What interesting trends exist within the data?"
"What types of analysis can I perform to help me understand what the data represents?"


### Writing a program: "Hello, data."
```python
# hello_data.py
# This is a simple Python program
# It will load a Microsoft Excel file into a DataFrame and render a plot
from pandas import DataFrame, read_excel
file_name = "./data.xlsx"
df = read_excel(file_name, sheet_name="Sheet 1", header=0)
print("Data column names: ", df.columns)
print("Table size: ", df.shape)
df.plot('COL_NAME_A', 'COL_NAME_B', title="Events over time", xlabel="Time (s)", ylabel="Count")
```


**Further Reading**:  
_Docs:_ [Python](https://python.org) \|
[Python Package Index (PyPI)](https://pypi.org) \|
[Python tutorial](https://docs.python.org/3/tutorial/index.html)  
_Packages:_ [pandas](https://pandas.pydata.org/) \|
[numpy](https://numpy.org/) \|
[matplotlib](https://matplotlib.org/)
_Reference:_ [Open Source Initiative](https://opensource.org/licenses)


---

## Using AI
### Prompt Engineering
Prompt engineering is a popular buzzword associated with many generative AI (GenAI) tools.
It implies a degree of sophistication and rigor which may not match reality.
A more appropriate phrase may be, _"prompt composition."_
This is the process of crafting a natural-language statement or expression
which is intended to instruct a model how to act, and what content to generate.
A prompt is the most common type of user interface to large-scale language models (LLMs) in use today.


### Large-scale language models (LLMs)
OpenAI took the world by storm in November of 2022 with the release of ChatGPT.
This signaled a major change in how the world would interact with software and computers.
ChatGPT is one of many large-scale language models (LLMs) available as a chat-based AI assistant. Now, Microsoft, Google, Amazon, Apple, IBM, and Anthropic have released popular models available for general use.
These AI enabled assistants include Copilot, Gemeni, Alexa, Siri, Watsonx, and Claude.

These models use special data encodings to assign relationships between the various properties and dimensions of each datum.
They rely on the data engineering pipeline and process to train reliable models and then perform inference tasks.


### Agents
Agentic AI represents a natural progression of AI technology.
Agents are trained to perform a specific task, and they are invoked with a specific instruction or prompt.
Multiple agents may be combined to perform more complicated sets of actions.


### MCP
The Model Context Protocol (MCP) is an open-source standard introduced by Anthropic in 2024 to connect AI models with external data, tools, and systems via a standardized client-server architecture. It acts as a universal bridge, allowing LLMs to securely access local files, databases, and APIs, shifting AI tools from a static knowledge paradigm to dynamic context-aware agents. MCP is a core factor causing the explosion of compatible AI agents and models and is fueling the rapid development and adoption of agentic AI.


### Creating with VS Code
Visual Studio Code is a text editor used by software developers to write software source code.
With the rapid adoption of AI tools, more developers are using the
"vibe-coding" technique to co-create code with AI by combining
prompt composition and software development techniques.
Many AI assistants and agents integrate directly with VS Code with extensions.


### Troubleshooting
The real magic happens when an error, mistake, or problem is found in generated content.
Determining how to set well-defined guardrails and constraints for AI tools will
help create a correct-by-construction environment.
In the event of identifying problems, we must figure out ways to help guide the AI system,
so it can automatically identify and correct the error.
This process of iterative troubleshooting is both the most frustrating and most rewarding aspect of software development.


### Intrepreting Data
This is a practical example. Ask yourself the question,
_"What underlying phenomena **caused** the data observed?"_
To answer this question, first identify a dataset to analyze; it may be the data set chosen from the example in the previous chapter.
Use the data analysis techniques specified to perform an initial 
analysis of the data, and create a mental model of the problem. Then ask yourself these questions,
_"How can I prompt an AI assistant to analyze the data and interpret the results?"_
_"How can I use an AI assistant or agent to generate a program that will help  me uncover new insights that may not be obvious to me now?"_
_"What will I need to troubleshoot problems or errors that I discover in the genreated content?"_

### Generating a program: "hello, _reason_?"
With a data set in mind, compose a prompt to help you solve a problem.

> DESCRIPTION  
> You are a data scientist and researcher supporting the business analysis team.
> 
> TASK  
> Generate a Python program that loads data from a source, performs a statistical analysis, and renders scatter and bar plots that show the relationship between the dimensions.

> ANALYSIS  
> Load the generated artifacts and create an executive summary describing the relationship between the data,
> and generate a set of recommendations for the next set of actions.
> List the assumptions implied by the dataset analysis, and enumerate a list of questions to consider.




**Further reading:**
[VS Code](https://code.visualstudio.com/) \|
[VS Code – Extensions Marketplace](https://marketplace.visualstudio.com/VSCode) \|
[Cline – VS Code AI Extension](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev)


---

## Managing AI Projects
With the adoption of AI assistants, managing versions of content is becoming ever more important.
AI projects require an established mechanism for reverting changes generated by automation.
Furthermore, understanding changes and tracking over time is an essential need.


### Version Control Systems
Creating, modifying, managing, and distributing shared content requires both effective collaboration and a rigorous mechanism for merging multiple contributions and modifications from multiple sources.
The software development community first encountered this problem since the introduction of network-based computing in the 1970s.
Since then the necessity of asynchronous collaboration has compounded in the age of digital information.
The answer to this problem is a version control system.

There are many version control systems and programs available for many use cases across industries.
The vast majority of free open-source software projects and communities have adopted git.
Version Control Systems (VCS) provide a solution that implements Source Code Management (SCM). Many developers use these terms interchangeably.


### git
git is the de facto standard for managing versions of source code and artifacts of a project. It is a version control system popular amongst programmers for storing the complete revision history of a program. Over the past decade, it has also become popular among website content creators to keep a history of website content revisions over time. The most common method for using git is via a command-line terminal program. See this [git handbook](https://docs.github.com/en/get-started/using-git/about-git) for more information on the typical usage.

git implements the distributed repository paradigm.
Every instance, or "clone" of the repository contains a complete set of the revision history.
This provides multiple benefits, including 
supporting offline development,
saving asynchronous changes,
and creating private local experiments.

git assumes it is the single source of truth.
Therefore it expects to retain and manage all versions of an artifact managed by git.
It is difficult to ensure coherency between artifacts stored in git and stored elsewhere. In other words, all versions of a file should be committed to the git repository, in order to capture all versions of the artifact.

The git program is a terminal user interface (TUI) that allows a user to perform git commands via a command-line execution shell program.
See the [git command reference](https://git-scm.com/docs) documentation for details of the available commands.


### GitHub
GitHub is a Microsoft cloud platform for storing and archiving git repositories. All content for a given project should be stored in a single git repository.


### Repository
A git repository is the storage location for managed files.
It contains a collection of "git refs" stored in the "git object database."
A git repository contains the complete revision history of the files managed.
git objects are used to store the repository revision history worktree.
A repository may contain multiple worktrees in the form of branches.

_Important note:_ git commit objects are immutable. Revisions can not be changed without modifying downstream child commit objects.


### Artifact States
git assigns three possible states for managed files:
_modified, staged,_ and _committed._

git uses files and directories (i.e., _"folders"_) to manage the files in each of these three states.
The _working directory_ contains the current active files with the latest version of the files being developed.
This is the current project directory.

git keeps track of the "staged" files in the "staging area." This is accessible via the git commands below.

git stores all committed file versions in the repository in the .git directory located as a subdirectory in the active project directory. Developers should only interact with the .git directory by using the commands provided by the git program.


### Local and Remote
git is a distributed version control system.
git commands operate on a local copy (i.e., "clone") of the repository.
git can also interact with remote repositories such as repositories hosted on GitHub.


### Clone
Clone is the act of creating a local copy from a remote repository.
For example, a developer would download a local copy of a remote GitHub repository with the `git clone` command.


### Stage, Commit, and Push

| Command | Action |
| --: | --- |
| `git add` | Add untracked files or unstaged changes to the staging area. |
| `git commit` | Commit staged changes and files to the repository history worktree |
| `git push` | Push local commit branch worktree to the remote branch. |


### Pull, Fetch, Merge, and Rebase

| Command | Action |
| --: | --- |
| `git pull` | Perform a `git fetch` followed by `git merge` or `git rebase`. |
| `git fetch` | Fetch changes from a remote repository without modifying any local branches. |
| `git merge` | Join two git branch histories together. |
| `git rebase` | Apply changes from one branch onto the tip of another. |

See the _Combine Diverged Branches_ section of the [Git Cheat Sheet](https://git-scm.com/cheat-sheet) for examples on the differences between `merge` and `rebase`.


### Diff
git provides basic and advanced methods for viewing change differences between commit "patches" of files. See the _"Checking the Status of Your Files"_ section of the [Pro Git book](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) for examples.


### Using git in VS Code
VS Code provides built-in support for managing source code with git repositories. The VS Code docs provide more details on how to interact with git
in the VS Code editor.
This is one example of many graphical user interfaces (GUIs) that allow 
users to interact with git repositories and perform git actions, without requiring a command-line interface (CLI).

The VS Code git interface provides an intuitive method for executing git commands.


**Further Reading:**  
[git (docs)](https://git-scm.org) \|
[git (command reference)](https://git-scm.com/docs) \|
[git (about)](https://docs.github.com/en/get-started/using-git/about-git) \|
[Pro Git book](https://git-scm.com/book/en/v2) \|
[git (glossary)](https://git-scm.com/docs/gitglossary) \|
[git handbook](https://docs.github.com/en/get-started/using-git/about-git) \|
[GitHub](https://github.com) \|
[git in VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview)


<br/>
<strong class="center">\* \* \*</strong>

More than 60 years ago, the great American song writer Bob Dylan wrote,
_"these times, they are a changin'."_
So, you can let crippling fear and self-doubt control you.
Or, you can get to work.

_Ironically, this post was created without any use of AI tools._
{: .sub}

<head>
<style>
    body {
        /* font-family: "Helvetica Neue", "Fira Sans", sans-serif; */
		text-align: justify;
    }
    .center {
        display: block;
        text-align: center;
        font-size: 1.2em;
    }
    .sub {
        color: #808080;
    }

    h2 {
        margin-top: 12pt;
        color: #1a5fb4;
    }
</style>
</head>
