

import desolver
import numpy
import pickle

# simple error function
def error_func(indiv, *args):
    # inverse exponential with offset, y = a * exp(b/x) + c
    predicted = indiv[0] * numpy.exp(indiv[1] / args[0]) + indiv[2]

    # sum of squared error
    error = predicted - args[1]
    return numpy.sum(error*error)

class TestDesolver():
    def setUp(self):
        self.xData = numpy.array([5.357, 9.861, 5.457, 5.936, 6.161, 6.731])
        self.yData = numpy.array([0.376, 7.104, 0.489, 1.049, 1.327, 2.077])

    def test_basic(self):
        solver = desolver.DESolver(error_func,
                                   [(-100,100)]*3, 30, 200,
                                   method = desolver.DE_RAND_1,
                                   args=[self.xData,self.yData],
                                   scale=0.8, crossover_prob=0.9,
                                   goal_error=.01, polish=False, verbose=False,
                                   use_pp = False, pp_modules=['numpy'])

        assert(solver.best_error <= .01)

    def test_pickle(self):
        # run the example solver
        solver = desolver.DESolver(error_func,
                                   [(-100,100)]*3, 30, 200,
                                   method = desolver.DE_RAND_1,
                                   args=[self.xData,self.yData],
                                   scale=0.8, crossover_prob=0.9,
                                   goal_error=.01, polish=False, verbose=False,
                                   use_pp = False, pp_modules=['numpy'])
        # pickle and unpickle it
        pstr = pickle.dumps(solver)
        solver2 = pickle.loads(pstr)

        # verify that we can access the data

    def test_seed(self):
        solver = desolver.DESolver(error_func,
                                   [(-100,100)]*3, 30, 200,
                                   method = desolver.DE_LOCAL_TO_BEST_1,
                                   args=[self.xData,self.yData], 
                                   seed = numpy.random.uniform(-1,1,size=(4,3)),
                                   scale=0.5, crossover_prob=0.9,
                                   goal_error=.01, polish=False, verbose=False,
                                   use_pp = False, pp_modules=['numpy'])

        assert(solver.best_error <= .01)

    def test_pp(self):
        solver = desolver.DESolver(error_func,
                                   [(-100,100)]*3, 30, 200,
                                   method = desolver.DE_RAND_1,
                                   args=[self.xData,self.yData],
                                   scale=0.8, crossover_prob=0.9,
                                   goal_error=.01, polish=False, verbose=False,
                                   use_pp = True, pp_modules=['numpy'])

        assert(solver.best_error <= .01)

    def test_polish(self):
        solver = desolver.DESolver(error_func,
                                   [(-100,100)]*3, 30, 200,
                                   method = desolver.DE_RAND_1,
                                   args=[self.xData,self.yData],
                                   scale=0.8, crossover_prob=0.9,
                                   goal_error=.01, polish=True, verbose=False,
                                   use_pp = False, pp_modules=['numpy'])

        assert(solver.best_error <= .01)
