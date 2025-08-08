'''
    This file contains the template for Assignment1.  For testing it, I will place it
    in a different directory, call the function <min_num_attendees>, and check its output.
    So, you can add/remove  whatever you want to/from this file.  But, don't change the name
    of the file or the name/signature of the following function.

    Also, I will use <python3> to run this code.
'''

"""
    D = # of days for book release event
    n = # of book clubs attending
    {c1, c2,..., cn} = {# members in club 1, # in club 2,..., # in club n}
    

"""

def min_num_attendees(input_file_path, output_file_path):
    '''
        This function will contain your code.  It wil read from the file <input_file_path>,
        and will write its output to the file <output_file_path>.
    '''

    infile = open(input_file_path, 'r')
    D = int(infile.readline().strip())
    clubs = []
    for x in infile.readline().strip().split(','):
        clubs.append(int(x))
    infile.close()

    """
        new algorithm here
    """
    
    #initializing sum array with n+1 elements
    n = len(clubs)
    sum = [0] * (n+1)
    
    # 2D array of all the iterations
    all_clubs = [[0 for _ in range(n)] for _ in range(D)]
    
    # put all the 
    for i in range (n):
        all_clubs[0][i] = clubs [i]
        



    outfile = open(output_file_path, 'w')
   # outfile.write(str(low) + '\n')
    outfile.close()

'''
    To test your function, you can uncomment the following command with the the input/output
    files paths that you want to read from/write to.  Do NOT forget to comment it out before
    submitting.
'''
#min_num_attendees('GA1_test_cases/input1.txt', 'testing_output_files/output_text.txt')