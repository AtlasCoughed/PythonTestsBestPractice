# Goodpractice - avoiding complex calcualtion in tests
def testGetProfitAfterRevSharing(self):
    result = profit_calculator.GetProfitAfterRevSharing(
        money.Cent(90),
        profit_calculator.RevShare(percent=20),
        profit_calculator.RevShare(percent=15),
        profit_calculator.RevShare(percent=10)),

     #TODO(someone): this test is failing even though I know its correct - better fix code!
     self.assertEqual(45, result.getCents())

#  START - Bad practice

def testGetProfitAfterRevSharing(self):
    profit = money.Cents(90)
    rev_share1 = profit_calculator.RevShare(percent=20)
    rev_share2 = profit_calculator.RevShare(percent=15)
    rev_share3 = profit_calculator.RevShare(percent=10)

    result = profit_calculator.GetProfitAfterRevSharing(profit, rev_share1, rev_share2, rev_share3)

    self.assertEqual(
        profit.GetMicros() - profit.GetMicros()
        * (rev_share1.GetFraction() + rev_share2.GetFraction() + rev_share2.GetFraction()),
        result.getMicros()
    )
# END - Bad Practice


# GOOD - CHOOSE Good representative values

def testMultiply_TwoPositiveValues_ProducesPositiveValue(self):
    self.assertEqual(6, my_math.Multiply(2,3 ))

def testMultiply_TwoNegativeAndPositiveValues_ProducesNegativeValue(self):
    self.assertEqual(6, my_math.Multiply(-2,3 ))

def testMultiply_PositiveAndNegativeValues_ProducesNegativeValue(self):
        self.assertEqual(6, my_math.Multiply(2, -3))

def testMultiply_TwoNegativeValues_ProducesPositiveValue(self):
    self.assertEqual(6, my_math.Multiply(-2, -3 ))

# END - GOOD

# START - BAD - Covers the same case of the same behavior multiple times:

def testMultiply(self):
  self.assertEqual(6, my_math.Multiply(2, 3))
  self.assertEqual(8, my_math.Multiply(2, 4))
  self.assertEqual(15, my_math.Multiply(3, 5))

# END - BAD


#######################################################

# Dos

# Approach tests as descriptions of outputs for given inputs,
# not full-fledged programs

# Write tests as straight-line code that doesn't force the reader to do mental
# computations to verify the test's correctness.

# Identify interesting boundary inputs for the code under test
# and test against those values instead of testing exhaustively using loops.


# DON'T
#
# Repeat the logic of the code under test in the test itself
# Use loops, conditionals, or complex operations in the body of a test (
# they're sometimes okay in helper methods)


