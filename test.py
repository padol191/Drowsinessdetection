import re

# Function checks if the string
# contains any special character


def run(string):

    # Make own character set and pass
    # this as argument in compile method
    regex = re.compile('[@#$%*}{~:]')

    # Pass the string in search
    # method of regex object.
    if(regex.search(string) == None):
        print("String is accepted")

    else:
        print("String is not accepted.")


# Driver Code
if __name__ == '__main__':

    # Enter the string
    string = "GeeksForGeeks"

    # calling run function
    run(string)
