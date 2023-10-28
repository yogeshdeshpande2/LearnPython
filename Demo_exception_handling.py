class TestException1(Exception):
    def __init__(self):
        pass

try:
    f = open('test_file_text.txt', 'r')
    if f.name == 'test_file_text.txt':
        raise TestException1

except FileNotFoundError as e:
    print(f"Error! {e}")
except TestException1 as e:
    print("Use defined exception raised here!")
except Exception as e:
    print(f'Other error! {e}')
else:
    print(f.read())
finally:
    f.close()
    print("This will always execute!")




# try:
#     f = open('test_file_text.txt', 'r')
#     # var_name = name
#
# except FileNotFoundError as e:
#     print(f"Error! {e}")
# except Exception as e:
#     print(f'Other error! {e}')
# else:
#     print(f.read())
# finally:
#     print("This will always execute!")


# try:
#     f = open('test_file_text1.txt', 'r')
# except FileNotFoundError:
#     print("Error! File not found")
# except:
#     print('Other error!')



# try:
#     pass
# except:
#     pass
# else:
#     pass
# finally:
#     pass