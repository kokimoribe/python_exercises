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
1. **Run the Setup Cell**: Before starting the exercises, you **must** run the first code cell (marked 'Setup'). 
   - This cell installs and configures the testing framework
   - The first execution may take 1-2 minutes as Google Colab prepares your execution environment
   - You'll know it's ready when you see a checkmark ✓ appear on the cell

#### Running the Exercises
1. Each exercise contains:
   - A function to implement
   - A docstring explaining what to do
   - Test cases to verify your solution
2. Write your code in place of the `pass` statement
3. Run the cell to check if your solution passes the tests
4. A ✓ appears when all tests pass
"""

# Setup code for ipytest
IPYTEST_SETUP = """#@title Run this first!!!
try:
    import ipytest
except ImportError:
    !pip install ipytest
    import ipytest
ipytest.autoconfig()"""

def py_to_notebook(py_file: Path, notebook_file: Path):
    """
    Convert a Python file with exercise sections into a Jupyter notebook.
    Each section marked with '#################################################'
    will become its own cell, with any standalone comments merged into their following code.
    
    Args:
        py_file (Path): Path to source Python file
        notebook_file (Path): Path where notebook should be saved
    """
    try:
        # Read the Python file
        with open(py_file, "r", encoding="utf-8") as f:
            content = f.read()

        # Split the file into sections based on the delimiter
        sections = [s.strip() for s in content.split("#################################################")]
        
        # Create a new Jupyter notebook
        notebook = nbformat.v4.new_notebook()
        cells = []

        # Add documentation markdown cell with formatted Colab link
        notebook_name = notebook_file.name
        cells.append(nbformat.v4.new_markdown_cell(COLLAB_BADGE.format(notebook_name=notebook_name)))
        cells.append(nbformat.v4.new_markdown_cell("### README"))
        cells.append(nbformat.v4.new_markdown_cell(NOTEBOOK_DOCS))

        # Add setup cell for ipytest
        cells.append(nbformat.v4.new_markdown_cell("### Exercises"))
        cells.append(nbformat.v4.new_code_cell(IPYTEST_SETUP))

        # Process each section
        for i, section in enumerate(sections):
            if not section.strip():  # Skip empty sections
                continue
                
            if i == 0:  # First non-empty section becomes markdown header
                cell = nbformat.v4.new_markdown_cell(section.replace("#", "").strip())
                cells.append(cell)
            else:
                # Split into lines and get the title
                lines = section.strip().split('\n')
                if lines[0].strip().startswith('#'):
                    # Extract title from the comment block
                    title = lines[0].strip('# \n')
                    # Remove the title line
                    lines = lines[1:]
                
                # Only create cell if there's content after removing title
                if lines:
                    # Add title directive and ipytest magic
                    code = f"#@title {title}\n%%ipytest\n\n" + '\n'.join(lines).strip()
                    cells.append(nbformat.v4.new_code_cell(code))

        notebook.cells = cells

        # Ensure the output directory exists
        notebook_file.parent.mkdir(parents=True, exist_ok=True)

        # Write the notebook to file
        with open(notebook_file, "w", encoding="utf-8") as f:
            nbformat.write(notebook, f)

        print(f"Successfully converted {py_file} to {notebook_file}")
        
    except FileNotFoundError:
        print(f"Error: Could not find the file {py_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Define source and output directories
    src_dir = Path("src")
    notebooks_dir = Path("notebooks")

    # Create notebooks directory if it doesn't exist
    notebooks_dir.mkdir(exist_ok=True)

    # Find all Python files in src directory
    python_files = src_dir.glob("*.py")

    # Convert each file
    for py_file in python_files:
        # Create corresponding notebook path
        notebook_file = notebooks_dir / py_file.with_suffix('.ipynb').name
        py_to_notebook(py_file, notebook_file)

if __name__ == "__main__":
    main()
