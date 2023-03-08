from importlib.resources import as_file, files

def get_flatland():
    """Get path to example "Flatland" [1]_ text file.

    Returns
    -------
    pathlib.WindowsPath
        Path to file.

    References
    ----------
    .. [1] E. A. Abbott, "Flatland", Seeley & Co., 1884.
    """
    with as_file(files("pycount_sak.data").joinpath("flatland.txt")) as f:
        data_file_path = f
    return data_file_path