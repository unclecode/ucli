# UCLI - Unclecode CLI Collection

A collection of powerful CLI tools to enhance developer workflow.

## Available Commands

| Command | Description | Config Required |
|---------|-------------|-----------------|
| `gitit` | AI-powered commit message & changelog generator | None |
| `gitis` | GitHub issues analyzer and tracker | `GITHUB_PERSONAL_ACCESS_TOKEN` |

## Installation

``` bash
# Install latest version from GitHub
pip install git+https://github.com/unclecode/ucli.git

# Update to latest version
pip install --upgrade git+https://github.com/unclecode/ucli.git
```

## Configuration

### GitHub Token
Required only for `gitis`:

``` bash
# Add to your ~/.bashrc or ~/.zshrc
export GITHUB_PERSONAL_ACCESS_TOKEN="your-token-here"
```

## Command Usage Guide

### gitit - Git Commit Helper
Analyzes uncommitted changes and generates AI-powered commit messages and changelogs.

Output Location: `.ucli/` directory in your project
- `.ucli/changelog.md`: Formatted changelog in Markdown
- `.ucli/changelog.json`: Structured data for programmatic use

``` bash
# From your git repository root:

# 1. Make your changes
git add file1.py file2.js

# 2. Generate commit message & changelog
gitit

# 3. Optionally review generated files in .ucli/
# 4. Apply the commit with generated message
gitit --commit

# Additional options:
gitit --branch      # Analyze changes since branching from main
gitit --help        # Show all available options
```

### gitis - GitHub Issues Manager
Analyzes and tracks GitHub issues for your repository.

Output Location: `.ucli/git_issues.md`

``` bash
# Must be run from a git repository directory

# List all open issues
gitis --state open

# Find issues with specific keywords
gitis --keywords bug feature

# Find issues where you were last commenter
gitis --owner-last

# Additional options:
gitis --help        # Show all available options
```

## Project Organization

``` plaintext
.ucli/                      # Created in your project directory
├── changelog.md           # Latest generated changelog
├── changelog.json        # Structured changelog data
└── git_issues.md        # Repository issues report

your-project/              # Your git repository
├── .ucli/               # UCLI working directory
├── .git/                # Git directory
└── ...                  # Your project files
```

## Development Setup

``` bash
# Clone the repository
git clone https://github.com/unclecode/ucli.git
cd ucli

# Install in development mode
pip install -e .
```

## Adding UCLI to Your Workflow

1. Initialize your git repository (if not already done)
  ```bash
  git init