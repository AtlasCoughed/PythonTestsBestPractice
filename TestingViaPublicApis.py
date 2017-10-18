# Tests should focus on testing your code's public API, and your code's implementation
#  details shouldn't need to be exposed to tests



# BAD - Tests private implementation details directly rather than using the public API:

def ProcessTransaction(transaction):
  if _IsValid(transaction):
    _SaveToDatabase(transaction)

def _IsValid(transaction):
  return transaction.GetAmount() < transaction.GetSender().GetBalance()

def _SaveToDataBase(transaction):
  # compute serialized transaction
  database.put(transaction.id, serialized_transaction)

def testIsValid(self):
    self.assertFalse(bank._isValid(bank.Transaction(source=EMPTY_ACCOUNT)),
                     msg="Empty account should not be valid")
    self.assertTrue(bank._IsValid(bank.Transaction(source=ACCOUNT_WITH_FUNDS)),
                  msg="Accounts with funds should be valid")

def testSaveToDatabase(self):
    _SaveToDataBase(bank.Transaction(id="123", data="abcxyz"))
    self.assertEqual('abcxyz', database.get('123'))

# END BAD -

# GOOD implementation: Tests iplementation details via the public api:

def testsShouldSaveValidTransaction(self):
    bank.ProcessTransaction(bank.Transaction(id="123", data="abcxyz", source=ACCOUNT_WITH_FUNDS))\
    self.assertEqual('abcxyz', database.get("123"))

def testShouldNotSaveInvalidTransactions(self):
    bank.ProcessTransaction(bank.Transaction(source=EMPTY_ACCOUNT))
    self.assertTrue(database.IsEmpty())

# END Good

# GOOD START - Injecting objects to encapsulate difficult-to-test code mocking out difficult to test code

class TransactionProcessor(object):
    def ProcessTransaction(self, transaction):
        # Do some interesting stuff...
        self._SaveToDatabase(transaction)

    def _SaveToDatabase(self, transaction):
        self.database.put(transaction.id, transaction)

def