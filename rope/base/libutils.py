"""A few utilities for using rope as a library"""
import os.path

import rope.base.project


def path_to_resource(project, path, type=None):
    """Get the resource at path

    You only need to specify `type` if `path` does not exist.  It can
    be either 'file' or 'folder'.  If the type is `None` it is assumed
    that the resource already exists.

    Note that this function uses `Project.get_resource()`,
    `Project.get_file()`, and `Project.get_folder()` methods.

    """
    path = os.path.abspath(path)
    project_path = path
    if path.startswith(project.address):
        project_path = path[len(project.address):].lstrip('/' + os.sep)
    else:
        project = rope.base.project.get_no_project()
    if type is None:
        return project.get_resource(project_path)
    if type == 'file':
        return project.get_file(project_path)
    if type == 'folder':
        return project.get_folder(project_path)
    return None