"""This file contains code for use with "Think Bayes",
by Allen B. Downey, available from greenteapress.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function, division

from thinkbayes2 import Pmf

class Bowl(object):
    """An object representing a bowl of cookies"""
    def __init__(self, bowlContents):
      self.contents= bowlContents

    def total(self):
      sum = 0
      for val in self.contents.values():
        sum += val
      return sum

class Cookie(Pmf):
  """A map from string bowl ID to probablity."""

  def __init__(self, hypos, bowls):
    """Initialize self.

    hypos: sequence of string bowl IDs
    """
    Pmf.__init__(self)
    for hypo in hypos:
      self.Set(hypo, 1)
    self.Normalize()
    self.bowls = dict()
    for bowl in bowls.keys():
      self.bowls[bowl] = Bowl(bowls[bowl])

  def Update(self, data):
    """Updates the PMF with new data.

    data: string cookie type
    """
    for hypo in self.Values():
      like = self.Likelihood(data, hypo)
      self.Mult(hypo, like)
    self.Normalize()

  def Likelihood(self, data, hypo):
    """The likelihood of the data under the hypothesis.

    data: string cookie type
    hypo: string bowl ID
    """
    bowl = self.bowls[hypo]
    totalCookies = bowl.total()
    like = bowl.contents[data]/totalCookies
    bowl.contents[data] -= 1
    return like


def main():
  bowls = {
    'Bowl 1':dict(vanilla=30, chocolate=10),
    'Bowl 2':dict(vanilla=20, chocolate=20),
  }

  hypos = list(bowls.keys())

  pmf = Cookie(hypos, bowls)

  pmf.Update('vanilla')
  pmf.Update('chocolate')
  pmf.Update('chocolate')

  for hypo, prob in pmf.Items():
    print(hypo, prob)


if __name__ == '__main__':
  main()
