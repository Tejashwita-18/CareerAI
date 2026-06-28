def extract_jd_text(file_path: str) -> str:
    """
    Extract text from a job description file.

    Parameters:
        file_path: Path to the job description file

    Return:
        str: Job description text
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Job description file not found: {file_path}")
    
    except Exception as e:
        raise Exception(f"Error while reading job description: {e}")
