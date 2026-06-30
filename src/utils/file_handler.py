import os
from pathlib import Path
import tempfile

def save_uploaded_file_to_temp(uploaded_file) -> str:
    """
    Saves a streamlit UploadedFile to a temporary file.

    Returns a temporary file path. 
    """

    suffix = Path(uploaded_file.name).suffix

    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=suffix
    ) as temp_file:
        temp_file.write(uploaded_file.getbuffer())

    return temp_file.name

def delete_temp_file(file_path: str) -> None:
    """
    Delete a temporary file.
    """

    if os.path.exists(file_path):
        os.remove(file_path)
