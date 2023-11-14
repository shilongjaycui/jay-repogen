# `jay-repogen`

A project template that generates boilerplate Python projects for you.

## Description

In my opinion, the biggest value this project template creates is that it <font color="green">**enables you to validate your business ideas very quickly by freeing you up from ever having to set up experiments/[POC](https://en.wikipedia.org/wiki/Proof_of_concept)s from scratch**</font>.

### What

- **What was my motivation for building this project?** To solidify my learnings from a Udemy course, [Taking Python to Production: A Professional Onboarding Guide](https://www.udemy.com/course/setting-up-the-linux-terminal-for-software-development/).
- **What did I learn?**
  - How to configure Z shell
  - How to manage Python versions with `pyenv`
  - How to manage linting tools with `pre-commit`
  - How to package Python software
  - How to publish a Python package to [PyPI](https://pypi.org/)
  - How to set up Python projects with `cookiecutter`
  - How to do shell scripting
  - How to automate GitHub operations with [GitHub CLI](https://cli.github.com/)
- **What makes my project stand out?** You can customize it to suit your needs and use it for the rest of your career.
- **What challenges did I face?** I've had to fix bugs that came out of no where and involved many different tools & technologies.
- **What features do I hope to implement in the future?** Be able to generate different types of Python projects; for example:
  - an AWS CDK app
  - a data pipeline
  - a machine learning model

### Why

- **Why did I build this project?** Just so I don't have to set up Python projects from scratch ever again.
- **What problem does it solve?** It saves you the manual labor of setting up Python projects from scratch.
- **Why did I use the technologies I used?** Because I just learned about them in the aforementioned [Udemy course](https://www.udemy.com/course/setting-up-the-linux-terminal-for-software-development/).

## Installation

Clone the repo in your terminal:

```bash
git clone git@github.com:shilongjaycui/jay-repogen.git
```

## Usage

Move into the repo folder:

```bash
cd jay-repogen
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

```bash
source venv/bin/activate
```

Install dependencies:

```bash
make install
```

(optional) Make sure the repo isn't broken:

```bash
make lint
```

```bash
make test
```

Generate your boilderplate Python project.

```bash
make generate-project
```

Now that you have your project generated in the `/sample` folder, feel free to move it somewhere else and start playing around with it.

## License

[MIT](https://choosealicense.com/licenses/mit/)
