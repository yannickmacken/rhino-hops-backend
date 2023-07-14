import compute_rhino3d.Util
import compute_rhino3d.Grasshopper as gh
import rhino3dm
import json
from typing import Any, List


def find_values(json_repr: Any, key_to_find: str, value_to_find: str) -> List[str]:
    """
    Recursively search through a JSON-like Python dictionary and find all keys that contain a specific value.

    Args:
        json_repr (Any): Python object (dictionary or list of dictionaries) that represent JSON data.
        key_to_find (str): The key to search for.
        value_to_find (str): The value to search for.

    Returns:
        List[str]: List of found values.
    """
    results = []

    def _decode_dict(a_dict: Any):
        """
        Decode a dictionary or list, searching for a specific key-value pair.
        """
        try:
            a_dict = a_dict.items()
        except AttributeError:  # a_dict is not a dict
            pass
        else:
            for key, value in a_dict:
                if key == key_to_find and value_to_find in value:
                    results.append(value)  # found key-value pair, add to results
                if isinstance(value, dict):
                    _decode_dict(value)  # recursively search in nested dict
                elif isinstance(value, list):
                    for item in value:  # recursively search in lists
                        _decode_dict(item)

    _decode_dict(json_repr)
    return results


def append_to_tree(tree: gh.DataTree, path: dict, value: str):
    """
    Append a value to a Grasshopper DataTree.

    Args:
        tree (gh.DataTree): The DataTree to append to.
        path (dict): The path to the new branch.
        value (str): The value to append.
    """
    tree.Append([path], [value])


def main():
    # Set the compute_rhino3d.Util.url to your server
    compute_rhino3d.Util.url = 'http://localhost:6500/'

    # Create DataTree for each input
    input_trees = []
    tree = gh.DataTree("count")
    append_to_tree(tree, {0}, "6")
    input_trees.append(tree)

    tree = gh.DataTree("truss_height")
    append_to_tree(tree, {0}, "6")
    input_trees.append(tree)

    tree = gh.DataTree("truss_depth")
    append_to_tree(tree, {0}, "18")
    input_trees.append(tree)

    tree = gh.DataTree("truss_width")
    append_to_tree(tree, {0}, "18")
    input_trees.append(tree)

    tree = gh.DataTree("spans")
    append_to_tree(tree, {0}, "14")
    input_trees.append(tree)

    tree = gh.DataTree("void_spans")
    append_to_tree(tree, {0}, "1")
    input_trees.append(tree)

    # Evaluate the Grasshopper definition
    output = gh.EvaluateDefinition('C:\\Users\\viktor\\OneDrive - VIKTOR\\Hops grasshopper integration\\truss.gh', input_trees)

    # Handle any errors or warnings
    errors = output['errors']
    if errors:
        print('ERRORS')
        for error in errors:
            print(error)
    warnings = output['warnings']
    if warnings:
        print('WARNINGS')
        for warning in warnings:
            print(warning)

    # Create a new rhino3dm file
    file = rhino3dm.File3dm()

    archive3dm_data_values = find_values(output, 'data', 'archive3dm')
    for value in archive3dm_data_values:
        print(value)
        obj = rhino3dm.CommonObject.Decode(json.loads(value))
        print(obj)
        file.Objects.AddBrep(obj)  # Add your Brep object to the file

    # Save the file to your desired location
    file.Write('C:\\Users\\viktor\\OneDrive - VIKTOR\\Hops grasshopper integration\\output.3dm', 7)
    print('wrote 3dm file to folder')


if __name__ == "__main__":
    main()
