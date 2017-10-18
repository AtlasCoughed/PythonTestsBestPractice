# Goodpractice - avoiding complex calcualtion in tests
def testGetProfitAfterRevSharing(self):
    result = profit_calculator.GetProfitAfterRevSharing(
        money.Cent(90),
        profit_calculator.RevShare(percent=20),
        profit_calculator.RevShare(percent=15),
        profit_calculator.RevShare(percent=10)),

     #TODO(someone): this test is failing even though I know its correct - better fix code!
     self.assertEqual(45, result.getCents())

# Bad practice

def testGetProfitAfterRevSharing(self):
    profit = money.Cents(90)
    rev_share1 = profit_calculator.RevShare(percent=20)
    rev_share2 = profit_calculator.RevShare(percent=15)
    rev_share3 = profit_calculator.RevShare(percent=10)

    result = profit_calculator.GetProfitAfterRevSharing(profit, rev_share1, rev_share2, rev_share3)