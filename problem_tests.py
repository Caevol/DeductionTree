#this is a test created by you that runs and returns a list of Problems associated with it if the test fails
class problem_test:

    def run_test(self):
        return self.test()

    def get_problem_list(self):
        return self.problem_list

    # constructor takes 2 variables
    # First is a list of Problems that are an issue if the test fails
    # Second is the test you want to run
    # Optional third so you can describe the test
    def __init__(self, prob_list, test_function, description=''):
        self.test_desc = description
        self.test = test_function
        self.problem_list = prob_list