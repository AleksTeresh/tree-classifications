#!/usr/bin/env python3

# sketch for an exponential algorithm determining whether problem is log* solvable or not
# missing to formally prove
# - iteratively building the set of equivalent labels by merging two sets is sound
# todo
#
# done
# - print certificate for log*n solvability
# - alleviate assumption for reaching every other label
#   - by constructing a graph (hypergraph or normal with collapsed edges) and separate each strongly connected component
#       - "fine" as removal of a rule bridging s.c.c. cannot create problems because:
#           - either the "pointed" s.c.c. is log*n solvable, then such rule is useless.
#           - Otherwise, using a rule would force subtree to be ω(log n) solvable, so again useless.

if __name__ == "__main__":
    from common import get_constraints_for_labels
else:
    from .common import get_constraints_for_labels

import networkx as nx

def is_log_star_solvable(constraints):
    G = nx.DiGraph()
    for constraint in constraints:
        G.add_edge(constraint[1], constraint[0])
        G.add_edge(constraint[1], constraint[2])
    log_star_solvable = False

    # split problem/constraints to smaller subproblems such that each small subproblem has a property that every
    # label can be reached from any other label
    for scc in nx.strongly_connected_components(G):
        reduced_constraints = [constraint for constraint in constraints if
                               (constraint[0] in scc and constraint[1] in scc and constraint[2] in scc)]
        if _is_log_star_solvable(reduced_constraints, list(scc)):
            log_star_solvable = True
            break
    return log_star_solvable

VERBOSE = False

def _is_log_star_solvable(constraints, labels):
    root_labels = [[label] for label in labels]

    if VERBOSE:
        certificate = dict()

    constrains_for_labels = get_constraints_for_labels(constraints, labels)

    while True:
        root_labels_enlarged = False
        for e1 in root_labels:
            for e2 in root_labels:
                new_root_labels = []
                for label in labels:
                    for constraint in constrains_for_labels[label]:
                        if (constraint[0] in e1 and constraint[1] in e2) or \
                                (constraint[1] in e1 and constraint[0] in e2):
                            new_root_labels.append(label)
                            break
                if new_root_labels not in root_labels:
                    root_labels.append(new_root_labels)
                    if VERBOSE:
                        certificate[tuple(new_root_labels)] = (tuple(e1),tuple(e2))
                    root_labels_enlarged = True
                    break
            if root_labels_enlarged:
                break
        if not root_labels_enlarged:
            break

    if labels not in root_labels or not constraints:  # not constraints here for the edge-case of a single label
        return False
    else:
        if VERBOSE:
            print(certificate)
        return True

if __name__ == "__main__":
    constraints = input().split()
    if is_log_star_solvable(constraints):
        print("O(log*n)")
    else:
        print("ω(log*n)")
