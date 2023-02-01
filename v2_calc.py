"""
In this version, I calculate the values in the 'key-value' pair directly inside of the dictionary instead of passing the array to each key. 
This makes for a much more efficient method and didn't have the issue of structure in the output. 
"""

def calculate(list):
    if len(list) < 9:
        print("List must contain nine numbers.")
    else:
        matrix = np.reshape(list, (3,3))
                            
        d= {
            'mean':[
                matrix.mean(axis=0).tolist(),
                matrix.mean(axis=1).tolist(),
                matrix.mean().tolist()
            ],
            'variance': [
                matrix.var(axis=0).tolist(),
                matrix.var(axis=1).tolist(),
                matrix.var().tolist()
            ],
            
            'standard deviation': [
                matrix.std(axis=0).tolist(),
                matrix.std(axis=1).tolist(),
                matrix.std().tolist()
             ], 
            
            'max': [
                matrix.max(axis=0).tolist(),
                matrix.max(axis=1).tolist(),
                matrix.max().tolist()
             ], 
            
            'min':[
                matrix.min(axis=0).tolist(),
                matrix.min(axis=1).tolist(),
                matrix.min().tolist()
             ], 
            
            'sum':[
                matrix.sum(axis=0).tolist(),
                matrix.sum(axis=1).tolist(),
                matrix.sum().tolist()
             ]
            
        }
        return d
