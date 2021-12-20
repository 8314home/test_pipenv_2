
def dfs_call_to_fill(mg, m_to_e_map, res):
    if mg in res:
        return res.get(mg)
    mg_s_direct_repotee = m_to_e_map.get(mg)
    print(f'{mg} has direct_reportee -{mg_s_direct_repotee}')
    if mg_s_direct_repotee: # now find indirect reportees
        for x in mg_s_direct_repotee.copy():   # copy is needed for reference
            indr_l = dfs_call_to_fill(x, m_to_e_map, res)
            if indr_l:
                mg_s_direct_repotee.extend(indr_l)
            print(f'{x} has direct_reportee added, now mg_s_direct_repotee is -{mg_s_direct_repotee}')
    # save final list of mg
    res[mg] = mg_s_direct_repotee
    return mg_s_direct_repotee


if __name__ == '__main__':
    emp_mgr_dict = \
    {
        'A': 'B',
        'B': 'C',
        'F': 'B',
        'D1': 'E',
        'C': 'D',
        'D': 'E'
    }
    result={}
    manager_to_emp={}
    # Method to solve in to filp the dependency from emp->mgr to mgr->list[emp]
    # pass this into DFS call to populate result dict
    # if result has i then return ans list
    # else get related list from mgr_to_emp mapping -- ie direct reportee of mgr
    # For eac of these reportee, find  & add their reportees -- DFS call

    print(f'manager_to_employee mapping')
    for e, m in emp_mgr_dict.items():
        manager_to_emp.setdefault(m, []).append(e)
    print(manager_to_emp)

    for e in manager_to_emp.keys():
        dfs_call_to_fill(e, manager_to_emp, result)
    print(result)
