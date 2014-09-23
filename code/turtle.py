from __future__ import print_function, division

import thinkbayes2

class Turtle(thinkbayes2.Suite):
    """A map from string bowl ID to probablity."""

    def Likelihood(self, data, hypo):
        """The likelihood of the data under the hypothesis.

        data: string cookie type
        hypo: string bowl ID
        """
        like = hypo[data] / hypo.Total()
        return like


def main():
    t0 = thinkbayes2.Hist(dict(blue=1, green=0))
    t1 = thinkbayes2.Hist(dict(blue=2/3, green=1/3))
    t2 = thinkbayes2.Hist(dict(blue=1/3, green=2/3))
    t3 = thinkbayes2.Hist(dict(blue=0, green=1))
    pmf = Turtle([t0,t1,t2,t3])

    pmf.Update('green')
    for hypo, prob in pmf.Items():
        print(hypo, prob)

if __name__ == '__main__':
    main()
