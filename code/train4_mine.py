"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

from dice import Dice
import thinkplot


class Train(Dice):
    """Represents hypotheses about how many trains the company has.

    The likelihood function for the train problem is the same as
    for the Dice problem.
    """
    def Likelihood(self, data, hypo):
        k, m = data
        if hypo < m:
            return 0
        else:
            return (1/hypo) * (m/hypo)**(k-1)


def main():
    hypos = range(1, 1001)
    suite = Train(hypos)
    data = (3,70)

    suite.Update(data)
    thinkplot.Pmf(suite, label='after (%d, %d)' % data)

    thinkplot.Show(xlabel='Number of trains',
                   ylabel='PMF')

    print('posterior mean', suite.Mean())


if __name__ == '__main__':
    main()
