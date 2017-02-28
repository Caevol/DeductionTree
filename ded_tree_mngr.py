#Author: Logan Pedersen


from problem import Problem
from problem_tests import problem_test
from itertools import chain

#basic functions built just to be plugged into the problem_tests
def basic_test_true():
    return True

def basic_test_false():
    return False


#This is an example problem tree to create more trees from (Trees can go much deeper than 1 or 2 layers)
def create_problem_tree():
    #Create leaf problems (These ones simply return a fix when they are reached in the tree
    leaf_1 = Problem('Leaf 1!')
    leaf_2 = Problem('Leaf 2!')
    leaf_3 = Problem('Leaf 3!')
    leaf_4 = Problem('Leaf 4!')
    leaf_5 = Problem('leaf 5!')
    leaf_6 = Problem('leaf 6!')

    #Define layer of tests above them
    cpu_test = problem_test([leaf_1, leaf_2, leaf_3], basic_test_false, 'cpu test')
    ip_test = problem_test([leaf_3, leaf_5, leaf_6], basic_test_false, 'ip test')
    computer_test = problem_test([leaf_2, leaf_4, leaf_5, leaf_3], basic_test_false, 'computer test')

    #define root problem, things don't work
    root_problem = Problem('Server is broken', [cpu_test, ip_test, computer_test])
    return root_problem

#This is the big worker function, it takes a problem, runs the tests inside the problem, and generates a list of
#problems using an intersection. Then, it runs this same function on those new problems. Eventually returning a big list
#of problems and fixes.
def get_diagnosis(top_problem):
    if len(top_problem.getTests()) == 0:
        return top_problem.getProblem()
    else:
        intersect_list = []
        for t in top_problem.getTests():
            if not t.test():
                intersect_lists(intersect_list, t.get_problem_list())

        ret_list = [get_diagnosis(prob) for prob in intersect_list]
        return [item for sublist in ret_list for item in sublist]

#Takes two lists and returns the elements that are in common between them
def intersect_lists(intersect_list, new_list):
    if len(new_list) == 0:
        return None
    elif len(intersect_list) == 0:
        intersect_list.extend(new_list)
    else:
        remove_list = [x for x in intersect_list if x not in new_list]
        for val in remove_list:
            intersect_list.remove(val)


if __name__ == '__main__':
    print get_diagnosis(create_problem_tree())


