import nbformat
from pathlib import Path

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

        # Add setup cell for ipytest
        setup_code = """try:
    import ipytest
except ImportError:
    !pip install ipytest
    import ipytest
ipytest.autoconfig()"""
        setup_cell = nbformat.v4.new_code_cell(setup_code)
        cells.append(setup_cell)

        # Process each section
        for i, section in enumerate(sections):
            if not section.strip():  # Skip empty sections
                continue
                
            if i == 0:  # First non-empty section becomes markdown header
                cell = nbformat.v4.new_markdown_cell(section.replace("#", "").strip())
                cells.append(cell)
            else:
                # Split into lines and skip the section title line
                lines = section.strip().split('\n')
                if lines[0].strip().startswith('#'):
                    lines = lines[1:]
                
                # Only create cell if there's content after removing title
                if lines:
                    code = "%%ipytest\n\n" + '\n'.join(lines).strip()
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
