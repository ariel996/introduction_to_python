def func():
    print('This is a message from the function in the imported module.')


print(f'This is a message from {__name__}.')

# Make a change here.
print('This should not be printed')

