"""
In this version I manually created an array for each key in the dictionary (d). 
This got the correct output but the test didn't like the format of the arrays since they were numpy arrays. 
Also, it was very long and cumbersome code that had a lot of extra steps and repetition
"""

def calculate(list):
    if len(list) < 9:
        print("List must contain nine numbers.")
    else:
        d={}
        matrix = np.reshape(list, (3,3))
                            
        for num in matrix:
            h_mean = np.mean(matrix, axis=0)
            h_var = np.var(matrix, axis=0)
            h_std = np.std(matrix, axis=0)
            h_max = np.max(matrix, axis=0)
            h_min = np.min(matrix, axis=0)
            h_sum = np.sum(matrix, axis=0)
            
            v_mean = np.mean(matrix, axis=1)
            v_var = np.var(matrix, axis=1)
            v_std = np.std(matrix, axis=1)
            v_max = np.max(matrix, axis=1)
            v_min = np.min(matrix, axis=1)
            v_sum = np.sum(matrix, axis=1)

            f_mean = np.mean(list)
            f_var = np.var(list)
            f_std = np.std(list)
            f_max = np.max(list)
            f_min = np.min(list)
            f_sum = np.sum(list)

            all_mean= []
            all_var = []
            all_std = []
            all_max = []
            all_min = []
            all_sum = []

            

            all_var.append(h_var) 
            all_var.append(v_var) 
            all_var.append(f_var) 

            all_std.append(h_std) 
            all_std.append(v_std) 
            all_std.append(f_std) 

            all_max.append(h_max) 
            all_max.append(v_max) 
            all_max.append(f_max)  

            all_min.append(h_min) 
            all_min.append(v_min) 
            all_min.append(f_min) 


            all_sum.append(h_sum) 
            all_sum.append(v_sum) 
            all_sum.append(f_sum) 


            d={
                'mean': all_mean, 
                 'variance': all_var, 
                  'standard deviation': all_std, 
                  'max': all_max, 
                  'min':all_min, 
                  'sum':all_sum
                 }
            return d
