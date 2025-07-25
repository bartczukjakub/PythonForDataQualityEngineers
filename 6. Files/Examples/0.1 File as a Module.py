a = 10
print(a)

# The tst has print statement inside, and when we import the module the entire file is run
import tst as test_module
print(a)
print (test_module.a)

# The tst2 module also has a print inside, however with a if __name__ == __main__ statement.
# When we import the module we changed its name to test_module_2 (or the default one) so its name doesn't equal __main__ anymore
import tst2 as test_module_2

print(f'Test module name is: {test_module_2.__name__}')

print(f'Current module name is: {__name__}')

print(test_module_2.a)