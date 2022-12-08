class Directory:
    def __init__(self, name, ID, parent_ID, children_IDs, children_names, files):
        self.name = name
        self.ID = ID
        self.parent_ID = parent_ID
        self.children_IDs = children_IDs
        self.children_names = children_names
        self.files = files

    def __repr__(self):
        return f"Directory(Name: {self.name}, ID: {self.ID}, Parent ID: {self.parent_ID}, Children IDs: {[str(x) for x in self.children_IDs]}, Files: {[str(x) for x in self.files]})"


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f"File({self.name}, {self.size})"


def get_directories(terminal_output):
    cwd = Directory("/", 0, None, [], [], [])
    directories = {0: cwd}

    id_counter = 1

    for line in terminal_output[1:]:
        if line[:3] == "dir":
            dirname = line[4:]
            cwd.children_IDs.append(id_counter)
            cwd.children_names.append(dirname)
            directories[id_counter] = Directory(dirname, id_counter, cwd.ID, [], [], [])
            id_counter += 1
        elif line[:4] == "$ cd":
            new_dir = line[5:]
            if new_dir == "..":
                cwd = directories[cwd.parent_ID]
            else:
                lookup = dict(zip(cwd.children_names, cwd.children_IDs))
                cwd = directories[lookup[new_dir]]
        elif line[:4] == "$ ls":
            continue
        else:
            filsize, filname = line.split(" ")
            cwd.files.append(File(filname, filsize))

    return directories


def get_directory_size(directories, directory_id):
    directory = directories[directory_id]
    file_sizes = sum([int(file.size) for file in directory.files])
    children_ids = directory.children_IDs

    for child_ID in children_ids:
        file_sizes += get_directory_size(directories, child_ID)

    return file_sizes


def get_size_of_directory_to_delete(
    directory_sizes, size_needed=30000000, total_capacity=70000000
):
    outermost = directory_sizes[0]
    unused_space = total_capacity - outermost
    space_needed_to_delete = size_needed - unused_space
    relevant_dirs = {
        k: v for k, v in directory_sizes.items() if v >= space_needed_to_delete
    }
    return sorted(relevant_dirs.values())[0]


if __name__ == "__main__":
    with open("data/day07.txt") as f:
        terminal_output = [x.strip() for x in f.readlines()]

        directories = get_directories(terminal_output)
        directory_sizes = dict(
            zip(
                list(directories.keys()),
                [get_directory_size(directories, id) for id in directories],
            )
        )

        print(
            "Part 1:",
            sum([dsize for dsize in list(directory_sizes.values()) if dsize <= 100000]),
        )
        print("Part 2:", get_size_of_directory_to_delete(directory_sizes))
