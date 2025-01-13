import nbformat
from pathlib import Path

def py_to_notebook(py_file, notebook_file):
    """
    Convert a Python file with exercise sections into a Jupyter notebook.
    Each section marked with '#################################################'
    will become its own cell, with any standalone comments merged into their following code.
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
        setup_code = "!pip install ipytest\n\nimport ipytest\nipytest.autoconfig()"
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
                # Add %%ipytest magic to the beginning of each exercise cell
                section_with_magic = "%%ipytest\n\n" + section.strip()
                cell = nbformat.v4.new_code_cell(section_with_magic)
                cells.append(cell)

        notebook.cells = cells

        # Ensure the output directory exists
        Path(notebook_file).parent.mkdir(parents=True, exist_ok=True)

        # Write the notebook to file
        with open(notebook_file, "w", encoding="utf-8") as f:
            nbformat.write(notebook, f)

        print(f"Successfully converted {py_file} to {notebook_file}")
        
    except FileNotFoundError:
        print(f"Error: Could not find the file {py_file}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # List of Python files to convert
    python_files = [
        "exercises.py",
        "2025_01_12.py",
    ]

    # Convert each file
    for py_file in python_files:
        notebook_file = Path(py_file).with_suffix('.ipynb')
        py_to_notebook(py_file, notebook_file)
