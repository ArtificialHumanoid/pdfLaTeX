import subprocess
from utilities.management_of.resources.operating_system.paths.path_management import relative_to_absolute_path
from utilities.management_of.resources.data.process.without_transformation.persistence.storage.storage_management import open_string


def compile(path):
    source = open_string(relative_to_absolute_path(path))
    end_trigger = r"\end{document}"
    if not source[-len(end_trigger):] == end_trigger:
        raise ValueError
    subprocess.run(["pdflatex", source])


if __name__ == "__main__":
    path = "./test.tex"
    compile(path=path)
