# Use setUp to define implicit defaults for tests but never let test excplicit rely on values defined in setUp

# Bad Practice #1 - Explicitly relies on a value defined in setUp:

@mock.patch.object(name_service, "GetName",
                   new=mock.MagicMock(return_value="John Doe"))
class TestService(googletest.TestCase):
    # ... hundreds of lines of tests ...

    def testShouldReturnDataFromService(self):
        details = bank.User("user").GetDetails()
        self.assertEqual("John Doe", details.name)


# Bad Practice #2 - Does irrelevant setup directly in tests

# Most of these I don't care about, but the code
# will throw exceptions if I don't set them!
@mock.patch.object(address_service, "GetAddress",
                   new=mock.MagicMock(return_value="default address"))
@mock.patch.object(phone_service, "GetPhone",
                   new=mock.MagicMock(return_value="555-5555"))
@mock.patch.object(name_service, "GetName",
                   new=mock.MagicMock(return_value="John Doe"))
@mock.patch.object(birthday_service, "GetBirthday",
                   new=mock.MagicMock(return_value="4 July 2010"))
def testShouldSetUserName(self):
    details = bank.User("user").GetDetails()
    self.assertEqual("John Doe", details.name)

    # End bad practice

    # Good: Defines defualts in setUp, overrides them in tests that care:

    @mock.patch.object(address_service, "GetAddress", new=mock.MagicMock(return_value="default address"))
    @mock.patch.object(phone_service, "GetPhone", new=mock.MagicMock(return_value="555-5555"))
    @mock.patch.object(name_service, "GetName",
                       new=mock.MagicMock(return_value="default name"))
    @mock.patch.object(birthday_service, "GetName", new=mock.MagicMock(return_value="4 July 2010"))
    class TestService(googletest.TestCase):
        # hundreds lines of code.....

        def testShouldSetUsername(self):
            with mock.patch.object(name_service, "GetName", return_value="John Doe"):
                details = bank.User('user').GetDetails()
            self.assertEqual("John Doe".details.name)

# Do

# Use setup to define safe return values for stubs so that tests won't throw unrelated exceptions but
# be careful not to rely on specific values for tests

# Use setup to define the object under test and its collaborators when they are too complex to be defined as their declaration
# Redfine the object under test and its collaborators possibly using helper methods and define different stub return
# different return values in any test methods that care about their details

# Dont

# Refer to constructor paramters that wer ebeing used in setup from within a test method
# without reconstructing the object in the test to make it clear how the parameters are related

# Rely on the specific values returned by mocks that were defined in setup
# Use setup to make calls against the class under test or perform verifications


