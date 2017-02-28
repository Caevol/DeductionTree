# The class Problem, contains a string that describes the problem,
# if the problem is simple, that string also explains the fix
# Problem contains a list of Problem_Tests, which are run to discover more deep rooted problems in the system.
class Problem:


    problem_description = ''
    tests = []


    # prob_1 = Problem('CPU overheating', list_of_tests_you've_made)
    # alternatively, you can make a fix object that when reached returns a recommended solution to a server
    # solution_1 = Problem('CPU is boiling, pour water on it')
    def __init__(self, description_string, tests_list=[]):
        self.problem_description = description_string
        self.tests = tests_list


    # returns the problem you defined
    def getProblem(self):
        return str(self.problem_description)

    def getTests(self):
        return self.tests