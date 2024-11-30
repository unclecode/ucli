# UCLI - Unclecode CLI Collection

A collection of powerful CLI tools for developers.

## Tools

- `gitboss`: Generate smart commit messages and changelogs using AI
- `ghissues`: Analyze GitHub issues and PRs with advanced filtering

## Installation

``` bash
# Install latest version from GitHub
pip install git+https://github.com/unclecode/ucli.git

# Update to latest version
pip install --upgrade git+https://github.com/unclecode/ucli.git
```

## Configuration

### GitHub Token
For `ghissues` you need to set your GitHub token:

``` bash
# Add to your ~/.bashrc or ~/.zshrc
export GITHUB_PERSONAL_ACCESS_TOKEN="your-token-here"
```

## Usage Examples

### gitboss
Generate smart commit messages and changelogs:

``` bash
# Generate changelog for current changes
gitboss

# Generate and commit changes
gitboss --commit

# Generate changelog for branch changes
gitboss --branch
```

### ghissues
Analyze GitHub issues:

``` bash
# List all open issues
ghissues --state open

# Find issues with specific keywords
ghissues --keywords bug feature

# Find issues where you were last commenter
ghissues --owner-last

# Save to custom file
ghissues --output my-issues.md
```

## Development Setup

``` bash
# Clone the repository
git clone https://github.com/unclecode/ucli.git
cd ucli

# Install in development mode
pip install -e .
```

## Structure

``` plaintext
ucli/
├── bin/
│   ├── gitboss
│   └── ghissues
├── requirements.txt
├── setup.py
└── README.md
```

## License

Apache License 2.0

## Author

[Unclecode](https://github.com/unclecode)
Follow me at [X](https://x.com/unclecode)