def rewrite_file_without_line(file_path, name_to_leave):
    found_name_to_leave = False
    with open(file_path, "r") as file:
        lines = file.readlines()
        new_lines = []
        for line in lines :
            name = take_line_give_name(line)
            name = " ".join(name)
            if not name == name_to_leave :
                new_lines.append(line)
            else :
                found_name_to_leave = True
        if not found_name_to_leave :
            return -1
    with open(file_path, "w") as file:
        file.writelines(new_lines)
    return 1

def take_line_give_name(line):
    try:
        *name, _, _, _, _, _, _, _ = line.strip().split()
        return name
    except ValueError:
        *name, _ = line.strip().split()
        return name