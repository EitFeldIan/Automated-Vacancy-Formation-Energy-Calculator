def replaceAtom(atom_index, new_element, poscar_path="POSCAR"):
    # Backup original POSCAR
    with open(poscar_path, 'r') as f:
        lines = f.readlines()
        
    with open(f"{poscar_path}_old", 'w') as f_backup:
        f_backup.writelines(lines)
    
    # Original function content continues...
    elem_line = 5
    count_line = 6
    coord_start = 8
    
    elements = lines[elem_line].strip().split()
    counts = list(map(int, lines[count_line].strip().split()))
    
    total_atoms = sum(counts)
    if atom_index < 1 or atom_index > total_atoms:
        raise ValueError(f"Atom index must be between 1 and {total_atoms}")
    
    cumulative = 0
    elem_idx = 0
    for idx, count in enumerate(counts):
        cumulative += count
        if atom_index <= cumulative:
            elem_idx = idx
            break
    
    counts[elem_idx] -= 1
    
    if new_element in elements:
        new_elem_idx = elements.index(new_element)
        counts[new_elem_idx] += 1
    else:
        elements.append(new_element)
        counts.append(1)
    
    target_line_idx = coord_start + (atom_index - 1)
    old_coord = lines.pop(target_line_idx)
    
    # Assuming no element symbol in coordinates, 
    # if they're there, you may remove additional space-separated tokens exceeding 'x y z'
    
    lines.append(old_coord)
    
    lines[elem_line] = ' '.join(elements) + '\n'
    lines[count_line] = ' '.join(map(str, counts)) + '\n'
    
    with open(poscar_path, 'w') as f:
        f.writelines(lines)

