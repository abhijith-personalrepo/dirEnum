import optparse
import os

def print_tree(start_path, indent=""):
    # If the start path is a file, print its name and return    
    if os.path.isfile(start_path):
        print(indent + start_path)
        return

    if not os.path.isdir(start_path):
        print(f"{start_path} is not a directory")
        return
    files = []
    # error controls
    try:
        files = os.listdir(start_path)
    except FileNotFoundError:
        print("The specified directory does not exist.")
        pass
    except NotADirectoryError:
        print("The specified path is not a directory.")
        pass
    except PermissionError:
        print("You do not have permission to access the specified directory.")
    except Exception as e:
        print("An error occurred:", e)
    #printing all files in the dir
    for file in files:
        try:
            if file.startswith("."):
                print_tree(os.path.join(start_path, file), indent + "**")
            else:
                print_tree(os.path.join(start_path, file), indent + "")
        except FileNotFoundError:
            pass
        except OSError:
            continue
        except BrokenPipeError:
            print("An error occurred:", e)



def print_count(*args, **kwargs):
    text = " ".join(map(str, args))
    count = len(text)
    print(text, **kwargs)
    return count+1


if __name__ == "__main__":
    parser= optparse.OptionParser()
    parser.add_option("-p","--path", dest="path",help="Path to destination folder from /")
    (options,arguments) = parser.parse_args()
    path = options.path
    if not path:
        path = input("Enter the path to destination folder from / : ")
    if os.path.isdir(path):
        count = print_count("Printing directory list inside "+ path)
        print("*"*count)
        print_tree(path,"")
    #else:
        print("Please specify a valid directory path using the -p argument.")

