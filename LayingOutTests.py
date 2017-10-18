# Unit tests tend to have a very regular structure.
# A common way to refer to this structure is arrange, act, assert:
# every test must arrange the state of the world to test,
# act on the class under test by calling methods, and
# assert that the world is in the expected state afterward.


# Bad: Interleaves arrange, act, and assert calls:

def testShouldReloadData(self):
  with mock.patch.object(my_package, "GetData", return_value="data1"):
    obj = my_package.MyClass()
    self.assertIsNone(obj.GetData())
    obj.LoadData()
    self.assertEqual("data1", obj.GetData())
  with mock.patch.object(myservice, "GetData", return_value="data2"):
    obj.LoadData()
    self.assertEqual("data2", obj.GetData())

# Defines difficult to distinguish arrange, act, and assert blocks:

def testShouldReloadData(self):
  obj = my_package.MyClass()
  with mock.patch.object(my_package, "GetData", side_effect=("data1", "data2")):
    obj.LoadData()

    obj.LoadData()
    self.assertEqual("data2", obj.GetData())

# End BAD

# Start GOOD
# Lays out arrange, act, assert blocks in a clear way:

def testShouldReloadData(self):
    obj = my_package.MyClass()

    with mock.patch.object(my_package, "GetData", side_effect=('data1', 'data2')):
        obj.LoadData()
        obj.LoadData()
        result = obj.GetData()

    self.assertEqual('data2', result)

