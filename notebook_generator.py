import nbformat
from pathlib import Path

# Documentation for the notebook
COLLAB_BADGE = """[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/kokimoribe/python_exercises/blob/publish/notebooks/{notebook_name})"""
NOTEBOOK_DOCS = """
If you're not familiar with notebooks:

https://chatgpt.com/share/6784782a-d7ac-8010-9dcf-9b5141e2a4ea


#### Key information

- **Execute a Cell**: 
  - `Shift+Enter` to execute and move to next cell
  - `Ctrl+Enter` (Windows) or `⌘+Enter` (Mac) to execute and stay on current cell
- **Edit a Cell**: Simply click inside any code cell to start editing
- **Add a Cell**: Use the + button in the top menu or press `Ctrl+M B` (Windows) or `⌘+M B` (Mac)
- **Dark Mode**: 
  1. Click on 'Tools' in the top menubar
  2. Select 'Settings'
  3. Choose 'Theme' → 'Dark'

#### Important First Steps
1. **Run the Setup Cell**: Before starting any exercise notebook, you **must** run the first code cell (marked 'Run this first!!!'). 
   - This cell installs and configures the testing framework
   - The first execution may take ~10 seconds as Google Colab prepares your execution environment
   - You'll know it's ready when you see a checkmark ✓ appear on the cell

#### Running the Exercises
1. Each exercise contains:
   - A function to implement
   - A docstring explaining what to do
   - Test cases to verify your solution
2. Write your code in place of the `pass` statement
3. Run the cell to check if your solution passes the tests
4. A ✓ appears when all tests pass

### Available Notebooks
"""

# Documentation for exercise notebooks
EXERCISE_DOCS = """Need help? Visit the [Home](https://colab.research.google.com/github/kokimoribe/python_exercises/blob/publish/notebooks/home.ipynb) notebook for detailed instructions"""

# Setup code for ipytest and any custom setup
IPYTEST_SETUP = """#@title Run this first!!!
try:
    import ipytest
except ImportError:
    !pip install ipytest
    import ipytest
ipytest.autoconfig()

# Custom setup code for this notebook (if any)
{custom_setup}"""

def generate_home_notebook(notebooks_dir: Path):
    """Generate a home notebook with links to all exercise notebooks."""
    notebook = nbformat.v4.new_notebook()
    cells = []
    
    # Add documentation
    cells.append(nbformat.v4.new_markdown_cell(NOTEBOOK_DOCS))
    
    # Add links to all notebooks
    links = []
    for nb_file in sorted(notebooks_dir.glob("*.ipynb")):
        if nb_file.name != "home.ipynb":
            name = nb_file.stem.replace("_", " ").title()
            colab_url = f"https://colab.research.google.com/github/kokimoribe/python_exercises/blob/publish/notebooks/{nb_file.name}"
            links.append(f"- [{name}]({colab_url})")
    
    cells.append(nbformat.v4.new_markdown_cell("\n".join(links)))
    
    notebook.cells = cells
    
    # Write the notebook
    home_file = notebooks_dir / "home.ipynb"
    with open(home_file, "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)
    
    print(f"Generated home notebook at {home_file}")

def split_into_sections(content: str) -> list[str]:
    """Split file content into sections based on '# EXERCISE:' and '# Setup' markers."""
    lines = content.split('\n')
    sections = []
    current_section = []
    
    for line in lines:
        if line.strip().startswith('# EXERCISE:') or line.strip().startswith('# Setup'):
            if current_section:  # Save previous section if it exists
                sections.append('\n'.join(current_section))
                current_section = []
        current_section.append(line)
    
    if current_section:  # Add the last section
        sections.append('\n'.join(current_section))
    
    return sections

def py_to_notebook(py_file: Path, notebook_file: Path):
    """
    Convert a Python file into a Jupyter notebook.
    Each section starting with '# EXERCISE:' or '# Setup' becomes its own cell.
    """
    try:
        # Read the Python file
        with open(py_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Split into sections
        sections = split_into_sections(content)
        
        # Create notebook
        notebook = nbformat.v4.new_notebook()
        cells = []

        # Add documentation cells
        notebook_name = notebook_file.name
        cells.append(nbformat.v4.new_markdown_cell(COLLAB_BADGE.format(notebook_name=notebook_name)))
        cells.append(nbformat.v4.new_markdown_cell(EXERCISE_DOCS))

        # Process sections
        custom_setup = ""
        for section in sections:
            if section.strip().startswith('# Setup'):
                # Extract setup code
                custom_setup = '\n'.join(section.split('\n')[1:])  # Skip the "# Setup" line
            elif section.strip().startswith('# EXERCISE:'):
                # Extract title
                first_line = section.split('\n')[0]
                title = first_line.replace('# EXERCISE:', '').strip()
                # Create exercise cell
                code = f"#@title {title}\n%%ipytest\n\n" + '\n'.join(section.split('\n')[1:])
                cells.append(nbformat.v4.new_code_cell(code))

        # Add setup cell after documentation but before exercises
        setup_code = IPYTEST_SETUP.format(custom_setup=custom_setup)
        cells.insert(2, nbformat.v4.new_code_cell(setup_code))

        notebook.cells = cells

        # Write the notebook
        notebook_file.parent.mkdir(parents=True, exist_ok=True)
        with open(notebook_file, "w", encoding="utf-8") as f:
            nbformat.write(notebook, f)

        print(f"Successfully converted {py_file} to {notebook_file}")
        
    except Exception as e:
        print(f"An error occurred with {py_file}: {str(e)}")

def main():
    # Setup directories
    src_dir = Path("src")
    notebooks_dir = Path("notebooks")
    notebooks_dir.mkdir(exist_ok=True)

    # Convert Python files to notebooks
    for py_file in src_dir.glob("*.py"):
        notebook_file = notebooks_dir / py_file.with_suffix('.ipynb').name
        py_to_notebook(py_file, notebook_file)
    
    # Generate home notebook
    generate_home_notebook(notebooks_dir)

if __name__ == "__main__":
    main()
