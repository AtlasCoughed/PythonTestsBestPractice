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

# BAD START - Injecting objects to encapsulate difficult-to-test code mocking out difficult to test code

class TransactionProcessor(object):
    def ProcessTransaction(self, transaction):
        # Do some interesting stuff...
        self._SaveToDatabase(transaction)

    def _SaveToDatabase(self, transaction):
        self.database.put(transaction.id, transaction)

def testShouldSaveToDatabase(self):
    # Define a new class that keeps track of whether _SaveToDatabase was called
    class TestTransactionProcssor(bank.TransactionProcessor):
        def _SaveToDatabase(self, transaction):
            self.saved_to_database = True

    processor = TestTransactionProcessor()
    processor.ProcessTransaction(bank.Transaction("id"))
    self.assertTrue(processor.saved_to_database)

# BAD END - -----

# Good START --- Mocks Objects encapsulating untestable code and uses public API

    # DO
    #
    # Make calls only against a class's externally visible (i.e., public and protected) methods in unit tests
    # C++ and Java: Expose only constants, and only when necessary
    # If you expose constants in Java, please mark the modifications with @VisibleForTesting
    # Replace untestable code with mocks or fakes in tests
    # Refactor private methods you want to test directly into their own component
    #
    # DON'T
    #
    # Increase visibility for methods that would otherwise be private in
    # order to expose them to unit tests
    # Extend a class under test to override certain methods and change their behavior
    #
    # Write tests that exercise a
    # class in a way that a user wouldn't be able to understand


def testShouldSaveToDatabase(self):
    database = db.InMemoryDatabase()
    with mock.patch.object(db, 'HeavyweightDatabase', return_value = database):
        processor = bank.TransactionProcessor()
        transaction = bank.Transaction('id')

        processor.ProcessTransaction(transaction)

    self.assertEqual(transaction, database.get('id'))

# Good END

