# Tree classifications

This repository contains classifications of some of the problems on rooted trees.

## Notation

_The following notation explanation is about 2-label setting, but can be trivially extended to a setting with > 2 labels_

We list the problems using sets of allowed restrictions. Since the tree is always binary, we’ll use _xyz_ as a shorthand for “if a node has a label _y_, then it must have 1 child with label _x_ and one child with label _z_”. E.g. _{ 121, 212 }_ means that if a node has label 2, it must have both children with label 1, and if a node has a label 1, it must have both children with label 2. Another example, _{112, 212, 122}_ means “if a node has label 1, it can either have children with labels 1 and 2 (i.e. children with different labels) or both children with labels 2; if a node has label 2, it must have children with 2 different labels (1, 2)”

## Problems

Note that we only consider problems that are non-isomorphic. E.g. { 112, 121 } and { 122, 212 } are isomorphic as we can just map ones to twos and twos to ones in the former instance to get to the latter one.

Besides, we also reduce the number of problems by eliminating redundant constraints wherever possible. E.g. {111,112,212} is in essence the same problem as {111} since 2s are never allowed to be a "parent" node.

### 2 labels

There are:

**30 non-isomorphic problems**

- 26 constant-time solvable

- 1 log-time solvable

- 1 linear-time solvable

- 1 unsolvable, which is [] i.e. emoty set of allowed configurations

- **1 unclassified (!)** The only unclassified problem is {121, 112, 212}.

All but 1 non-isomorphic problems with 2 labels have been classified. Classification results can be found [here](https://github.com/AleksTeresh/tree-classifications/blob/master/problems/2labels.json).

Most of the problems were rather trivial to classify. Lower and upper bound justifications for a not-so-trivial problem {121, 112} can be found here in [the docs folder](https://github.com/AleksTeresh/tree-classifications/tree/master/docs).

## Scripts

