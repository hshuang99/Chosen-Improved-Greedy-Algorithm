import operations
from cost_function import operationCost
import numpy as np

def row_op_sel(L_row, L_row_cst, mat, inverse, p_value, minm_cost, select_list):
    for row_op in L_row:
        tmp_mat = operations.row_i2j(mat, row_op[0], row_op[1])
        tmp_inverse = operations.col_i2j(inverse, row_op[1], row_op[0])
        L_row_cst.append(operationCost(tmp_mat, tmp_inverse, p_value, 0))

    for index, row_op_cst in enumerate(L_row_cst):
        if row_op_cst < minm_cost:
            select_list.clear()
            select_list.append((L_row[index][0], L_row[index][1], 0))
            minm_cost = row_op_cst
        elif row_op_cst == minm_cost:
            select_list.append((L_row[index][0], L_row[index][1], 0))
    return select_list, minm_cost
def col_op_sel(L_col, L_col_cst, mat, inverse, p_value, minm_cost, select_list):
    for col_op in L_col:
        tmp_mat = operations.col_i2j(mat, col_op[0], col_op[1])
        tmp_inverse = operations.row_i2j(inverse, col_op[1], col_op[0]) 
        L_col_cst.append(operationCost(tmp_mat, tmp_inverse, p_value, 1))

    for index, col_op_cst in enumerate(L_col_cst):
        if col_op_cst < minm_cost:
            select_list.clear()
            select_list.append((L_col[index][0], L_col[index][1], 1))
            minm_cost = col_op_cst #update the new cost
        elif col_op_cst == minm_cost:
            select_list.append((L_col[index][0], L_col[index][1], 1))
    return select_list, minm_cost
def B_row_sel(L_row, L_row_cst, mat, inverse, p_value, minm_cost, best_row_cst, B_row):
    for op_row in L_row:
        tmp_row_mat = operations.row_i2j(mat, op_row[0], op_row[1])
        tmp_row_inv = operations.col_i2j(inverse, op_row[1], op_row[0])
        L_row_cst.append(operationCost(tmp_row_mat, tmp_row_inv, p_value, 0))

    for index, row_op_cst in enumerate(L_row_cst):
        if row_op_cst < minm_cost:
            if row_op_cst < best_row_cst:
                B_row = []
                B_row.append((L_row[index][0], L_row[index][1], 0))
                best_row_cst = row_op_cst
        elif row_op_cst == minm_cost:
            B_row.append((L_row[index][0], L_row[index][1], 0))
    return B_row, best_row_cst
def B_col_sel(L_col, L_col_cst, mat, inverse, p_value, minm_cost, best_col_cst, B_col):
    for op_col in L_col:
        tmp_col_mat = operations.col_i2j(mat, op_col[0], op_col[1])
        tmp_col_inv = operations.row_i2j(inverse, op_col[1], op_col[0])
        L_col_cst.append(operationCost(tmp_col_mat, tmp_col_inv, p_value, 1))

    for index, col_op_cst in enumerate(L_col_cst):
        if col_op_cst < minm_cost:
            if col_op_cst < best_col_cst:
                B_col = []
                B_col.append((L_col[index][0], L_col[index][1], 1))
                best_col_cst = col_op_cst
        elif col_op_cst == minm_cost:
            B_col.append((L_col[index][0], L_col[index][1], 1))
    return B_col, best_col_cst
def rand_row_sel(L_row, mat, inverse, p_value, escapeCandidates):
    for op_row in L_row:
        tmp_row_mat = operations.row_i2j(mat, op_row[0], op_row[1])
        tmp_row_inv = operations.col_i2j(inverse, op_row[1], op_row[0])
        tmp_row_cst = operationCost(tmp_row_mat, tmp_row_inv, p_value, 0)
        escapeCandidates.append((tmp_row_cst, op_row[0], op_row[1], 0))
    return escapeCandidates
def rand_col_sel(L_col, mat, inverse, p_value, escapeCandidates):
    for op_col in L_col:
        tmp_col_mat = operations.col_i2j(mat, op_col[0], op_col[1])
        tmp_col_inv = operations.row_i2j(inverse, op_col[1], op_col[0])
        tmp_col_cst = operationCost(tmp_col_mat, tmp_col_inv, p_value, 1)
        escapeCandidates.append((tmp_col_cst, op_col[0], op_col[1], 1))
    return escapeCandidates
