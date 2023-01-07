file = open('./7/input.txt', 'r')
data = file.readlines()

# parse row
# do command
# cd will move up or down tree
# ls will list nodes
# if dir make dir node
# if int make file node
# once tree is mapped, traverse for file size


class Node:
    def __init__(self, parent, name, size=None, filetype=None, children=None):
        self.parent = parent
        self.name = name
        self.size = size
        self.filetype = filetype
        self.children = children


def find_child_dir_by_name(children, name):
    for child in children:
        if child.name == name and child.size is None:
            return child


def build_file_tree(data):
    root_dir = Node(None, '/', None, None, [])
    current_dir = root_dir

    i = 1
    while i < len(data):
        row = data[i].strip()
        if row[0] == '$':
            command_split = row.split(' ')
            if command_split[1] == 'cd':
                if command_split[2] == '..':
                    current_dir = current_dir.parent
                else:
                    current_dir = find_child_dir_by_name(
                        current_dir.children, command_split[2])
        else:
            dir_split = row.split(' ')
            if dir_split[0] == 'dir':
                dir = Node(current_dir, dir_split[1], None, None, [])
                current_dir.children.append(dir)
            else:
                filename = dir_split[1].split('.')
                filetype = filename[1] if len(filename) > 1 else None
                file = Node(current_dir, filename[0], int(
                    dir_split[0]), filetype, None)
                current_dir.children.append(file)

        i += 1

    return root_dir


print(build_file_tree(data))
